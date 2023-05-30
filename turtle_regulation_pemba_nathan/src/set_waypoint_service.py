#!/usr/bin/env python3

import rospy
from turtle_regulation_pemba_nathan1.srv import waypoint
from geometry_msgs.msg import Point

waypoint = Point()

def set_waypoint_callback(req):
    global waypoint
    waypoint = req.way_point
    return True

rospy.init_node('set_waypoint_service')
rospy.Service('set_waypoint_service', SetWaypoint, set_waypoint_callback)

rospy.spin()


rospy.wait_for_service('set_waypoint_service')
try:
    set_waypoint = rospy.ServiceProxy('set_waypoint_service', SetWaypoint)
    response = set_waypoint(2, 2)  # Set a new waypoint at (7, 7)
    if response:
        rospy.loginfo('Waypoint set successfully')
    else:
        rospy.logwarn('Failed to set waypoint')
except rospy.ServiceException as e:
    rospy.logerr('Service call failed: %s' % e)
