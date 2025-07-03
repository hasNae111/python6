import os
import shutil

#challenge1
dossier = "C:\\Users\\AdMin\\Desktop\\challenge1"
texte_combine = ""
fichiers = os.listdir(dossier)
for fichier in fichiers:
    if fichier.endswith(".txt"):
        chemin = dossier + "/" + fichier
        with open(chemin, "r", encoding="utf-8") as f:
            contenu = f.read()
            texte_combine += contenu + "\n"

print("Texte combine de tous les fichiers :")
print(texte_combine)


#challenge2
dossier = "C:\\Users\\AdMin\\Desktop\\challenge1"
fichier_config = "config.yaml"
chemin_complet = dossier + "/" + fichier_config
if os.path.exists(chemin_complet):
    print("Le fichier config.yaml existe.")
    print("Contenu du fichier :")
    with open(chemin_complet, "r", encoding="utf-8") as f:
        contenu = f.read()
        print(contenu)
else:
    print("Le fichier config.yaml n'existe pas dans ce dossier.")

#challenge3
source = "C:\\Users\\AdMin\\Desktop\\challenge1"
destination = "C:\\Users\\AdMin\\Desktop\\challenge3"
if not os.path.exists(destination):
    os.makedirs(destination)
fichiers = os.listdir(source)
for fichier in fichiers:
    if fichier.endswith(".txt"):
        chemin_source = os.path.join(source, fichier)
        chemin_dest = os.path.join(destination, fichier)
        shutil.copy(chemin_source, chemin_dest)
        print(f"Copie : {fichier}")

print("Copie terminee.")

#challenge4
dossier_principal = "challenge4"
sous_dossiers = ["documents", "images", "scripts", "archives"]
if not os.path.exists(dossier_principal):
    os.mkdir(dossier_principal)
    print(f"Dossier cree : {dossier_principal}")
else:
    print(f"Dossier deja existant : {dossier_principal}")


for nom in sous_dossiers:
    chemin = os.path.join(dossier_principal, nom)
    if not os.path.exists(chemin):
        os.mkdir(chemin)
        print(f"Sous-dossier cree : {chemin}")
    else:
        print(f"Sous-dossier deja existant : {chemin}")

#challenge5

nom_fichier = "challenge5.txt"
f = open(nom_fichier, "w", encoding="utf-8")

for i in range(1, 6):
    ligne = f"Ligne numero {i}\n"
    f.write(ligne)
f.close()

print(f"Le fichier '{nom_fichier}' a ete cree et rempli avec succes.")
