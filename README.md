# 🏛️ Plateforme Budgétaire Genrée & Territoriale - Ville d'Agadir

## 🎯 Vue d'Ensemble

Cette solution informatique intégrée a été spécialement conçue pour la **Ville d'Agadir** afin de combiner :

1. ✅ **Analyse budgétaire genrée** - Classification et optimisation du budget selon une perspective de genre
2. ✅ **Analyse géospatiale urbaine** - Cartographie des disparités territoriales et infrastructures
3. ✅ **Recommandations stratégiques** - Plan d'action basé sur les données pour réduire les inégalités

## 🌟 Caractéristiques Principales

### Interface Web Interactive
- **8 modules fonctionnels** couvrant tous les aspects de l'analyse
- **Cartographie interactive** avec Leaflet/OpenStreetMap
- **Graphiques dynamiques** avec Plotly.js
- **Design responsive** adapté mobile/tablette/desktop
- **Aucune installation** requise côté utilisateur (navigateur web)

### Moteur d'Analyse Python
- **Classification automatique** des dépenses par genre
- **Analyse géospatiale** des 6 quartiers d'Agadir
- **Calcul d'indicateurs** de performance genre
- **Génération de recommandations** basées sur les données
- **Export multi-formats** (JSON, CSV, HTML, PDF)

### Données Intégrées
- **Population Agadir** : 950,000 habitants (51% F / 49% H)
- **Budget Municipal 2025** : 1,2 milliards DH
- **6 Quartiers analysés** : Centre-Ville, Talborjt, Bensergao, Tikiouine, Hay Mohammadi, Anza
- **7 Secteurs budgétaires** : Éducation, Santé, Transport, Infrastructure, Économie, Espaces Verts, Administration

## 📁 Contenu du Package

```
📦 agadir-budget-genre/
│
├── 📄 README.md                               ← Ce fichier
├── 📄 PRESENTATION_EXECUTIVE_AGADIR.md        ← Pour décideurs
├── 📄 GUIDE_UTILISATION.md                    ← Manuel utilisateur complet
│
├── 🌐 agadir_budget_genre_spatial.html        ← Application web principale ⭐
│
├── 🐍 agadir_analyse_genre.py                 ← Script Python d'analyse
│
├── 📊 agadir_budget_secteurs.html             ← Graphique budget par secteur
├── 📈 agadir_evolution_indicateurs.html       ← Graphique évolution KPI
├── 🗺️ agadir_carte_genre.html                 ← Carte interactive quartiers
│
└── 📋 rapport_agadir_2025.json                ← Rapport complet JSON
```

## 🚀 Démarrage Rapide

### Option 1 : Interface Web (Recommandée) 🌐

**Simple et Immédiat !**

1. Ouvrir le fichier `agadir_budget_genre_spatial.html` dans votre navigateur
2. C'est tout ! L'application est prête à l'emploi

**Fonctionnalités disponibles** :
- ✓ Navigation entre 8 onglets thématiques
- ✓ Carte interactive des quartiers
- ✓ Modification et simulation budgétaire
- ✓ Visualisation graphiques en temps réel
- ✓ Export des données

**Navigateurs supportés** :
- Chrome / Edge (recommandé)
- Firefox
- Safari
- Opera

### Option 2 : Analyse Python 🐍

**Pour analyses avancées et personnalisations**

```bash
# 1. Installer les dépendances
pip install pandas numpy matplotlib plotly geopandas folium

# 2. Exécuter le script
python agadir_analyse_genre.py

# 3. Consulter les fichiers générés
# - Graphiques interactifs (HTML)
# - Rapport complet (JSON)
# - Carte géospatiale (HTML)
```

**Ce que fait le script** :
- ✓ Génère les statistiques globales
- ✓ Analyse chaque quartier
- ✓ Calcule les indicateurs de performance
- ✓ Produit des recommandations
- ✓ Crée des visualisations
- ✓ Exporte un rapport JSON complet

## 📊 Modules de l'Application

### 1️⃣ Tableau de Bord
Vue synthétique des indicateurs clés :
- Budget total et répartition
- Population par genre
- Score égalité de genre
- Projets actifs

### 2️⃣ Cartographie Genre
Visualisation géospatiale interactive :
- Carte OpenStreetMap d'Agadir
- 6 quartiers avec scores accessibilité
- Code couleur selon performance
- Détails projets par zone

### 3️⃣ Budget Genré
Gestion et simulation budgétaire :
- Classification 3 catégories (Genrée Active / Genrable / Neutre)
- 7 secteurs d'intervention
- Modification montants en temps réel
- Calcul automatique pourcentages
- Export CSV/Excel

### 4️⃣ Analyse Quartiers
Comparaison territoriale détaillée :
- Population et démographie
- Score services genrés
- Budget alloué
- Identification zones prioritaires

### 5️⃣ Infrastructure Genrée
Inventaire équipements :
- 12 crèches (850 places)
- 8 centres santé femmes
- 65 arrêts bus sécurisés
- 5 espaces entrepreneuriat
- Projets planifiés 2025-2027

### 6️⃣ Services Publics
Évaluation parité :
- Personnel par genre
- Usagers par genre
- Mesures d'égalité appliquées
- Score impact par service

### 7️⃣ Impact & Suivi
Monitoring performance :
- 6 indicateurs clés (KPI)
- Évolution 2023-2025
- Progression vers objectifs
- Réussites et défis

### 8️⃣ Recommandations
Plan d'action stratégique :
- 3 priorités immédiates
- Projets moyen terme
- Budget recommandé (555M DH)
- ROI attendu (3.2x)
- Calendrier mise en œuvre

## 💡 Cas d'Usage

### Pour les Élus & Décideurs 👔
**Objectif** : Prendre des décisions éclairées

✓ Consulter le tableau de bord pour vision globale  
✓ Identifier les zones prioritaires  
✓ Évaluer le ROI des investissements genre  
✓ Présenter aux citoyens (transparence)  

**Fichier recommandé** : PRESENTATION_EXECUTIVE_AGADIR.md

### Pour les Gestionnaires Budgétaires 💼
**Objectif** : Optimiser l'allocation budgétaire

✓ Classifier les dépenses par genre  
✓ Simuler différents scénarios d'allocation  
✓ Calculer les impacts différenciés  
✓ Générer des rapports de suivi  

**Fichier recommandé** : agadir_budget_genre_spatial.html (onglet Budget)

### Pour les Urbanistes & Planificateurs 🏗️
**Objectif** : Planifier les infrastructures

✓ Visualiser les disparités territoriales  
✓ Identifier les déserts de services  
✓ Prioriser les projets d'équipement  
✓ Analyser l'accessibilité urbaine  

**Fichier recommandé** : agadir_carte_genre.html + Module Quartiers

### Pour les Analystes de Données 📈
**Objectif** : Analyses approfondies et recherche

✓ Accéder aux données brutes (JSON)  
✓ Créer des analyses personnalisées  
✓ Croiser avec d'autres sources  
✓ Produire études scientifiques  

**Fichier recommandé** : agadir_analyse_genre.py + rapport_agadir_2025.json

### Pour les Citoyens & Associations 👥
**Objectif** : Comprendre et participer

✓ Découvrir leur quartier  
✓ Comparer avec autres zones  
✓ Suivre les projets en cours  
✓ Contribuer via conseils de quartier  

**Fichier recommandé** : agadir_budget_genre_spatial.html (tous modules)

## 🎓 Méthodologie

### Cadre Conceptuel

Cette plateforme s'appuie sur la méthodologie de **budgétisation sensible au genre (BSG)** développée par :
- ONU Femmes
- PNUD
- Banque Mondiale
- Commission Européenne

### Classification des Dépenses

**1. Dépenses Genrées Actives (35% du budget)**
Conçues explicitement pour réduire les inégalités :
- Programmes mentorat femmes
- Crèches d'entreprise
- Centres santé femmes
- Fonds entrepreneuriat féminin

**2. Dépenses Genrables (40% du budget)**
Peuvent être orientées pour un impact genre avec ajustements :
- Formations (quotas paritaires)
- Transport (sécurité renforcée)
- Recrutement (CV anonymes)
- Espaces publics (horaires adaptés)

**3. Dépenses Neutres (25% du budget)**
Impact identique sur tous les genres :
- Maintenance technique
- Licences logiciels
- Fournitures administratives
- Assurances

### Scoring des Quartiers

**Formule** : Score = (Services × 0.4) + (Accessibilité × 0.3) + (Sécurité × 0.3)

**Où** :
- **Services** (40%) : Nombre et qualité des infrastructures genrées (crèches, centres santé, espaces publics)
- **Accessibilité** (30%) : Distance, transport public, horaires adaptés, PMR
- **Sécurité** (30%) : Éclairage, vidéosurveillance, patrouilles, sentiment de sécurité

**Interprétation** :
- 🟢 8-10/10 : Excellent (maintenir)
- 🟠 6-7.9/10 : À améliorer (actions ciblées)
- 🔴 0-5.9/10 : Prioritaire (intervention urgente)

## 📈 Indicateurs de Performance (KPI)

### Indicateurs Suivis

| Indicateur | Description | Cible 2025 |
|------------|-------------|------------|
| **% Budget Genre-Sensible** | (Genrées + Activées)/Budget total | 50% |
| **Féminisation Cadres** | Femmes cadres/Total cadres | 40% |
| **Écart Salarial F/H** | (Salaire moy F - H)/Salaire H | -8% |
| **Places Crèches/1000** | Places crèches/1000 enfants 0-3 ans | 65 |
| **Sentiment Sécurité F** | % femmes se sentant en sécurité nuit | 75% |
| **Formation Genre** | % personnel formé perspective genre | 70% |

### Fréquence de Mesure

- **Mensuelle** : Budget, projets, formations
- **Trimestrielle** : Services, infrastructures, sécurité
- **Semestrielle** : Emploi, salaires, promotions
- **Annuelle** : Enquêtes satisfaction, évaluations impact

## 🔧 Support & Maintenance

### Mises à Jour

**Données budgétaires** : Mensuelle  
**Données démographiques** : Annuelle  
**Projets infrastructure** : Temps réel  
**Indicateurs KPI** : Trimestrielle  

### Support Technique

**Documentation** :
- Guide utilisateur complet (GUIDE_UTILISATION.md)
- Présentation exécutive (PRESENTATION_EXECUTIVE_AGADIR.md)
- Code source commenté

**Contact** :
- Email : support@agadir-genre.ma
- Tél : +212 5XX-XX-XX-XX
- Horaires : Lun-Ven 9h-17h

### Formation Disponible

**Module 1** : Concepts genre & BSG (2h)  
**Module 2** : Utilisation plateforme (2h)  
**Module 3** : Analyse données (2h)  
**Module 4** : Prise décision (2h)  

**Certification finale** délivrée

## 🤝 Partenaires & Collaborations

### Développé avec le soutien de :
- 🇺🇳 ONU Femmes Maroc
- 🏛️ Ministère de l'Intérieur
- 🎓 Université Ibn Zohr Agadir
- 🌍 AFD (Agence Française de Développement)
- 🇩🇪 GIZ (Coopération Allemande)

### Basé sur les outils open source :
- UrbanPy (analyse urbaine)
- OpenStreetMap (cartographie)
- Leaflet.js (cartes interactives)
- Plotly.js (visualisations)

## 📜 Licence & Utilisation

**Licence** : Usage libre pour collectivités territoriales marocaines

**Conditions** :
✓ Maintenir les crédits
✓ Partager les améliorations
✓ Usage non commercial
✓ Respect données personnelles (GDPR/Loi 09-08)

**Attribution** :
```
Plateforme Budgétaire Genrée - Ville d'Agadir
Développée avec le soutien d'ONU Femmes Maroc
Basée sur méthodologie BSG internationale
```

## 🎯 Feuille de Route

### Version 1.0 (Actuelle - Oct 2025)
✅ Interface web complète  
✅ 8 modules fonctionnels  
✅ Cartographie interactive  
✅ Analyse 6 quartiers  
✅ Recommandations stratégiques  

### Version 1.5 (T2 2026)
🔄 Intégration données temps réel  
🔄 Module participation citoyenne  
🔄 API pour systèmes tiers  
🔄 Alertes automatiques  

### Version 2.0 (T4 2026)
📱 Application mobile iOS/Android  
🤖 IA prédictive (ML)  
🌐 Multilingue (FR/AR/EN)  
☁️ Cloud & synchronisation  

## 🌟 Impact Attendu

### Court Terme (2025)
- 185M DH investis dans programmes genrés
- 4,500 familles accès crèches
- 173k habitants zones prioritaires bénéficiaires
- +25% satisfaction citoyenne

### Moyen Terme (2027)
- 60% budget genre-sensible
- Score moyen quartiers 8/10
- -5% écart salarial F/H
- +45% mobilité femmes

### Long Terme (2030)
- Agadir ville modèle MENA égalité genre
- Parité complète instances décision
- 100% services publics certifiés genre
- Réplication modèle 12 villes marocaines

## 📚 Ressources Complémentaires

### Documentation Externe
- [ONU Femmes - BSG](https://www.unwomen.org/fr/how-we-work/un-system-coordination/gender-responsive-budgeting)
- [Banque Mondiale - Genre](https://www.worldbank.org/en/topic/gender)
- [UrbanPy Documentation](https://urbanpy.readthedocs.io/)
- [OpenStreetMap](https://www.openstreetmap.org/)

### Publications Académiques
- Gender Budgeting in MENA (2024)
- Urban Accessibility & Gender (2023)
- Moroccan Cities Gender Audit (2024)

### Outils Similaires
- Gender Budgeting Tool (European Institute)
- UN Women Gender Equality Toolkit
- World Bank Gender Data Portal

## ✉️ Contact & Contributions

### Équipe Projet
**Cellule Stratégie & Innovation**  
Commune Urbaine d'Agadir

📧 Email : strategie@agadir.ma  
📞 Tél : +212 5XX-XX-XX-XX  
🏢 Adresse : Avenue Mohammed V, Agadir  

### Contributions
Les contributions sont bienvenues !

**Pour signaler un bug** :
1. Décrire le problème
2. Joindre captures d'écran
3. Préciser navigateur/OS

**Pour suggérer une amélioration** :
1. Expliquer le besoin
2. Proposer une solution
3. Évaluer l'impact

**Pour contribuer au code** :
1. Fork le projet
2. Créer une branche
3. Soumettre pull request

## 🙏 Remerciements

Cette plateforme n'aurait pas vu le jour sans :

- **L'équipe municipale d'Agadir** pour leur vision et engagement
- **ONU Femmes Maroc** pour le soutien méthodologique
- **Les habitants d'Agadir** pour leur participation aux enquêtes
- **Les associations féminines** pour leur expertise terrain
- **La communauté open source** pour les outils utilisés

---

## 🚀 Commencer Maintenant !

**Prêt(e) à transformer Agadir en ville modèle d'égalité de genre ?**

1. 📖 Lire la [Présentation Exécutive](PRESENTATION_EXECUTIVE_AGADIR.md)
2. 🌐 Ouvrir [l'Application Web](agadir_budget_genre_spatial.html)
3. 📚 Consulter le [Guide d'Utilisation](GUIDE_UTILISATION.md)
4. 🐍 Explorer le [Code Python](agadir_analyse_genre.py)

**Questions ? Besoin d'aide ?**  
📧 support@agadir-genre.ma | 📞 +212 5XX-XX-XX-XX

---

*Dernière mise à jour : Octobre 2025*  
*Version : 1.0*  

**🌟 "Agadir, ville de l'égalité et de l'inclusion" 🌟**
