#!/usr/bin/env python
import rospy

if __name__ =='__main__':

    rospy.init_node('dummy')
    rospy.loginfo('Dummy : starts')
    rospy.spin()
    rospy.loginfo('Dummy : Bye Bye')
