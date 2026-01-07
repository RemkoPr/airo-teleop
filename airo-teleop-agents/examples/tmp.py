from airo_robots.manipulators.hardware.ur_rtde import URrtde
import ur_analytic_ik


ur = URrtde(ip_address="10.42.0.162")
joint_pose = ur.get_joint_configuration()
tcp_pose = ur.get_tcp_pose()
calculated_tcp_pose = ur_analytic_ik.ur5e.forward_kinematics(*joint_pose)
print(f"UR reported joint pose: {joint_pose}")
print(f"UR reported tcp pose:\n {tcp_pose}")
print(f"Calculated tcp pose:\n {calculated_tcp_pose}")