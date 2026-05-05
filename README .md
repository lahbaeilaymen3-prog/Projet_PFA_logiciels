# Projet de Fin d'Année — Automatisation des Ventes

**Matière :** Logiciels  
**Auteurs :** Aymen Lahbaeil, Slim Hableni, Ahmed Dridi

---

## Contexte

Une entreprise de e-commerce utilise un fichier Excel pour suivre ses ventes. Le volume de données devient trop important pour un tableur classique. Ce projet Python automatise l'analyse des ventes à partir d'un fichier CSV, conformément au sujet du PFA.

---

## Objectif

Le programme permet de :

- Créer `ventes.csv` avec les données d'exemple du sujet (`ID,Prix,Quantite,Remise`)
- Générer `ventes.csv` automatiquement avec un grand nombre de produits aléatoires
- Lire dynamiquement n'importe quel fichier CSV existant
- Calculer le **Chiffre d'Affaires Brut** : `CA_Brut = Prix × Quantite`
- Appliquer la remise pour obtenir le **CA Net** : `CA_Net = CA_Brut × (1 - Remise / 100)`
- Calculer la **TVA (20%)** sur le CA Net : `TVA = CA_Net × 0.20`
- Afficher le **CA Total** de l'entreprise
- Identifier l'**ID du produit** ayant généré le plus gros CA Net
- Exporter les résultats dans `resultats_final.csv`
- Générer deux graphiques Matplotlib sauvegardés en PNG

---

## Fichiers du projet

| Fichier | Description |
|---|---|
| `main.py` | Script unique : menu principal, création CSV, génération aléatoire, analyse, graphiques |
| `ventes.csv` | Fichier d'entrée des ventes (créé via le menu) |
| `resultats_final.csv` | Fichier de sortie avec les colonnes calculées (CA_Brut, CA_Net, TVA) |
| `README.md` | Documentation du projet |
| `.gitignore` | Fichiers ignorés par Git |

> ℹ️ Ce projet ne contient qu'un seul fichier Python (`main.py`). Les fonctionnalités de génération aléatoire sont intégrées directement dans le menu.

---

## Structure de `ventes.csv`

```csv
ID,Prix,Quantite,Remise
101,15.0,3,10
102,25.0,2,5
103,10.0,5,0
```

## Structure de `resultats_final.csv` (sortie)

```
ID, Prix, Quantite, Remise, CA_Brut, CA_Net, TVA
```

---

## Utilisation

### Lancer le programme

```bash
python main.py
```

Un menu s'affiche à chaque lancement :

```
==================================================
   🛒  Automatisation des Ventes
==================================================
  1. Créer ventes.csv avec les données d'exemple
  2. Générer ventes.csv avec des données aléatoires
  3. Analyser un fichier CSV existant
  0. Quitter
==================================================
Votre choix :
```

---

### Option 1 — Créer `ventes.csv` avec les données d'exemple

Crée `ventes.csv` avec les 3 lignes d'exemple du sujet (ID 101, 102, 103).  
Si le fichier existe déjà, le programme demande une confirmation avant de le remplacer :

```
⚠️  Le fichier ventes.csv existe déjà. Voulez-vous le remplacer ? (o/n) :
```

Une fois créé, remplissez le fichier manuellement puis passez à l'**option 3** pour l'analyser.

---

### Option 2 — Générer `ventes.csv` avec des données aléatoires

Génère `ventes.csv` avec un nombre de produits saisi par l'utilisateur :

```
Entrez le nombre de produits à générer :
```

Chaque produit est généré avec :
- un prix aléatoire entre 5 € et 500 €
- une quantité aléatoire entre 1 et 20
- une remise parmi : 0, 5, 10, 15, 20 ou 25 %

---

### Option 3 — Analyser un fichier CSV existant

Le programme demande le nom du fichier à analyser :

```
Entrez le nom du fichier CSV à analyser (appuyez sur Entrée pour utiliser ventes.csv) :
```

- Appuyez sur **Entrée** pour utiliser `ventes.csv` par défaut
- Ou saisissez le nom d'un autre fichier CSV

#### Résultats affichés dans le terminal

```
==================================================
  📦 Nombre de produits traités : 1000
  💰 CA Total de l'entreprise   : 2 845 123,45 EUR
  🏆 Produit le plus rentable   : ID 247  (9 870,00 EUR CA Net)
==================================================
```

#### Fichier exporté

```
✅ Fichier 'resultats_final.csv' créé avec succès (1000 lignes).
```

#### Graphiques générés et sauvegardés

Le programme génère automatiquement deux graphiques PNG dans le dossier du projet :

**Graphique 1 — Barres horizontales** (`graphique_barres.png`)  
CA Net par produit, classé par ordre décroissant. Si le nombre de produits dépasse 30, plusieurs pages sont créées (`graphique_barres_page1.png`, `graphique_barres_page2.png`, etc.). Le meilleur produit est mis en valeur en orange.

**Graphique 2 — Camembert** (`graphique_camembert.png`)  
Répartition du CA Net entre les produits. Au-delà du top 9, les produits restants sont regroupés sous « Autres ». Le meilleur produit est mis en valeur (part décalée).

---

## Bonus réalisés

- ✅ Graphiques Matplotlib : barres horizontales paginées + camembert de répartition
- ✅ Sauvegarde des graphiques en PNG avant affichage (ordre correct)
- ✅ Lecture dynamique de fichiers CSV de tailles différentes
- ✅ Gestion des lignes invalides (avertissement affiché, ligne ignorée)
- ✅ Génération aléatoire intégrée directement dans `main.py` (pas de fichier séparé)
- ✅ Confirmation avant écrasement d'un fichier existant (option 1)

---

## Bibliothèques utilisées

| Bibliothèque | Usage |
|---|---|
| `csv` | Lecture et écriture des fichiers CSV |
| `os` | Gestion des chemins de fichiers |
| `random` | Génération aléatoire des données (option 2) |
| `matplotlib.pyplot` | Affichage et sauvegarde des graphiques |
| `matplotlib.ticker` | Formatage des axes (valeurs en euros) |
| `matplotlib.patches` | Légendes colorées des graphiques |

---

## Environnement requis

### 1. Logiciels à installer

| Logiciel | Lien de téléchargement |
|---|---|
| Python 3 | [python.org/downloads](https://www.python.org/downloads/) |
| VS Code | [code.visualstudio.com](https://code.visualstudio.com/) |

> ⚠️ Lors de l'installation de Python, cochez **"Add Python to PATH"**.

### 2. Extension VS Code

Dans VS Code, installer l'extension **Python** (by Microsoft) via le panneau Extensions (`Ctrl+Shift+X`).

### 3. Installer la dépendance Python

```bash
pip install matplotlib
```

### 4. Vérifier l'installation

```bash
python --version
pip --version
```

Si les deux commandes affichent un numéro de version, l'environnement est prêt. ✅

---

## Exécution

```bash
python main.py
```