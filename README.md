# Carcass
Projet : Créer une version en ligne du jeu Carcassonne 2 : chasseurs et cueilleurs

Seb, le fichier que nous avons regardé ensemble mercredi 01/08 est conservé sous le nom carcass_08001

La nouvelle version intègre beaucoup de changements:

- un fichier par classe python
- un répertoire pour le client
- un répertoire pour le serveur
- les classes Tuile, Square et CarcassGame constituent la modélisation du jeu et sont regroupées dans le répertoire carcassClient/model
- une partie coté serveur est représentée par la classe serverGame
- Les clients sont représentés coté serveur par la classe ServerChannel 
  
- Pour jouer :
  - lancer le serveur : python carcassServer/carcassServer.py localhost:1200 (par exemple)
  - lancer trois clients : python carcassClient/carcassClient.py localhost:1200 
  
- Le nombre de joueurs pour une partie est fixé à trois pour l'instant. Lorsque trois joueurs sont connectés, une nouvelle partie se lance.

- Les propriétés (ordre des cartes, numéro du tour, cartes jouées ) de la partie sont visibles dans la console du serveur
  
   
