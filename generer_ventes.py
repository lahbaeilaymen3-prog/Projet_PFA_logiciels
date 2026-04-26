import csv
import random

nombre_produits = int(input("Entrez le nombre de produits à générer : "))

with open("ventes.csv", mode="w", newline="", encoding="utf-8") as fichier:
    ecrivain = csv.writer(fichier)
    ecrivain.writerow(["ID", "Prix", "Quantite", "Remise"])

    for i in range(1, nombre_produits + 1):
        id_produit = 100 + i
        prix = round(random.uniform(5, 500), 2)
        quantite = random.randint(1, 20)
        remise = random.choice([0, 5, 10, 15, 20, 25])

        ecrivain.writerow([id_produit, prix, quantite, remise])

print(f"Le fichier ventes.csv avec {nombre_produits} produits a été créé avec succès.")