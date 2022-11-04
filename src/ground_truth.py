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



class PublishGroundTruth(object):


  def __init__(self):

    rospy.Subscriber("/ground_truth", Odometry, self.gt_cb) 
    self.pub_gt = rospy.Publisher('/my_odom_ground_truth', Odometry, queue_size=10)
  





  def get_gt(self):
    rospy.wait_for_service('/gazebo/get_model_state')
    get_model_srv = rospy.ServiceProxy('/gazebo/get_model_state', GetModelState)
    odom = Odometry()
    header = Header()
    header.frame_id = '/gt'
    model = GetModelStateRequest()
    model.model_name = 'husky'

    # Define the data localization
    result = get_model_srv(model)
    odom.pose.pose = result.pose
    odom.twist.twist= result.twist
    header.stamp = rospy.Time.now()
    odom.header = header
    self.pub_gt.publish(odom)

  def gt_cb(self, msg):
    self.get_gt()
 


    
 
 

rospy.init_node('pub_gt')


PublishGroundTruth()


# spin() simply keeps python from exiting until this node is stopped
rospy.spin()
