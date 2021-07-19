
import rospy
from std_msgs.msg import Float32MultiArray

def ultra_sensors():
    pub = rospy.Publisher('ultra_sensors',Float32MultiArray, queue_size=1)
    rospy.init_node('ultra_sensors', anonymous=False)
    rate = rospy.Rate(200) # 10hz
    array = [23.0, 22.3, 3.2, 55.6, 12.4]

    while not rospy.is_shutdown():
        ultra_str = Float32MultiArray(data = array)
        rospy.loginfo(ultra_str)
        pub.publish(ultra_str)
        rate.sleep()
 
if __name__ == '__main__':
    try:
        ultra_sensors()

    except rospy.ROSInterruptException:
        pass