class Warior:
    player_healt = 100
    position_x = 6
    position_y = 0

    def __init__(self, name):
        self.name = name

    def take_damege(self):
        Warior.player_healt -= 1
        return f"Your player is {self.name}, and he has {self.player_healt} healt."
    
    def move_left(self):
        Warior.position_x -= 1
        return f"{self.name} is in cel {self.position_x}"
    
    def move_right(self):
        Warior.position_x += 1
        return f"{self.name} is in cel {self.position_x}"
    
    def move_down(self):
        Warior.position_y -= 1
        return f"{self.name} is in cel {self.position_y}"
    
    def move_up(self):
        Warior.position_y += 1
        return f"{self.name} is in cel {self.position_y}"

warrior_1 = Warior("Paula")
warrior_2 = Warior("Paul")

print(warrior_1.take_damege())
print(warrior_1.move_up())