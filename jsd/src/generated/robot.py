'''
Created on 06.12.2015.

@author: xx
'''

from jinja2.environment import Environment
from jinja2.loaders import PackageLoader
from execute.execute import execute
from root import SRC_DIR 
import os

class Robot(object):
           
    def interpret(self, model):
        print(model)
            
def generate(template_name, output_name, render_vars):
    env = Environment(trim_blocks = True, lstrip_blocks = True, loader = PackageLoader("generated", "templates"))
    
    template = env.get_template(template_name)
    rendered = template.render(render_vars)
    #i pisemo u fajl
    file_name = os.path.join(SRC_DIR, "output", output_name)
    print(file_name)
    with open(file_name, "w+") as f:
        f.write(rendered)




def main(debug = False):
    
    model = execute(os.path.join(SRC_DIR, "model"), 'model.tx', 'test.rbt', debug, debug)
    robot = Robot()
    robot.interpret(model)
    generate("tmodels.tx", "models.py", {"model" : model})
   
   
    
    
if __name__ == '__main__':
    main(True)
    
    