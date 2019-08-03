# Carcass
Projet : Créer une version en ligne du jeu Carcassonne 2 : chasseurs et cueilleurs

Seb, le fichier que nous avons regardé ensemble mercredi 01/08 est carcass_08001

La nouvelle version intègre beaucoup de changement:

- un fichier par classe python: 
- un répertoire pour le client
- un répertoire pour le serveur
- les classes Tuile, Square et CarcassGame constituent la modélisation du jeu et sont regroupées dans le répertoire carcassClient/model
  
  Pour jouer :
   lancer le serveur : python carcassServer/carcassServer.py localhost:1200 (par exemple)
   lancer trois clients : python carcassClient/carcassClient.py localhost:1200 (le nombre de joueurs pour une partie est fixé à trois)
