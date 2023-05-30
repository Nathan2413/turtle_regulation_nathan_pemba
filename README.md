# Turtle Regulation - TP1 ROBO
Ce projet GitHub contient les codes et les fichiers nécessaires pour la régulation en cap et en distance d'une tortue dans le simulateur turtlesim.

## Installation
1- Clonez ce projet GitHub dans votre workspace catkin catkin_ws/src :

```git clone https://github.com/votre_nom/turtle_regulation_nathan_pemba.git```

2- Compilez le package en utilisant catkin_make :
```cd catkin_ws```

 ```catkin_make```

3- Sourcez votre workspace :
*source catkin_ws/devel/setup.bash

## Utilisation
Régulation en cap
1- Lancez le nœud set_way_point.py pour la régulation en cap :
*roslaunch turtle_regulation_nathan_pemba set_way_point.launch

2- Le nœud se souscrit au topic /pose pour obtenir la position de la tortue et publie sur le topic /cmd_vel pour envoyer la commande de mouvement.

3-Les paramètres de régulation peuvent être ajustés en modifiant le fichier config/set_way_point.yaml.

4-Les comportements pour différentes valeurs de Kp (constante de proportionnalité) peuvent être observés et ajustés dans le fichier set_way_point.py.

## Régulation en distance
1- Lancez le nœud set_way_point_distance.py pour la régulation en distance :
* roslaunch turtle_regulation_nathan_pemba set_way_point_distance.launch

2- Le nœud se souscrit au topic /pose pour obtenir la position de la tortue et publie sur le topic /cmd_vel pour envoyer la commande de mouvement.

3- Les paramètres de régulation peuvent être ajustés en modifiant le fichier config/set_way_point_distance.yaml.

4- Les comportements pour différentes valeurs de Kpl (constante de proportionnalité linéaire) peuvent être observés et ajustés dans le fichier set_way_point_distance.py.

## Modification du waypoint
1- Utilisez le service set_waypoint_service pour modifier le waypoint de la tortue.
* rosservice call /set_waypoint_service "x: 5.0 y: 5.0"*

## Launch file**
1- Un fichier launch est fourni pour faciliter le lancement des nœuds :
* roslaunch turtle_regulation_nathan_pemba regulation.launch*

## Comportements pour différentes valeurs de Kp et Kpl**
1- Kp/Kpl fort(e) : La tortue réagira de manière plus agressive à l'erreur, entraînant des mouvements plus rapides mais potentiellement moins stables.

2- Kp/Kpl faible : La tortue réagira de manière plus douce à l'erreur, entraînant des mouvements plus lents mais plus stables.

3- Kp/Kpl choisi(e) : La valeur spécifique de Kp/Kpl peut être choisie en fonction des besoins spécifiques du système et des performances souhaitées. Il est recommandé de tester différentes valeurs pour trouver un équilibre entre la réactivité et la stabilité du système.

