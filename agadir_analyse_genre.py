"""
Plateforme d'Analyse Budgétaire Genrée et Géospatiale - Ville d'Agadir
========================================================================

Ce script combine:
1. Analyse budgétaire genrée
2. Analyse géospatiale urbaine (OSM/UrbanPy)
3. Visualisation cartographique interactive
4. Génération de rapports et recommandations

Auteur: Système d'Analyse Budgétaire Genrée
Date: 2025
"""

import warnings
warnings.filterwarnings('ignore')

import pandas as pd
import numpy as np
import geopandas as gpd
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
from shapely.geometry import Point, Polygon
import folium
from datetime import datetime
import json

# Tentative d'import des bibliothèques géospatiales (optionnelles)
try:
    import osmnx as ox
    import h3
    GEOSPATIAL_AVAILABLE = True
except ImportError:
    print("⚠️ Bibliothèques géospatiales non disponibles. Installation: pip install osmnx h3")
    GEOSPATIAL_AVAILABLE = False


class AgadirBudgetGenreAnalyzer:
    """
    Analyseur intégré pour la budgétisation genrée territoriale d'Agadir
    """
    
    def __init__(self):
        """Initialisation de l'analyseur"""
        self.city_name = "Agadir, Morocco"
        self.city_coords = (30.4278, -9.5981)  # Latitude, Longitude
        self.population = 950000
        self.budget_total = 1200  # Millions DH
        
        # Quartiers d'Agadir
        self.quartiers = {
            'Centre-Ville': {'pop': 85000, 'coords': (30.4278, -9.5981), 'score': 8.5},
            'Talborjt': {'pop': 120000, 'coords': (30.4100, -9.5800), 'score': 7.2},
            'Bensergao': {'pop': 95000, 'coords': (30.4400, -9.6100), 'score': 5.8},
            'Tikiouine': {'pop': 78000, 'coords': (30.4500, -9.5700), 'score': 5.2},
            'Hay Mohammadi': {'pop': 110000, 'coords': (30.4000, -9.6000), 'score': 7.8},
            'Anza': {'pop': 92000, 'coords': (30.3900, -9.5500), 'score': 8.2}
        }
        
        # Configuration budget par secteur
        self.budget_data = None
        self.initialize_budget_data()
        
    def initialize_budget_data(self):
        """Initialiser les données budgétaires"""
        self.budget_data = pd.DataFrame({
            'Secteur': [
                'Éducation & Formation',
                'Santé & Services Sociaux',
                'Transport & Mobilité',
                'Infrastructure Urbaine',
                'Développement Économique',
                'Espaces Verts & Loisirs',
                'Administration & RH'
            ],
            'Budget_MDH': [180, 220, 160, 280, 140, 100, 120],
            'Part_Genree_Pct': [65, 58, 42, 35, 48, 38, 15],
            'Classification': [
                'Genrée Active', 'Genrée Active', 'Genrable',
                'Genrable', 'Genrée Active', 'Genrable', 'Neutre'
            ],
            'Priorite': [3, 3, 2, 2, 3, 2, 1]
        })
        
        # Calculer les montants genrés
        self.budget_data['Montant_Genre_MDH'] = (
            self.budget_data['Budget_MDH'] * 
            self.budget_data['Part_Genree_Pct'] / 100
        )
        
    def generer_statistiques_globales(self):
        """Générer les statistiques globales de la ville"""
        stats = {
            'population': self.population,
            'population_femmes': int(self.population * 0.51),
            'population_hommes': int(self.population * 0.49),
            'budget_total': self.budget_total,
            'budget_genre_sensible': self.budget_data['Montant_Genre_MDH'].sum(),
            'pct_budget_genre': round(
                (self.budget_data['Montant_Genre_MDH'].sum() / self.budget_total) * 100, 1
            ),
            'nb_quartiers': len(self.quartiers),
            'score_moyen_genre': round(
                np.mean([q['score'] for q in self.quartiers.values()]), 1
            )
        }
        
        return stats
    
    def analyser_budget_par_classification(self):
        """Analyser la répartition budgétaire par classification genre"""
        classification_stats = self.budget_data.groupby('Classification').agg({
            'Budget_MDH': 'sum',
            'Montant_Genre_MDH': 'sum'
        }).reset_index()
        
        classification_stats['Pct_Total'] = (
            classification_stats['Budget_MDH'] / self.budget_total * 100
        ).round(1)
        
        return classification_stats
    
    def identifier_zones_prioritaires(self):
        """Identifier les zones/quartiers prioritaires"""
        quartiers_df = pd.DataFrame([
            {
                'Quartier': nom,
                'Population': data['pop'],
                'Score_Genre': data['score'],
                'Latitude': data['coords'][0],
                'Longitude': data['coords'][1]
            }
            for nom, data in self.quartiers.items()
        ])
        
        # Identifier les priorités
        quartiers_df['Priorite'] = quartiers_df['Score_Genre'].apply(
            lambda x: 'Prioritaire' if x < 6 else ('À améliorer' if x < 7.5 else 'Satisfaisant')
        )
        
        # Calculer budget recommandé proportionnel à la priorité
        quartiers_df['Budget_Recommande_MDH'] = quartiers_df.apply(
            lambda row: (row['Population'] / self.population * self.budget_total) * 
                       (1.3 if row['Priorite'] == 'Prioritaire' else 
                        1.1 if row['Priorite'] == 'À améliorer' else 1.0),
            axis=1
        ).round(1)
        
        return quartiers_df.sort_values('Score_Genre')
    
    def calculer_indicateurs_performance(self):
        """Calculer les indicateurs de performance genre"""
        indicateurs = {
            'Pct_Femmes_Conseil_Municipal': {
                '2023': 28, '2024': 32, 'Objectif_2025': 35
            },
            'Ecart_Salarial_FH_Pct': {
                '2023': -15, '2024': -12, 'Objectif_2025': -8
            },
            'Taux_Feminisation_Cadres_Pct': {
                '2023': 32, '2024': 36, 'Objectif_2025': 40
            },
            'Places_Creches_Pour_1000': {
                '2023': 45, '2024': 52, 'Objectif_2025': 65
            },
            'Sentiment_Securite_Femmes_Pct': {
                '2023': 58, '2024': 64, 'Objectif_2025': 75
            },
            'Formation_Genre_Personnel_Pct': {
                '2023': 32, '2024': 48, 'Objectif_2025': 70
            }
        }
        
        # Calculer la progression
        indicateurs_df = pd.DataFrame(indicateurs).T
        indicateurs_df['Progression_Pct'] = (
            (indicateurs_df['2024'] - indicateurs_df['2023']) /
            abs(indicateurs_df['Objectif_2025'] - indicateurs_df['2023']) * 100
        ).round(1)
        
        return indicateurs_df
    
    def generer_recommandations(self):
        """Générer des recommandations stratégiques"""
        zones_prioritaires = self.identifier_zones_prioritaires()
        zones_faibles = zones_prioritaires[
            zones_prioritaires['Priorite'] == 'Prioritaire'
        ]
        
        recommandations = {
            'immediates': [
                {
                    'titre': 'Renforcement Zones Défavorisées',
                    'zones': zones_faibles['Quartier'].tolist(),
                    'budget_requis': zones_faibles['Budget_Recommande_MDH'].sum(),
                    'impact': f"{zones_faibles['Population'].sum()} habitants",
                    'actions': [
                        'Créer 3 nouvelles crèches municipales',
                        'Renforcer l\'éclairage public (50 km de voiries)',
                        'Installer 25 arrêts de bus sécurisés',
                        'Ouvrir 2 centres de santé femmes'
                    ]
                },
                {
                    'titre': 'Sécurité Urbaine Genrée',
                    'zones': ['Toute la ville'],
                    'budget_requis': 45,
                    'impact': 'Toute la population',
                    'actions': [
                        'Vidéosurveillance intelligente (200 caméras)',
                        'Patrouilles nocturnes renforcées',
                        'Application mobile alerte sécurité',
                        'Formation agents sécurité sur genre'
                    ]
                }
            ],
            'moyen_terme': [
                {
                    'secteur': 'Transport',
                    'projet': 'BHNS - Bus à Haut Niveau de Service',
                    'budget': 180,
                    'delai': '2025-2026',
                    'impact': '+45% mobilité femmes'
                },
                {
                    'secteur': 'Santé',
                    'projet': 'Centres Santé Femmes de Proximité',
                    'budget': 65,
                    'delai': '2025',
                    'impact': '+60% accès soins femmes'
                },
                {
                    'secteur': 'Économie',
                    'projet': 'Fonds Entrepreneuriat Féminin',
                    'budget': 40,
                    'delai': '2025-2027',
                    'impact': '500 nouvelles entreprises'
                }
            ],
            'budget_total_recommande': 555  # Millions DH
        }
        
        return recommandations
    
    def creer_carte_interactive(self, output_file='agadir_carte_genre.html'):
        """Créer une carte interactive avec Folium"""
        # Créer la carte centrée sur Agadir
        m = folium.Map(
            location=self.city_coords,
            zoom_start=12,
            tiles='OpenStreetMap'
        )
        
        # Ajouter les marqueurs pour chaque quartier
        for nom, data in self.quartiers.items():
            # Couleur selon le score
            if data['score'] >= 8:
                color = 'green'
                statut = '✓ Excellent'
            elif data['score'] >= 6:
                color = 'orange'
                statut = '⚡ À améliorer'
            else:
                color = 'red'
                statut = '⚠️ Prioritaire'
            
            # Créer le popup
            popup_html = f"""
            <div style="font-family: Arial; width: 250px;">
                <h3 style="color: #1e3c72; margin-bottom: 10px;">{nom}</h3>
                <p><strong>Population:</strong> {data['pop']:,}</p>
                <p><strong>Score Genre:</strong> {data['score']}/10</p>
                <p style="color: {color}; font-weight: bold;">{statut}</p>
            </div>
            """
            
            folium.Marker(
                location=data['coords'],
                popup=folium.Popup(popup_html, max_width=300),
                icon=folium.Icon(color=color, icon='info-sign'),
                tooltip=nom
            ).add_to(m)
        
        # Sauvegarder la carte
        m.save(output_file)
        print(f"✅ Carte interactive sauvegardée: {output_file}")
        
        return m
    
    def visualiser_budget_par_secteur(self):
        """Créer une visualisation du budget par secteur"""
        fig = px.bar(
            self.budget_data,
            x='Secteur',
            y='Budget_MDH',
            color='Classification',
            title='Budget 2025 par Secteur et Classification Genre',
            labels={'Budget_MDH': 'Budget (Millions DH)', 'Secteur': 'Secteur'},
            color_discrete_map={
                'Genrée Active': '#48bb78',
                'Genrable': '#ed8936',
                'Neutre': '#cbd5e0'
            }
        )
        
        fig.update_layout(
            xaxis_tickangle=-45,
            height=500,
            showlegend=True
        )
        
        return fig
    
    def visualiser_evolution_indicateurs(self):
        """Visualiser l'évolution des indicateurs dans le temps"""
        indicateurs_df = self.calculer_indicateurs_performance()
        
        fig = go.Figure()
        
        for idx, indicateur in enumerate(indicateurs_df.index):
            fig.add_trace(go.Scatter(
                x=['2023', '2024', 'Objectif 2025'],
                y=[
                    indicateurs_df.loc[indicateur, '2023'],
                    indicateurs_df.loc[indicateur, '2024'],
                    indicateurs_df.loc[indicateur, 'Objectif_2025']
                ],
                mode='lines+markers',
                name=indicateur,
                line=dict(width=3),
                marker=dict(size=10)
            ))
        
        fig.update_layout(
            title='Évolution des Indicateurs de Performance Genre',
            xaxis_title='Année',
            yaxis_title='Valeur',
            height=500,
            hovermode='x unified'
        )
        
        return fig
    
    def generer_rapport_complet(self, output_file='rapport_agadir_2025.json'):
        """Générer un rapport complet en JSON"""
        rapport = {
            'ville': self.city_name,
            'date_rapport': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'statistiques_globales': self.generer_statistiques_globales(),
            'budget_par_classification': self.analyser_budget_par_classification().to_dict('records'),
            'zones_prioritaires': self.identifier_zones_prioritaires().to_dict('records'),
            'indicateurs_performance': self.calculer_indicateurs_performance().to_dict(),
            'recommandations': self.generer_recommandations()
        }
        
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(rapport, f, ensure_ascii=False, indent=2)
        
        print(f"✅ Rapport complet généré: {output_file}")
        
        return rapport
    
    def analyser_accessibilite_osm(self):
        """Analyser l'accessibilité urbaine via OpenStreetMap (si disponible)"""
        if not GEOSPATIAL_AVAILABLE:
            print("⚠️ Analyse OSM non disponible. Installer osmnx: pip install osmnx")
            return None
        
        try:
            # Télécharger le réseau de rues d'Agadir
            print("📥 Téléchargement des données OpenStreetMap pour Agadir...")
            G = ox.graph_from_place(self.city_name, network_type='all')
            
            # Statistiques du réseau
            stats = ox.basic_stats(G)
            
            print(f"✅ Réseau téléchargé: {stats['n']} nœuds, {stats['m']} arêtes")
            
            # Points d'intérêt genrés
            tags_genre = {
                'amenity': ['school', 'kindergarten', 'hospital', 'clinic', 
                           'community_centre', 'social_facility'],
                'leisure': ['park', 'playground', 'sports_centre'],
                'shop': ['convenience', 'supermarket']
            }
            
            pois = ox.features_from_place(self.city_name, tags=tags_genre)
            
            print(f"✅ {len(pois)} points d'intérêt identifiés")
            
            return {
                'graph': G,
                'stats': stats,
                'pois': pois
            }
            
        except Exception as e:
            print(f"❌ Erreur lors de l'analyse OSM: {str(e)}")
            return None
    
    def afficher_resume_console(self):
        """Afficher un résumé dans la console"""
        stats = self.generer_statistiques_globales()
        classification = self.analyser_budget_par_classification()
        zones = self.identifier_zones_prioritaires()
        
        print("\n" + "="*80)
        print("🏛️  RAPPORT D'ANALYSE BUDGÉTAIRE GENRÉE - VILLE D'AGADIR 2025")
        print("="*80)
        
        print("\n📊 STATISTIQUES GLOBALES")
        print(f"   Population totale: {stats['population']:,} habitants")
        print(f"   - Femmes: {stats['population_femmes']:,} (51%)")
        print(f"   - Hommes: {stats['population_hommes']:,} (49%)")
        print(f"   Budget total: {stats['budget_total']:,} Millions DH")
        print(f"   Budget genre-sensible: {stats['budget_genre_sensible']:.1f} M DH ({stats['pct_budget_genre']}%)")
        print(f"   Score moyen genre: {stats['score_moyen_genre']}/10")
        
        print("\n💰 RÉPARTITION PAR CLASSIFICATION")
        for _, row in classification.iterrows():
            print(f"   {row['Classification']:20} {row['Budget_MDH']:6.0f} M DH ({row['Pct_Total']:5.1f}%)")
        
        print("\n🏘️  ZONES PRIORITAIRES")
        for _, zone in zones.head(3).iterrows():
            print(f"   {zone['Quartier']:20} Score: {zone['Score_Genre']}/10 - {zone['Priorite']}")
        
        print("\n💡 RECOMMANDATIONS")
        recommandations = self.generer_recommandations()
        print(f"   Budget total recommandé: {recommandations['budget_total_recommande']} Millions DH")
        print(f"   Nombre d'actions immédiates: {len(recommandations['immediates'])}")
        print(f"   Projets moyen terme: {len(recommandations['moyen_terme'])}")
        
        print("\n" + "="*80 + "\n")


def main():
    """Fonction principale"""
    print("🚀 Lancement de l'Analyse Budgétaire Genrée - Agadir\n")
    
    # Créer l'analyseur
    analyzer = AgadirBudgetGenreAnalyzer()
    
    # Afficher le résumé
    analyzer.afficher_resume_console()
    
    # Générer les visualisations
    print("📊 Génération des visualisations...")
    
    # Budget par secteur
    fig_budget = analyzer.visualiser_budget_par_secteur()
    fig_budget.write_html('/home/claude/agadir_budget_secteurs.html')
    print("✅ Graphique budget par secteur créé")
    
    # Évolution indicateurs
    fig_indicateurs = analyzer.visualiser_evolution_indicateurs()
    fig_indicateurs.write_html('/home/claude/agadir_evolution_indicateurs.html')
    print("✅ Graphique évolution indicateurs créé")
    
    # Carte interactive
    analyzer.creer_carte_interactive('/home/claude/agadir_carte_genre.html')
    
    # Générer le rapport complet
    rapport = analyzer.generer_rapport_complet('/home/claude/rapport_agadir_2025.json')
    
    # Analyse OSM (optionnelle)
    print("\n🗺️  Tentative d'analyse géospatiale OSM...")
    osm_data = analyzer.analyser_accessibilite_osm()
    
    print("\n✅ Analyse complète terminée!")
    print("\n📁 Fichiers générés:")
    print("   - agadir_budget_secteurs.html")
    print("   - agadir_evolution_indicateurs.html")
    print("   - agadir_carte_genre.html")
    print("   - rapport_agadir_2025.json")
    print("\n🎯 Consultez ces fichiers pour une analyse détaillée\n")


if __name__ == "__main__":
    main()
