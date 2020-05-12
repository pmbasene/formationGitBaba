# Memo Git

## Faire un commit

Les differentes etapes pour faire un commit de son fichier

1- **git init "nom_du_dossier"**

Permet d'initialiser le dossier qui comporte les fichiers à versionner. Soit on se deplace vers le dossier en question grace à  la commande *cd* soit on donne le chemin absolu _path/to/dir_

2- **git add "nom_du_fichier"**

3- **git commit --message "ceci est description des modifications effectuées sur le fichier"**

>> Astuce raccourci: on peut combiner les commandes 2 et 3 en une seule grace à la syntaxe suivante:  
**git commit -am "ceci est description des modifi effectuées sur le fichier"**  

## Analyse les fichiers

Il peut aariver qu'on veuille savoir l'etat de notre dossier de travail (working directory) c'est à dire verifier quels sont les fichiers qui ont ete modifiés et quelles lignes specifiquement ont ete modifiées , et par qui?  l'historiques des modifications. Tout un tas d'informations relatives aux fichiers. Ainsi Git permet offre des commandes pour cet effet:

a- **git status**  

b- **git diff**

Permet de compare l'ancienne version du fichier à la nouvelle version modifié

c- **git log**

Nous liste l'historique de toutes les modifications des fichiers depuis la date de creation (ou de premier commit).  

## Branch and Merge

Pour travailler sur une version donnée d'un fichier, on peut/doit creer une branche. L'idee de pouvoir evoluer sur une partie de ce fichier de son cote sans affecte ou corrompre le reste du document. Ce qui permet aussi de pouvoir revenir aux verions anterieures facilement.

