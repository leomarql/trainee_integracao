#!/usr/bin/env python

from __future__ import print_function
import sys
import rospy
from beginner_tutorials.srv import *

def vel_control_client(x, y):
    rospy.wait_for_service('vel_control')
    try:
        vel_control = rospy.ServiceProxy('vel_control', VelControl)
        resp1 = vel_control(x, y)
        return resp1
    except rospy.ServiceException as e:
        print("Service call failed: %s"%e)

def usage():
    return "%s [x y]"%sys.argv[0]

if __name__ == "__main__":
    if len(sys.argv) == 3:
        x = float(sys.argv[1])
        y = float(sys.argv[2])
    else:
        print(usage())
        sys.exit(1)
    print("Requesting position (%s,%s)"%(x, y))
    print("target pos: (%s, %s)\n velocity: (%s)"%(x, y, vel_control_client(x, y)))