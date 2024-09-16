#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry
from math import pow, atan2, sqrt
from tutorial_avant.srv import pontoDesejado, pontoDesejadoResponse

class TurtleBot3Control:
    def __init__(self):
        # Inicializa o nó ROS
        rospy.init_node('turtlebot3_control', anonymous=True)

        self.velocity_publisher = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
        self.odom_subscriber = rospy.Subscriber('/odom', Odometry, self.odom_callback)

        self.velocity_msg = Twist()

        # Define a posição alvo na odom
        # self.target_x = 2.0
        # self.target_y = 3.0

        # Define a tolerância para alcançar a posição alvo
        self.tolerance = 0.2

        # Inicializa a posição atual do TurtleBot3 na odom
        self.current_x = 0.0
        self.current_y = 0.0
        self.current_yaw = 0.0

    def odom_callback(self, odom):
        self.current_x = odom.pose.pose.position.x
        self.current_y = odom.pose.pose.position.y
        t3 = 2.0 * (odom.pose.pose.orientation.w * odom.pose.pose.orientation.z + odom.pose.pose.orientation.x + odom.pose.pose.orientation.y)
        t4 = 1.0 - 2.0 * (odom.pose.pose.orientation.y * odom.pose.pose.orientation.y + odom.pose.pose.orientation.z + odom.pose.pose.orientation.z)
        self.current_yaw = atan2(t3, t4)

    def move_turtlebot3(self, _pontoDesejado):
        # Define a taxa de atualização do loop
        rate = rospy.Rate(10)

        while not rospy.is_shutdown() and sqrt(pow((_pontoDesejado.x - self.current_x), 2) + pow((_pontoDesejado.y- self.current_y), 2)) >= self.tolerance:
            # Calcula o ângulo para a posição alvo
            angle_to_target = atan2(_pontoDesejado.y - self.current_y, _pontoDesejado.x - self.current_x)

            self.velocity_msg.linear.x = 0.2
            self.velocity_msg.angular.z = 1.5 * (angle_to_target - self.current_yaw)
            self.velocity_publisher.publish(self.velocity_msg)

            rate.sleep()

        # Quando a posição alvo é alcançada, para o TurtleBot3
        self.velocity_msg.linear.x = 0.0
        self.velocity_msg.angular.z = 0.0
        self.velocity_publisher.publish(self.velocity_msg)

        mensagem = 'O robô atingiu o ponto desejado'
        return pontoDesejadoResponse(mensagem)

if __name__ == '__main__':
    try:
        # Cria o objeto TurtleBot3Control
        turtlebot3_control = TurtleBot3Control()
        service = rospy.Service('/receberPonto', pontoDesejado, turtlebot3_control.move_turtlebot3)
        rospy.spin()

    except rospy.ROSInterruptException:
        pass