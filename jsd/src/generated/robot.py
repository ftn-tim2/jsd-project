'''
Created on 06.12.2015.

@author: xx
'''

from jinja2.environment import Environment
from jinja2.loaders import PackageLoader
from execute.execute import execute
from root import SRC_DIR 
import os
           
def typeDef(typeDef):
    if typeDef == "char":
        return "CharField"
    elif typeDef == "int":
        return "IntegerField"
    elif typeDef == "bigInteger":
        return "BigIntegerField"
    elif typeDef == "binary":
        return "BinaryField"
    elif typeDef == "boolean":
        return "BooleanField"
    elif typeDef =="commaSeparatedInteger":
        return "CommaSeparatedIntegerField"
    elif typeDef =="date":
        return "DateField"
    elif typeDef == "dateTime":
        return "DateTimeField"
    elif typeDef == "decimal":
        return "DecimalField"
    elif typeDef == "duration":
        return "DurationField"
    elif typeDef == "email":
        return "EmailField"
    elif typeDef == "file":
        return "FileField"
    elif typeDef == "filePath":
        return "FilePathField"
    elif typeDef == "float":
        return "FloatField"
    elif typeDef == "image":
        return "ImageField"
    elif typeDef =="nullBoolean":
        return "NullBooleanField"
    elif typeDef == "positiveInteger":
        return "PositiveIntegerField"
    elif typeDef == "slug":
        return "SlugField"
    elif typeDef == "smallInteger":
        return "SmallIntegerField"
    elif typeDef == "text":
        return "TextField"
    elif typeDef == "time":
        return "TimeField"
    elif typeDef == "URL":
        return "URLField"
    elif typeDef == "UUID":
        return "UUIDField"
    elif typeDef == "foreignKey":
        return "ForeignKey"
    elif typeDef == "oneToOne":
        return "OneToOneField"
    elif typeDef == "manyToMany":
        return "ManyToManyField"
    
def checkType(someitem):
    if  ( someitem =='foreignKey' or someitem =='oneToOne' or someitem =='manyToMany'):
        return True
    else:
        return False
            
def generate(template_name, output_name, render_vars):
    env = Environment(trim_blocks = True, lstrip_blocks = True, loader = PackageLoader("generated", "templates"))
    env.filters["typeDef"] = typeDef
    env.tests["checkType"] = checkType
    
    template = env.get_template(template_name)
    rendered = template.render(render_vars)
    #i pisemo u fajl
    file_name = os.path.join(SRC_DIR, "output", output_name)
    print(file_name)
    with open(file_name, "w+") as f:
        f.write(rendered)




def main(debug = False):
    
    model = execute(os.path.join(SRC_DIR, "model"), 'model.tx', 'test.rbt', debug, debug)
    generate("tmodels.tx", "models.py", {"model" : model})
   
   
    
    
if __name__ == '__main__':
    main(True)
    
    