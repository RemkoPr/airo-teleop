from teleop_agent import TeleopAgent, TeleopConfig
from airo_teleop_devices.gello_teleop_device import GelloTeleop


class Gello4UR_ParallelGripper(TeleopAgent):
    def __init__(self, gello_usb_port: str, ur_type: str, gripper_opening_range: tuple[float, float], config: TeleopConfig):
        if self.config.use_joint_space:
            def transform_func(raw_data):
                raise NotImplementedError("Joint space control not implemented yet")
        elif not self.config.use_joint_space:
            def transform_func(raw_data):
                raise NotImplementedError("Cartesian space control not implemented yet")
        teleop_device = GelloTeleop(gello_usb_port, transform_func=transform_func)
        super().__init__(config=config, teleop_device=teleop_device)
        self.ur_robot = ur_type

    def get_action(self, current_robot_pose):
        action = self.gello_teleop_device.get_state()
        self.prev_action = action
        return action
    
class Gello4UR3(Gello4UR_ParallelGripper):
    def __init__(self, gello_usb_port: str, config: TeleopConfig):
        raise NotImplementedError

class Gello4UR3_Robotiq(Gello4UR_ParallelGripper):
    def __init__(self, gello_usb_port: str, config: TeleopConfig):
        raise NotImplementedError
    
    
class Gello4UR3_Schunk(Gello4UR_ParallelGripper):
    def __init__(self, gello_usb_port: str, config: TeleopConfig):
        raise NotImplementedError
    
class Gello4UR5(Gello4UR_ParallelGripper):
    def __init__(self, gello_usb_port: str, config: TeleopConfig):
        raise NotImplementedError
    
class Gello4UR5_Robotiq(Gello4UR_ParallelGripper):
    def __init__(self, gello_usb_port: str, config: TeleopConfig):
        raise NotImplementedError
    
class Gello4UR5_Schunk(Gello4UR_ParallelGripper):
    def __init__(self, gello_usb_port: str, config: TeleopConfig):
        raise NotImplementedError
    