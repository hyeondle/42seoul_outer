from S1E7 import Baratheon, Lannister

class King(Baratheon, Lannister):
    def __init__(self, first_name, is_alive=True):
        """Init the king"""
        super().__init__(first_name, is_alive)

    def die(self):
        """Kill the king"""
        self.is_alive = False

    def set_eyes(self, eyes):
        """Set the eyes color"""
        self.eyes = eyes

    def set_hairs(self, hairs):
        """Set the hairs color"""
        self.hairs = hairs

    def get_eyes(self):
        """Return the eyes color"""
        return self.eyes

    def get_hairs(self):
        """Return the hairs color"""
        return self.hairs