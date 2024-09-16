import rospy
from visualization_msgs.msg import Marker, MarkerArray
from geometry_msgs.msg import Point

class RVizInterface:
    def __init__(self):
        self.marker_array = MarkerArray()
        self.marker_pub = rospy.Publisher("teste", MarkerArray, queue_size=10)

    def publish_marker(self, position, color, scale):
        marker = Marker()
        marker.header.frame_id = "map"
        marker.header.stamp = rospy.Time.now()
        marker.ns = "my_namespace"
        marker.id = len(self.marker_array.markers) + 1
        marker.type = Marker.CUBE
        marker.action = Marker.ADD
        marker.pose.position = Point(*position)
        marker.pose.orientation.w = 1.0
        marker.scale.x = scale
        marker.scale.y = scale
        marker.scale.z = scale
        marker.color.r, marker.color.g, marker.color.b = color
        marker.color.a = 1.0

        self.marker_array.markers.append(marker)
        self.marker_pub.publish(self.marker_array)

    def update_marker_color(self, position, color):
        for marker in self.marker_array.markers:
            if (
                abs(marker.pose.position.x - position[0]) < 0.01
                and abs(marker.pose.position.y - position[1]) < 0.01
                and abs(marker.pose.position.z - position[2]) < 0.01
            ):
                marker.color.r, marker.color.g, marker.color.b = color
                marker.color.a = 1.0

        self.marker_pub.publish(self.marker_array)

    def clean_markers(self):
        delete_marker = Marker()
        delete_marker.header.frame_id = "map"
        delete_marker.header.stamp = rospy.Time.now()
        delete_marker.ns = "my_namespace"
        delete_marker.id = 0
        delete_marker.action = Marker.DELETEALL

        self.marker_array.markers = [delete_marker]
        self.marker_pub.publish(self.marker_array)