import rospy
from AStar import AStarPlanner
from rvizGraphics import RVizInterface
from nav_msgs.msg import OccupancyGrid
from geometry_msgs.msg import PointStamped

def clicked_point_callback(clicked_point):
    global planner, start_pose, goal_pose

    if start_pose is None:
        rviz.clean_markers()
        start_pose = (clicked_point.point.x, clicked_point.point.y)
        rviz.publish_marker((start_pose[0], start_pose[1], 0.0), (1.0, 0, 0), map.info.resolution)
        rospy.loginfo("PosiÃ§Ã£o inicial definida: x = %f, y = %f", start_pose[0], start_pose[1])
    elif goal_pose is None:
        goal_pose = (clicked_point.point.x, clicked_point.point.y)
        rviz.publish_marker((goal_pose[0], goal_pose[1], 0.0), (1.0, 0, 0), map.info.resolution)
        rospy.loginfo("PosiÃ§Ã£o goal definida: x = %f, y = %f", goal_pose[0], goal_pose[1])
        # Ambas as posiÃ§Ãµes foram definidas, chamar a funÃ§Ã£o find_path
        planner.start_pose_x, planner.start_pose_y = start_pose
        planner.goal_pose_x, planner.goal_pose_y = goal_pose
        planner.find_path(rviz)
        start_pose = None
        goal_pose = None


if __name__ == '__main__':
    rospy.init_node('a_star_planner')

    planner = AStarPlanner()
    rviz = RVizInterface()

    # VariÃ¡veis para armazenar as posiÃ§Ãµes inicial e goal
    start_pose = None
    goal_pose = None
    planner.execution_speed = 0.1

    # Inscrever no tÃ³pico /map para receber o occupancy grid
    rospy.Subscriber('/map', OccupancyGrid, planner.map_callback)
    map = rospy.wait_for_message('/map', OccupancyGrid)

    # Inscrever no tÃ³pico /clicked_point para receber os pontos clicados pelo usuÃ¡rio
    rospy.Subscriber('/clicked_point', PointStamped, clicked_point_callback)

    # Spin ROS
    rospy.spin()