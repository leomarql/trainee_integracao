#!/usr/bin/env python

from __future__ import print_function

import sys
import rospy
from beginner_tutorials.srv import Vel_control

def vel_control_client(x, y):
    rospy.init_node('vel_control_client')
    rospy.wait_for_service('vel_control')
    try:
        vel_control1 = rospy.ServiceProxy('vel_control', Vel_control)
        resp = vel_control1(x, y)
        return resp.result
    except rospy.ServiceException as e:
        print('Falha ao chamar o serviço: %s'%e)

def usage():
    return "%s [x y]"%sys.argv[0]

if __name__ == "__main__":
    if len(sys.argv) == 3:
        x = float(sys.argv[1])
        y = float(sys.argv[2])
    else:
        print(usage())
        sys.exit(1)
    print('posição:\n x:%s \n y:%s'%(x, y))
    print('atingiu o alvo? %s'%(vel_control_client(x, y)))