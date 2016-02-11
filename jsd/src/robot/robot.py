'''
Created on 06.12.2015.

@author: xx
'''

from textx.metamodel import metamodel_from_file
from textx.export import metamodel_export, model_export
import pydot
from textx.exceptions import TextXSemanticError

class Robot(object):
           
    def interpret(self, model):
        print("nema sintaksnih gresaka")
            
            
    def __str__(self):
        return "Robot position is {}, {}.".format(self.x, self.y)


if __name__ == '__main__':

    robot_mm = metamodel_from_file('model.tx', debug = False)
    
    robot_model = robot_mm.model_from_file('test.rbt')
    robot = Robot()
    robot.interpret(robot_model)
   

    