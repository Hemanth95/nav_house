#!/usr/bin/env python3
import rclpy
from geometry_msgs.msg import PoseStamped
from simple_commander import BasicNavigator
import tf_transformations
import sys

def create_pose_stamp(navigator, pos_x, pos_y, oren_z):
    q_x, q_y, q_z, q_w = tf_transformations.quaternion_from_euler(0.0, 0.0, oren_z)
    pose = PoseStamped()
    pose.header.frame_id = 'map'
    pose.header.stamp = navigator.get_clock().now().to_msg();
    pose.pose.position.x = pos_x
    pose.pose.position.y = pos_y
    pose.pose.position.z = 0.0
    pose.pose.orientation.x = q_x
    pose.pose.orientation.y = q_y
    pose.pose.orientation.z = q_z
    pose.pose.orientation.w = q_w
    return pose

def create_positions(navigator):
    positions={}
    positions['bathroom'] = create_pose_stamp(navigator, 3.0, 3.5, -1.5)
    positions['dining'] = create_pose_stamp(navigator, 0.5, 0.5, 1.5)
    positions['living'] = create_pose_stamp(navigator, 5.0, 2.6, 1.5)
    positions['home'] = create_pose_stamp(navigator, 0.0, 0.0, 0.0)
    positions['kitchen'] = create_pose_stamp(navigator, -4.0, 3.5, -1.50)
    positions['room2'] = create_pose_stamp(navigator, 8.0, -1.06, -3)
    positions['room1'] = create_pose_stamp(navigator, -4.0, 0.0, 0.0)
    return positions
    


def main():
    rclpy.init()
    nav = BasicNavigator()
    positions = create_positions(nav)
    initial_pose = create_pose_stamp(nav, -0.0, 0.0, 0.0)
    nav.waitUntilNav2Active()
    if positions.get(sys.argv[1]) != None:
        nav.goToPose(positions[sys.argv[1]])
        # for waypoint in waypoints:
        #     nav.goToPose(waypoint)
        while not nav.isTaskComplete():
            feedback = nav.getFeedback()
            print(feedback)

    # nav.waitUntilNav2Active()

    rclpy.shutdown()
    pass
if __name__=='__main__':
    main()