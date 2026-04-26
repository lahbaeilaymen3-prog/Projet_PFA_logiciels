import csv
import os
import matplotlib.pyplot as plt

nom_fichier = input("Entrez le nom du fichier CSV à analyser (appuyez sur Entrée pour utiliser ventes.csv) : ").strip()

if nom_fichier == "":
    nom_fichier = "ventes.csv"

colonnes_obligatoires = ["ID", "Prix", "Quantite", "Remise"]

# Question 1 : Générer ventes.csv
if not os.path.exists(nom_fichier):
    if nom_fichier == "ventes.csv":
        with open(nom_fichier, mode="w", newline="", encoding="utf-8") as fichier:
            ecrivain = csv.writer(fichier)
            ecrivain.writerow(colonnes_obligatoires)

        print("Le fichier ventes.csv a été créé avec l'en-tête demandé.")
        print("Remplissez maintenant le fichier puis relancez le programme.")
    else:
        print("Erreur : le fichier indiqué n'existe pas.")

else:
    with open(nom_fichier, mode="r", newline="", encoding="utf-8") as fichier:
        lecteur = csv.DictReader(fichier)

        if lecteur.fieldnames is None:
            print("Erreur : le fichier CSV est vide.")

        elif any(colonne not in lecteur.fieldnames for colonne in colonnes_obligatoires):
            print("Erreur : le fichier CSV ne contient pas les colonnes obligatoires : ID, Prix, Quantite, Remise")

        else:
            ca_total = 0
            meilleur_id = ""
            meilleur_ca_net = 0
            resultats = []
            ids = []
            ca_nets = []
            nombre_produits = 0

            # Bonus : Lecture dynamique
            for ligne in lecteur:
                id_produit = ligne["ID"]
                prix = float(ligne["Prix"])
                quantite = int(ligne["Quantite"])
                remise = float(ligne["Remise"])

                # Question 2 : Calcul du CA brut
                ca_brut = prix * quantite

                # Question 3 : Calcul du CA net
                ca_net = ca_brut - (ca_brut * remise / 100)

                # Question 4 : Calcul de la TVA
                tva = ca_net * 0.20

                # Question 5 : Calcul du CA total
                ca_total += ca_net
                nombre_produits += 1

                # Question 6 : Produit avec le plus gros bénéfice
                if ca_net > meilleur_ca_net:
                    meilleur_ca_net = ca_net
                    meilleur_id = id_produit

                ids.append(id_produit)
                ca_nets.append(ca_net)

                # Question 7 : Préparer resultats_final.csv
                resultats.append({
                    "ID": id_produit,
                    "Prix": prix,
                    "Quantite": quantite,
                    "Remise": remise,
                    "CA_Brut": round(ca_brut, 2),
                    "CA_Net": round(ca_net, 2),
                    "TVA": round(tva, 2)
                })

            if nombre_produits == 0:
                print("Le fichier ne contient aucune donnée à traiter.")
            else:
                print("Nombre de produits traités :", nombre_produits)
                print("CA Total de l'entreprise :", round(ca_total, 2))
                print("ID du produit avec le plus gros bénéfice :", meilleur_id)

                # Question 7 : Export des résultats
                with open("resultats_final.csv", mode="w", newline="", encoding="utf-8") as fichier_resultat:
                    champs = ["ID", "Prix", "Quantite", "Remise", "CA_Brut", "CA_Net", "TVA"]
                    ecrivain = csv.DictWriter(fichier_resultat, fieldnames=champs)

                    ecrivain.writeheader()
                    ecrivain.writerows(resultats)

                print("Le fichier resultats_final.csv a été créé avec succès.")

                # Bonus : Graphique Matplotlib
                plt.bar(ids, ca_nets, color="skyblue")
                plt.title("CA Net par produit")
                plt.xlabel("ID du produit")
                plt.ylabel("CA Net")
                plt.xticks(rotation=90)
                plt.show()