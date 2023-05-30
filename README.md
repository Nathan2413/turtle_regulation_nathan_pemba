# README

## Régulation en cap - Turtle 

Ce package ROS contient un nœud de régulation en cap pour un robot tortue simulé dans l'environnement turtlesim. Le nœud utilise une constante Kp pour calculer la commande en cap du turtle.

### Tester avec différentes valeurs de Kp
Voici les comportements observés pour différentes valeurs de Kp :

- Kp fort (on a pris, Kp = 2.0) : Le turtle réagit de manière très rapide aux erreurs de cap. Cela peut entraîner des oscillations importantes et une instabilité lors de l'approche du waypoint. Le turtle peut également dépasser légèrement le waypoint avant de se stabiliser.

- Kp faible (on a pris, Kp = 0.5) : Le turtle réagit lentement aux erreurs de cap. Cela peut entraîner une approche lente et peu précise du waypoint. Le turtle peut prendre plus de temps pour atteindre le waypoint et peut présenter des mouvements lents et saccadés.

- Kp choisi (on a pris, Kp = 1.0) : Cette valeur de Kp donne un bon compromis entre réactivité et stabilité. Le turtle réagit de manière appropriée aux erreurs de cap, avec une réponse rapide mais sans oscillations excessives. Le turtle atteint le waypoint avec précision et sans dépassement significatif.

Il est important de trouver la valeur de Kp qui convient le mieux à votre application spécifique en fonction de la dynamique de votre robot et de la précision souhaitée dans la régulation en cap.


