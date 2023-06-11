#!/usr/bin/env python3
import rospy
from tutorial_avant.srv import pontoDesejado

if __name__ == '__main__':
    rospy.init_node('client')
    rospy.wait_for_service('/receberPonto')

    try:
        enviarPonto = rospy.ServiceProxy('/receberPonto', pontoDesejado)
        mensagem = enviarPonto(2, 2)
        rospy.loginfo(mensagem.message)
    except rospy.ServiceException as Error:
        rospy.loginfo(Error)