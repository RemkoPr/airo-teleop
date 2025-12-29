from teleop_device import TeleopDevice


class SpaceMouseTeleop(TeleopDevice):
    def __init__(self, gello_interface):
        super().__init__()
        # ...

    def get_raw_state(self):
        raise NotImplementedError