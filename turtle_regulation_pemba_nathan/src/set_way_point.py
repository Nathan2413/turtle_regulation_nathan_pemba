#!/usr/bin/env python3
import rospy
from turtlesim.msg import Pose
from geometry_msgs.msg import Twist
from math import atan2, sin, cos, degrees

# Variable globale pour stocker la pose de la tortue
current_pose = Pose()

# Callback appelée lorsqu'un message est reçu sur le topic "pose"
def pose_callback(msg):
    global current_pose
    current_pose = msg

# Initialisation du nœud ROS
rospy.init_node('turtle_regulation_pemba_nathan')

# Souscription au topic "pose" avec la fonction de rappel pose_callback
rospy.Subscriber('pose', Pose, pose_callback)

# Définition du waypoint avec les coordonnées (7, 7)
# Coordonnées des points A et B
xA, yA = 0, 0  # Coordonnées de la tortue
xB, yB = 7, 7  # Coordonnées du waypoint
# Calcul de l'angle désiré en degrés
desired_angle = degrees(atan2(yB - yA, xB - xA))

# Constante de proportionnalité Kp pour l'angle
Kp_angle = 2.0

# Constante de proportionnalité Kp pour la distance
Kp_distance = 2.0

# Boucle principale
rate = rospy.Rate(10)  # Fréquence de publication (10 Hz)
while not rospy.is_shutdown():
    # Calcul de l'erreur d'angle
    error_angle = atan2(sin(desired_angle - current_pose.theta), cos(desired_angle - current_pose.theta))
    
    # Calcul de la commande en vitesse angulaire (cap) du robot
    command_angular = Kp_angle * error_angle
    
    # Calcul de l'erreur de distance
    error_distance = ((xB - xA)**2 + (yB - yA)**2)**0.5
    
    # Calcul de la commande en vitesse linéaire (avance) du robot
    command_linear = Kp_distance * error_distance
    
    # Création d'un objet Twist avec les vitesses linéaire et angulaire
    twist = Twist()
    twist.linear.x = command_linear
    twist.angular.z = command_angular
    
    # Création d'un éditeur pour publier sur le topic "cmd_vel"
    pub = rospy.Publisher('turtle1/cmd_vel', Twist, queue_size=10)
    pub.publish(twist)

    rate.sleep()
