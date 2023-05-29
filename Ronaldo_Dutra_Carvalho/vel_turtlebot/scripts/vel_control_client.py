#!/usr/bin/env python3

import rospy
from vel_turtlebot.srv import velocity_control

if __name__ == '__main__':
     rospy.init_node("vel_control_client")

     rospy.wait_for_service("/controlar_velocidade")

     try:
        movimentar_turtle = rospy.ServiceProxy("/controlar_velocidade", velocity_control)
        x = float(input("insira a coordenada x"))
        y = float(input("insira a coordenada y"))
        resposta = movimentar_turtle(x,y)
        rospy.loginfo("A tartaruga chegou:"+str(resposta.acertouAlvo))
     except rospy.ServiceException as e:
        rospy.logwarn("Serviço falhou: " + str(e))