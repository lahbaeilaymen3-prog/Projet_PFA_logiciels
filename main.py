import csv
import os
import random
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import matplotlib.patches as mpatches


# -------------------------------------------------------
# Configuration globale du style des graphiques
# -------------------------------------------------------
plt.rcParams.update({
    "figure.facecolor":  "#F8F9FA",
    "axes.facecolor":    "#FFFFFF",
    "axes.edgecolor":    "#CCCCCC",
    "axes.grid":         True,
    "grid.color":        "#E0E0E0",
    "grid.linestyle":    "--",
    "grid.alpha":        0.6,
    "font.family":       "DejaVu Sans",
    "axes.titlesize":    13,
    "axes.titleweight":  "bold",
    "axes.labelsize":    10,
    "xtick.labelsize":   8,
    "ytick.labelsize":   8,
})

COULEUR_PRINCIPALE = "#4C72B0"
COULEUR_MEILLEUR   = "#E05C2A"
COULEUR_FOND_TITRE = "#2C3E50"
PALETTE_CAMEMBERT  = [
    "#4C72B0", "#DD8452", "#55A868", "#C44E52", "#8172B2",
    "#937860", "#DA8BC3", "#8C8C8C", "#CCB974", "#64B5CD",
]


# -------------------------------------------------------
# Fonctions graphiques
# -------------------------------------------------------

def sauvegarder(fig, dossier, nom_fichier):
    """Sauvegarde une figure dans le dossier du script."""
    chemin = os.path.join(dossier, nom_fichier)
    fig.savefig(chemin, dpi=150, bbox_inches="tight", facecolor=fig.get_facecolor())
    print(f"   📸 Graphique sauvegardé : {nom_fichier}")


def tracer_barres(ids_page, ca_page, meilleur_id, num_page, nb_pages, dossier):
    """
    Bonus : Graphique 1 - Barres horizontales du CA Net par produit.
    Pagination automatique pour gérer un grand nombre de produits.
    """
    nb          = len(ids_page)
    hauteur_fig = max(6, nb * 0.48)
    fig, ax     = plt.subplots(figsize=(13, hauteur_fig), facecolor="#F8F9FA")

    couleurs = [COULEUR_MEILLEUR if id_p == meilleur_id else COULEUR_PRINCIPALE
                for id_p in ids_page]

    barres = ax.barh(ids_page, ca_page, color=couleurs,
                     edgecolor="white", height=0.62, zorder=3)

    valeur_max = max(ca_page) if ca_page else 1
    for barre, val, couleur in zip(barres, ca_page, couleurs):
        alpha = 0.55 + 0.45 * (val / valeur_max)
        barre.set_alpha(alpha)

    for barre, valeur in zip(barres, ca_page):
        ax.text(
            valeur + valeur_max * 0.012,
            barre.get_y() + barre.get_height() / 2,
            f"{valeur:,.2f} €",
            va="center", ha="left",
            fontsize=max(6, min(8, 220 // nb)),
            color="#333333", fontweight="bold",
        )

    suffixe = f"  -  Page {num_page}/{nb_pages}" if nb_pages > 1 else ""
    ax.set_title(f"CA Net par produit (classement décroissant){suffixe}",
                 pad=14, color=COULEUR_FOND_TITRE)
    ax.set_xlabel("CA Net (€)")
    ax.set_ylabel("ID Produit")

    taille_y = max(5, min(9, 200 // nb))
    ax.tick_params(axis="y", labelsize=taille_y)
    ax.xaxis.set_major_formatter(mticker.FuncFormatter(lambda v, _: f"{v:,.0f}"))

    legende = [
        mpatches.Patch(color=COULEUR_MEILLEUR,   label=f"Meilleur produit (ID {meilleur_id})"),
        mpatches.Patch(color=COULEUR_PRINCIPALE, label="Autres produits"),
    ]
    ax.legend(handles=legende, fontsize=8, loc="lower right",
              framealpha=0.9, edgecolor="#CCCCCC")

    ax.invert_yaxis()
    ax.set_xlim(0, valeur_max * 1.18)
    plt.tight_layout()

    nom = f"graphique_barres_page{num_page}.png" if nb_pages > 1 else "graphique_barres.png"
    sauvegarder(fig, dossier, nom)
    plt.show()
    plt.close(fig)


def tracer_camembert(ids_tries, ca_nets_tries, meilleur_id, dossier):
    """
    Bonus : Graphique 2 - Camembert de la répartition du CA Net.
    Si trop de produits, regroupe les petits sous 'Autres'.
    """
    MAX_PARTS = 10
    total     = sum(ca_nets_tries)

    if len(ids_tries) > MAX_PARTS:
        ids_affich = list(ids_tries[:MAX_PARTS - 1])
        ca_affich  = list(ca_nets_tries[:MAX_PARTS - 1])
        reste      = sum(ca_nets_tries[MAX_PARTS - 1:])
        ids_affich.append("Autres")
        ca_affich.append(reste)
    else:
        ids_affich = list(ids_tries)
        ca_affich  = list(ca_nets_tries)

    nb       = len(ids_affich)
    couleurs = (PALETTE_CAMEMBERT * ((nb // len(PALETTE_CAMEMBERT)) + 1))[:nb]

    explode = [0.07 if str(id_p) == str(meilleur_id) else 0 for id_p in ids_affich]

    fig, ax = plt.subplots(figsize=(10, 7), facecolor="#F8F9FA")

    wedges, texts, autotexts = ax.pie(
        ca_affich,
        labels=None,
        autopct=lambda pct: f"{pct:.1f}%\n({pct * total / 100:,.0f} EUR)" if pct >= 3 else "",
        colors=couleurs,
        explode=explode,
        startangle=140,
        pctdistance=0.78,
        wedgeprops={"edgecolor": "white", "linewidth": 1.8},
    )

    for at in autotexts:
        at.set_fontsize(7.5)
        at.set_color("#222222")

    legende_labels = [
        f"ID {id_p}  -  {ca:,.2f} EUR  ({ca / total * 100:.1f}%)"
        for id_p, ca in zip(ids_affich, ca_affich)
    ]
    ax.legend(wedges, legende_labels,
              title="Produits", title_fontsize=9,
              loc="center left", bbox_to_anchor=(1.02, 0.5),
              fontsize=8, framealpha=0.9, edgecolor="#CCCCCC")

    ax.set_title("Répartition du CA Net par produit",
                 pad=16, color=COULEUR_FOND_TITRE)

    plt.tight_layout()
    sauvegarder(fig, dossier, "graphique_camembert.png")
    plt.show()
    plt.close(fig)


# -------------------------------------------------------
# Option 1 : Créer ventes.csv avec les données d'exemple
# (Question 1 du sujet)
# -------------------------------------------------------

def creer_ventes_exemple(dossier_script):
    """Crée ventes.csv avec les 3 lignes d'exemple du sujet."""
    colonnes_obligatoires = ["ID", "Prix", "Quantite", "Remise"]
    chemin_fichier = os.path.join(dossier_script, "ventes.csv")

    if os.path.exists(chemin_fichier):
        confirmation = input(
            "⚠️  Le fichier ventes.csv existe déjà. Voulez-vous le remplacer ? (o/n) : "
        ).strip().lower()
        if confirmation != "o":
            print("❌ Opération annulée.")
            return

    with open(chemin_fichier, mode="w", newline="", encoding="utf-8") as fichier:
        ecrivain = csv.writer(fichier)
        ecrivain.writerow(colonnes_obligatoires)
        ecrivain.writerows([
            [101, 15.0, 3, 10],
            [102, 25.0, 2, 5],
            [103, 10.0, 5, 0],
        ])

    print("✅ Le fichier ventes.csv a été créé avec les données d'exemple.")
    print("   Remplissez-le puis choisissez l'option 3 pour analyser.\n")


# -------------------------------------------------------
# Option 2 : Générer ventes.csv avec des données aléatoires
# (fonctionnalité de generer_ventes.py)
# -------------------------------------------------------

def generer_ventes(dossier_script):
    """Génère ventes.csv avec un nombre de produits aléatoires saisi par l'utilisateur."""
    nombre_produits = int(input("Entrez le nombre de produits à générer : "))

    chemin = os.path.join(dossier_script, "ventes.csv")
    with open(chemin, mode="w", newline="", encoding="utf-8") as fichier:
        ecrivain = csv.writer(fichier)
        ecrivain.writerow(["ID", "Prix", "Quantite", "Remise"])
        for i in range(1, nombre_produits + 1):
            id_produit = 100 + i
            prix       = round(random.uniform(5, 500), 2)
            quantite   = random.randint(1, 20)
            remise     = random.choice([0, 5, 10, 15, 20, 25])
            ecrivain.writerow([id_produit, prix, quantite, remise])

    print(f"✅ Le fichier ventes.csv avec {nombre_produits} produits a été créé avec succès.\n")


# -------------------------------------------------------
# Option 3 : Analyser un fichier CSV existant
# -------------------------------------------------------

def analyser_ventes(dossier_script):
    """Lit un fichier CSV, calcule les indicateurs et génère les graphiques."""
    nom_fichier = input(
        "Entrez le nom du fichier CSV à analyser (appuyez sur Entrée pour utiliser ventes.csv) : "
    ).strip()

    if nom_fichier == "":
        nom_fichier = "ventes.csv"

    colonnes_obligatoires = ["ID", "Prix", "Quantite", "Remise"]
    chemin_fichier = os.path.join(dossier_script, nom_fichier)

    if not os.path.exists(chemin_fichier):
        print("❌ Erreur : le fichier indiqué n'existe pas.")
        print("   Utilisez l'option 1 ou 2 pour créer ventes.csv d'abord.")
        return

    # Lecture dynamique du fichier CSV (Bonus)
    with open(chemin_fichier, mode="r", newline="", encoding="utf-8") as fichier:
        lecteur = csv.DictReader(fichier, skipinitialspace=True)

        if lecteur.fieldnames is None:
            print("❌ Erreur : le fichier CSV est vide.")
            return

        if any(col not in lecteur.fieldnames for col in colonnes_obligatoires):
            print("❌ Erreur : colonnes obligatoires manquantes (ID, Prix, Quantite, Remise).")
            return

        ca_total        = 0.0
        meilleur_id     = ""
        meilleur_ca_net = 0.0
        resultats       = []
        nombre_produits = 0

        for ligne in lecteur:
            if not any(v and v.strip() for v in ligne.values()):
                continue

            try:
                id_produit = ligne["ID"].strip()
                prix       = float(ligne["Prix"].strip())
                quantite   = int(ligne["Quantite"].strip())
                remise     = float(ligne["Remise"].strip())
            except (ValueError, AttributeError, KeyError):
                print(f"⚠️  Ligne invalide ignorée : {ligne}")
                continue

            # ---------------------------------------------------
            # Question 2 : Calcul du Chiffre d'Affaires Brut
            # CA_Brut = Prix × Quantité
            # ---------------------------------------------------
            ca_brut = prix * quantite

            # ---------------------------------------------------
            # Question 3 : Application de la remise → CA Net
            # CA_Net = CA_Brut × (1 - Remise / 100)
            # ---------------------------------------------------
            ca_net = ca_brut * (1 - remise / 100)

            # ---------------------------------------------------
            # Question 4 : Calcul de la TVA (20%) sur le CA Net
            # ---------------------------------------------------
            tva = ca_net * 0.20

            # Accumulation pour le CA total (Question 5)
            ca_total += ca_net
            nombre_produits += 1

            # ---------------------------------------------------
            # Question 6 : Suivi du produit le plus rentable
            # ---------------------------------------------------
            if ca_net > meilleur_ca_net:
                meilleur_ca_net = ca_net
                meilleur_id     = id_produit

            resultats.append({
                "ID":       id_produit,
                "Prix":     prix,
                "Quantite": quantite,
                "Remise":   remise,
                "CA_Brut":  round(ca_brut, 2),
                "CA_Net":   round(ca_net,  2),
                "TVA":      round(tva,     2),
            })

    if nombre_produits == 0:
        print("⚠️  Le fichier ne contient aucune donnée à traiter.")
        return

    # -------------------------------------------------------
    # Question 5 : Affichage du CA Total de l'entreprise
    # -------------------------------------------------------
    print("\n" + "=" * 50)
    print(f"  📦 Nombre de produits traités : {nombre_produits}")
    print(f"  💰 CA Total de l'entreprise   : {round(ca_total, 2):,.2f} EUR")

    # -------------------------------------------------------
    # Question 6 : Affichage du produit le plus rentable
    # -------------------------------------------------------
    print(f"  🏆 Produit le plus rentable   : ID {meilleur_id}  ({round(meilleur_ca_net, 2):,.2f} EUR CA Net)")
    print("=" * 50 + "\n")

    # -------------------------------------------------------
    # Question 7 : Export dans resultats_final.csv
    # -------------------------------------------------------
    chemin_resultat = os.path.join(dossier_script, "resultats_final.csv")
    champs = ["ID", "Prix", "Quantite", "Remise", "CA_Brut", "CA_Net", "TVA"]

    with open(chemin_resultat, mode="w", newline="", encoding="utf-8") as fichier_resultat:
        ecrivain = csv.DictWriter(fichier_resultat, fieldnames=champs)
        ecrivain.writeheader()
        ecrivain.writerows(resultats)

    print(f"✅ Fichier 'resultats_final.csv' créé avec succès ({nombre_produits} lignes).\n")

    # -------------------------------------------------------
    # Bonus : Génération des deux graphiques + sauvegarde PNG
    # -------------------------------------------------------
    donnees_triees = sorted(
        zip([r["ID"] for r in resultats], [r["CA_Net"] for r in resultats]),
        key=lambda x: x[1],
        reverse=True,
    )
    ids_tries     = [d[0] for d in donnees_triees]
    ca_nets_tries = [d[1] for d in donnees_triees]

    print("📊 Génération des graphiques...\n")

    # --- Graphique 1 : Barres horizontales avec pagination ---
    PRODUITS_PAR_PAGE = 30
    pages = [
        (ids_tries[i:i + PRODUITS_PAR_PAGE], ca_nets_tries[i:i + PRODUITS_PAR_PAGE])
        for i in range(0, nombre_produits, PRODUITS_PAR_PAGE)
    ]
    nb_pages = len(pages)

    for num_page, (ids_page, ca_page) in enumerate(pages, start=1):
        tracer_barres(ids_page, ca_page, meilleur_id, num_page, nb_pages, dossier_script)

    # --- Graphique 2 : Camembert de répartition ---
    tracer_camembert(ids_tries, ca_nets_tries, meilleur_id, dossier_script)

    print("\n✅ Tous les graphiques ont été affichés et sauvegardés dans le dossier du projet.")


# -------------------------------------------------------
# Menu principal
# -------------------------------------------------------

def main():
    dossier_script = os.path.dirname(os.path.abspath(__file__))

    print("\n" + "=" * 50)
    print("   🛒  Automatisation des Ventes")
    print("=" * 50)
    print("  1. Créer ventes.csv avec les données d'exemple")
    print("  2. Générer ventes.csv avec des données aléatoires")
    print("  3. Analyser un fichier CSV existant")
    print("  0. Quitter")
    print("=" * 50)

    choix = input("Votre choix : ").strip()

    if choix == "1":
        creer_ventes_exemple(dossier_script)
    elif choix == "2":
        generer_ventes(dossier_script)
    elif choix == "3":
        analyser_ventes(dossier_script)
    elif choix == "0":
        print("Au revoir !")
    else:
        print("❌ Choix invalide. Veuillez entrer 1, 2, 3 ou 0.")


if __name__ == "__main__":
    main()