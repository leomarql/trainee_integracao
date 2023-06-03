##!/usr/bin/env python
from __future__ import print_function

import sys
import rospy
from beginner_tutorials.srv import *

def vel_control_client(x, y):
    rospy.wait_for_service('vel_control')
    try:
        vel_control = rospy.ServiceProxy('vel_control', Vel_Control)
        resp1 = vel_control(x, y)
    except rospy.ServiceException as e:
        print("Service call failed: %s"%e)

def usage():
    return "%s [x y]"%sys.argv[0]

if __name__ == "__main__":
    if len(sys.argv) == 3:
        x = int(sys.argv[1])
        y = int(sys.argv[2])
    else:
        print(usage())
        sys.exit(1)
    response = vel_control_client(x, y)
    print("Pos x final = %s, Pos y final  = %s" % (x, y))
   