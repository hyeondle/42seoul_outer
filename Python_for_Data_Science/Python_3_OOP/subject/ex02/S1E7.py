from S1E9 import Character


class Baratheon(Character):
    """Repersenting the Baratheon family."""

    def __init__(self, first_name, is_alive=True):
        """Init the Baratheon"""
        super().__init__(first_name, is_alive)
        self.family_name = "Baratheon"
        self.eyes = "brown"
        self.hairs = "dark"

    def __str__(self):
        """Return the representation of the object"""
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def __repr__(self):
        """Return the representation of the object for debugging"""
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def die(self):
        """Kill the character (in Baratheon)"""
        self.is_alive = False


class Lannister(Character):
    """Repersenting the Lannister family."""

    def __init__(self, first_name, is_alive=True):
        """Init the Lannister"""
        super().__init__(first_name, is_alive)
        self.family_name = "Lannister"
        self.eyes = "blue"
        self.hairs = "light"

    def __str__(self):
        """Return the representation of the object"""
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def __repr__(self):
        """Return the representation of the object for debugging"""
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def die(self):
        """Kill the character (in Lannister)"""
        self.is_alive = False

    def create_lannister(first_name, is_alive):
        """Create a Lannister"""
        return Lannister(first_name, is_alive)
