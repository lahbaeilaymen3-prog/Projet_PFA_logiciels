# Projet de Fin d’Année — Automatisation des Ventes

Ce projet Python automatise l’analyse des ventes à partir d’un fichier CSV, conformément au sujet du PFA [file:1].

## Objectif

Le programme permet de :

- générer le fichier `ventes.csv` avec l’en-tête `ID,Prix,Quantite,Remise` [file:1]
- lire un fichier CSV existant ou utiliser `ventes.csv` par défaut [file:1]
- calculer le chiffre d’affaires brut (`CA_Brut = Prix × Quantite`) [file:1]
- appliquer la remise pour obtenir le chiffre d’affaires net (`CA_Net`) [file:1]
- calculer la TVA de 20 % sur le CA net [file:1]
- afficher le CA total de l’entreprise [file:1]
- identifier l’ID du produit ayant généré le plus gros bénéfice [file:1]
- exporter les résultats dans `resultats_final.csv` [file:1]
- afficher un graphique simple avec Matplotlib pour visualiser le CA par produit [file:1]

## Fichiers du projet

- `main.py` : script principal pour créer `ventes.csv` si nécessaire, analyser les ventes, exporter `resultats_final.csv` et afficher le graphique.
- `generer_ventes.py` : script optionnel pour générer automatiquement un grand nombre de produits dans `ventes.csv`.
- `ventes.csv` : fichier d’entrée contenant les ventes.
- `resultats_final.csv` : fichier de sortie contenant les colonnes d’origine et les colonnes calculées.

## Structure de `ventes.csv`

Le fichier `ventes.csv` doit contenir l’en-tête suivant :

```csv
ID,Prix,Quantite,Remise
```

Exemple de contenu :

```csv
ID,Prix,Quantite,Remise
101,15.0,3,10
102,25.0,2,5
103,10.0,5,0
```

Ces valeurs correspondent à l’exemple donné dans le sujet [file:1].

## Utilisation

### 1. Créer automatiquement `ventes.csv`

Lancer :

```bash
python3 main.py
```

Si `ventes.csv` n’existe pas, le programme le crée automatiquement avec l’en-tête demandé [file:1].

### 2. Remplir `ventes.csv`

Deux possibilités :

- remplir le fichier manuellement
- ou utiliser `generer_ventes.py` pour générer beaucoup de produits automatiquement

### 3. Générer plusieurs produits automatiquement

Lancer :

```bash
python3 generer_ventes.py
```

Puis entrer par exemple :

```bash
1000
```

Le script crée alors un fichier `ventes.csv` avec 1000 produits.

### 4. Analyser les ventes

Lancer ensuite :

```bash
python3 main.py
```

Le programme peut :

- utiliser `ventes.csv` par défaut
- ou analyser un autre fichier CSV existant saisi par l’utilisateur

### 5. Résultats obtenus

Le programme affiche :

- le nombre de produits traités
- le CA total de l’entreprise [file:1]
- l’ID du produit avec le plus gros bénéfice [file:1]

Il génère aussi :

- `resultats_final.csv` [file:1]
- un graphique Matplotlib du CA Net par produit [file:1]

## Bonus réalisés

- graphique simple avec Matplotlib pour visualiser le CA par produit [file:1]
- lecture dynamique de fichiers CSV de tailles différentes [file:1]
- possibilité d’analyser un fichier CSV existant fourni par l’utilisateur
- possibilité de générer un grand nombre de produits automatiquement


## Bibliothèques utilisées

Ce projet Python utilise les bibliothèques suivantes :

- `csv` : pour lire et écrire les fichiers CSV
- `os` : pour vérifier l'existence des fichiers et gérer certains chemins
- `random` : pour générer des données de ventes aléatoires
- `matplotlib.pyplot` : pour afficher un graphique du chiffre d'affaires par produit

## Prérequis

Avant d'exécuter le projet, il faut avoir :

- Python 3 installé
- la bibliothèque `matplotlib` installée

## Installation

Installez la bibliothèque nécessaire avec la commande suivante :

```bash
pip install matplotlib
```

## Exécution

Lancez le projet avec :

```bash
python main.py
```

## Fichiers du projet

- `main.py` : programme principal
- `generer_ventes.py` : génération automatique du fichier `ventes.csv`
- `ventes.csv` : fichier source des ventes
- `resultats_final.csv` : fichier de sortie contenant les résultats calculés
- `README.md` : documentation du projet
- `.gitignore` : fichiers ignorés par Git

## Auteur

Projet réalisé par Aymen Lahbaeil , Slim Hableni et Ahmed Dridi.
