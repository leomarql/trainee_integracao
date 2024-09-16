#!/usr/bin/env python3

#from _future_impor print_function
import sys
import rospy
from desafiointeg.srv import Vel_controled

def vel_control_client(x,y):
    rospy.wait_for_service('Vel_control')
    try:
        Vel_control = rospy.ServiceProxy('Vel_control',Vel_control)
        resp1 = Vel_control(x,y)
        rospy
        return resp1
    except rospy.ServiceException as e:
        print("Service call failed: %s"%e)
    
def usage():
    return "%s [x y]"%sys.argv[0]

if __name__=="__main__":
    if len(sys.argv) == 3:
        x = float(sys.argv[1])
        y = float(sys.argv[2])
    else:
        print(usage())
        sys.exit(1)
        
    print("Posição: (%s,%s)"%(x,y))
    
    print("Posição estabelecida:(%s,%s) "%(x,y,vel_control_client(x,y)))