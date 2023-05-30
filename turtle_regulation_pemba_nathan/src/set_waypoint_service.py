#!/usr/bin/env python3

import rospy
from turtle_regulation_pemba_nathan1.srv import waypoint
from std_msgs.msg import Bool

waypoint_coords = (0.0, 0.0)  # Coordonnées initiales du waypoint

def set_waypoint_callback(request):
    global waypoint_coords
    waypoint_coords = (request.x, request.y)
    response = Bool()
    response.data = True
    return response

rospy.init_node('set_way_point')
service = rospy.Service('set_waypoint_service', waypoint, set_waypoint_callback)

rospy.spin()
