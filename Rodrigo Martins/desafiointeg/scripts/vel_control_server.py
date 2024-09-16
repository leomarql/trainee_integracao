#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry
from math import pow,atan2,sqrt
from desafiointeg.srv import Vel_controled, Vel_controledResponse

class TurtleBot3Control:
    def __init__(self):
        #Inicializa o nó ROS
        rospy.init_node('turtlebot3_control',anonymous= True)
        
        self.velocity_publisher = rospy.Publisher('/cmd_vel',Twist, queue_size=10)
        self.odom_substriber = rospy.Subscriber('/odom',Odometry, self .odom_callback)
        
        self.velocity_msg = Twist()
        
        # Define a posição alvo na odom
        self.target_x = 5.0
        self.target_y = 5.0
        
        # Define a tolerância para alcançar a posição alvo
        self.tolerance = 0.2
        
        # Inicializa a posição atual do TurtleBot3 na odom
        self.current_x = 0.0
        self.current_y = 0.0
        self.current_yaw = 0.0
        
    def odom_callback(self , odom):
        self.current_x = odom.pose.pose.position.x
        self.current_y = odom.pose.pose.position.target_y
        t3 = 2.0 * (odom.pose.pose.orientation.w * odom.pose.pose.orientation.z + odom.pose.pose.orientation.x + odom.pose.pose.orientation.y)
        t4 = 1.0 - 2.0 * (odom.pose.pose.orientation.y * odom.pose.pose.orientation.y + odom.pose.pose.orientation.z + odom.pose.pose.orientation.z)
        self.current_yaw = atan2(t3 , t4)
    
    def move_turtlebot3(self):
        # Define a taxa de atualização do loop
        rate = rospy.Rate(10)
        
        while not rospy.is_shutdown() and sqrt(pow((self.target_x - self.current_x),2)+ pow((self.target_y - self.current_y),2)) >= self.tolerance:
             # Calcula o ângulo para a posição alvo
            angle_to_target = atan2(self.target_y - self.current_y,self.target_x - self.current_x)
            
            self.velocity_msg.linear.x =0.2
            self.velocity_msg.angular.z =1.5 * (angle_to_target - self.current_yaw)
            self.velocity_publisher.publish(self.velocity_msg)
            
            rate.sleep()
        # Quando a posição alvo é alcançada, para o TurtleBot3
        self.velocity_msg.linear.x = 0.0
        self.velocity_msg.angular.z = 0.0
        self.velocity_publisher.publish(self.velocity_msg)
        
    def alvo_vel_control(self , req):
        self.target_x = req.x
        self.target_y = req.y
        self.move_turtlebot3()
        return Vel_controlResponse(True)
    
    def vel_control_server(self):
        s = rospy.Service('vel_controled',Vel_controled,self.alvo_vel_control)
        print("Preparado para receber a posição.")
        rospy.spin()
        
if __name__ == '__main__':
    try:
        
        turtlebot3_control = TurtleBot3Control()               
        
        turtlebot3_control.vel_control_server()
        
    except rospy.ROSInterruptException:
        pass