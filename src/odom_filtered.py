#!/usr/bin/env python3

import rospy
from std_msgs.msg import String
from sensor_msgs.msg  import Imu
from nav_msgs.msg import Odometry
from std_msgs.msg import Header
from gazebo_msgs.srv import GetModelState, GetModelStateRequest
from geometry_msgs.msg  import Twist, Point
from tf.transformations import euler_from_quaternion, quaternion_from_euler
from math import cos,sin



class PublishOdometry(object):



    def __init__(self):
        rospy.Subscriber("/odometry/filtered", Odometry, self.odo_cb) 
        self.odom_pub = rospy.Publisher('/my_odom_filtered', Odometry, queue_size=10)
        

    def get_odom(self):
        rospy.wait_for_service('/gazebo/get_model_state')
        get_model_srv = rospy.ServiceProxy('/gazebo/get_model_state', GetModelState)
        odom = Odometry()
        header = Header()
        header.frame_id = '/odom'
        model = GetModelStateRequest()
        model.model_name = 'husky'

        # Define the data localization
        result = get_model_srv(model)
        odom.pose.pose = result.pose
        odom.twist.twist= result.twist
        header.stamp = rospy.Time.now()
        odom.header = header
        self.odom_pub.publish(odom)

    def odo_cb(self, msg):
        self.get_odom()


rospy.init_node('odom_pub_filtered')

#dom_pub = rospy.Publisher('/my_odom', Odometry)

PublishOdometry()
rospy.spin()

# spin() simply keeps python from exiting until this node is stopped
#





""" 
rate = rospy.Rate(2)
 """
""" while not rospy.is_shutdown():
    result = get_model_srv(model)

    odom.pose.pose = result.pose
    odom.twist.twist = result.twist

    header.stamp = rospy.Time.now()
    odom.header = header

    odom_pub.publish(odom)

    rate.sleep() """
