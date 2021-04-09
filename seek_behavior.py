'''
Seek Steering Behavior

'''
# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.

# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
import math 

print("Implementing Seek Steering Behaviors...")
print("\n")

#The Player Class
class player:
    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)
        
    def current_position(self):
        return self.x, self.y

    def move_player_position(x, y):
        self.x = x
        self.y = x
        
    def get_position_x(self):
        return self.x
        
    def get_position_y(self):
        return self.y

#The NPC 

class npc:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.target_x = 0
        self.target_y = 0
        self.velocity_vector = [0,0]

    def get_x_coordinate(self):
        return self.x
    
    def get_y_coordinate(self):
        return self.y
    
    def set_target(self, px, py):
        self.target_x = px
        self.target_y = py

    def get_npc_velocity(self):
    #find the NPC velocity which is the hypotenuse
        self.velocity_vector[0] = self.target_x - self.get_x_coordinate() 
        self.velocity_vector[1] = self.target_y - self.get_y_coordinate()
        return self.velocity_vector
        
    def get_euler_position(self):
        print("Velocity vector {0}".format(self.velocity_vector))
        self.x = self.x + self.get_npc_velocity()[0]
        self.y = self.y + self.get_npc_velocity()[1]
        print("NPC Position position:({0}, {1}) ".format(self.x, self.y))
    
    def current_position(self):
        return self.x, self.y
    


def main():
    print("Please press C to change your coordinates at any time.")
    
    print("PLAYERChar please initialize your coordinates:")
    x = input("x-coordinate:")
    y = input("y-coordinate:")
    #create the player object
    p = player(x, y)
    #get the player's current position
    p.current_position()
    
    #initialize the npc
    n = npc(3,5)
    print ("Player position : NPC Target {0}".format(p.current_position()))
    print("NPC starting position {0}".format(n.current_position()))
    
    #give the NPC the target position
    n.set_target(p.get_position_x(), p.get_position_y())
    
    #keep moving until the npc arrives at target
    while(n.current_position() != p.current_position()):
        #keep moving npc
        n.get_euler_position()

    
print("Seek Steering Behavior Text Tutorial Complete")
    
    
    
if __name__ == "__main__":
    main()