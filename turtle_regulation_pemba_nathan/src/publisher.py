#!/usr/bin/env python3

import rospy
from math import atan2, sin, cos, sqrt
from turtlesim.msg import Pose
from geometry_msgs.msg import Twist
from std_msgs.msg import Bool

# Variables globales
current_pose = Pose()
waypoint = (7, 7)
Kpl = 1.0  # Constante de proportionnalité pour la vitesse linéaire
Kpa = 1.0  # Constante de proportionnalité pour la vitesse angulaire
distance_tolerance = 0.1  # Seuil de distance pour atteindre le waypoint
angle_tolerance = 0.1  # Seuil d'angle pour atteindre l'orientation désirée
is_moving_publisher = rospy.Publisher('is_moving', Bool, queue_size=1)

def pose_callback(data):
    global current_pose
    current_pose.x = data.x
    current_pose.y = data.y
    current_pose.theta = data.theta

def calculate_distance(point_a, point_b):
    return sqrt((point_b[0] - point_a[0])**2 + (point_b[1] - point_a[1])**2)

def regulate():
    rospy.init_node('turtle_regulation_publisher')
    rospy.Subscriber('pose', Pose, pose_callback)
    cmd_vel_publisher = rospy.Publisher('turtle1/cmd_vel', Twist, queue_size=1)
    rate = rospy.Rate(10)  # 10 Hz

    while not rospy.is_shutdown():
        distance_error = calculate_distance((current_pose.x, current_pose.y), waypoint)

        if distance_error > distance_tolerance:
            is_moving_publisher.publish(Bool(True))

            # Calcul de l'angle désiré
            desired_angle = atan2(waypoint[1] - current_pose.y, waypoint[0] - current_pose.x)

            # Calcul de l'erreur d'angle
            angle_error = atan2(sin(desired_angle - current_pose.theta), cos(desired_angle - current_pose.theta))

            # Calcul de la commande angulaire
            angular_velocity = Kpa * angle_error

            # Calcul de la commande linéaire
            linear_velocity = Kpl * distance_error

            # Publication de la commande
            cmd_vel_msg = Twist()
            cmd_vel_msg.linear.x = linear_velocity
            cmd_vel_msg.angular.z = angular_velocity
            cmd_vel_publisher.publish(cmd_vel_msg)
        else:
            is_moving_publisher.publish(Bool(False))

        rate.sleep()

if __name__ == '__main__':
    try:
        regulate()
    except rospy.ROSInterruptException:
        pass

