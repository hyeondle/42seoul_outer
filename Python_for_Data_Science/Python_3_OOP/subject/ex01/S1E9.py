from abc import ABC, abstractmethod


class Character(ABC):
    """Abstract class for specify all characters"""

    def __init__(self, first_name, is_alive=True):
        """Init the character"""
        self.first_name = first_name
        self.is_alive = is_alive

    @abstractmethod
    def die(self):
        """Kill the character"""
        pass


class Stark(Character):
    """Class about Stark"""

    def die(self):
        """Kill the character (in Stark)"""
        self.is_alive = False
