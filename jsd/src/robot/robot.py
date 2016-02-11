'''
Created on 06.12.2015.

@author: xx
'''

from textx.metamodel import metamodel_from_file
from textx.export import metamodel_export, model_export
import pydot
from textx.exceptions import TextXSemanticError

class Robot(object):
    
    def __init__(self):
        self.x = 0
        self.y = 0
        
    def interpret(self, model):
        
        for command in model.commands:
            if command.__class__.__name__ == 'InitCommand':
                self.x = command.xPos
                self.y = command.yPos
            else:
                #move command
                direction = command.direction
                
                move = {
                    'up': (0, 1),
                    'down': (0, -1),
                    'left': (-1, 0),
                    'right': (1, 0)
                }[direction]

                # Calculate new robot position
                self.x += command.steps * move[0]
                self.y += command.steps * move[1]
                    
    def __str__(self):
        return "Robot position is {}, {}.".format(self.x, self.y)

def move_command_processor(move_cmd):
    if move_cmd.steps < 0:
        raise TextXSemanticError('Broj koraka ne moze biti negativan')
    elif move_cmd.steps == 0:
        move_cmd.steps = 1

if __name__ == '__main__':

    robot_mm = metamodel_from_file('model.tx', debug = False)
    
    robot_model = robot_mm.model_from_file('test.rbt')
    robot = Robot()
    robot.interpret(robot_model)
    print(robot)
   

    