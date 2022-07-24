#!/usr/bin/env python

import rospy
import actionlib
import tf
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal

# the list of points to patrol
waypoints = [
    ['one', (-9.00926589966,-7.3114233017, -0.715664389043)],
    ['two', (-12.3895702362,-16.8471450806,-0.6190094399)],
    ['three', (-8.93702888489,-17.0259094238, 0.714991778648)]
]

class Patrol:

    def __init__(self):
        self.client = actionlib.SimpleActionClient('move_base', MoveBaseAction)
        self.client.wait_for_server()

    def set_goal_to_point(self, point):

        self.client.send_goal(goal)
        wait = self.client.wait_for_result()
        if not wait:
            rospy.logerr("Action server not available!")
            rospy.signal_shutdown("Action server not available!")
        else:
            return self.client.get_result()


if __name__ == '__main__':
    rospy.init_node('patrolling')
    try:
        while not rospy.is_shutdown():
            for i, w in enumerate(waypoints):
                rospy.loginfo("Sending waypoint %d - %s", i, w[0])
                p.set_goal_to_point(w[1])
    except rospy.ROSInterruptException:
        rospy.logerr("Something went wrong when sending the waypoints")
