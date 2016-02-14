"""
Created on 06.12.2015.

@author: xx
"""

from jinja2.environment import Environment
from jinja2.loaders import PackageLoader
from execute.execute import execute
from root import SRC_DIR
import os


def typeDef(typedef):
    if typedef == "char":
        return "CharField"
    elif typedef == "int":
        return "IntegerField"
    elif typedef == "bigInteger":
        return "BigIntegerField"
    elif typedef == "binary":
        return "BinaryField"
    elif typedef == "boolean":
        return "BooleanField"
    elif typedef == "commaSeparatedInteger":
        return "CommaSeparatedIntegerField"
    elif typedef == "date":
        return "DateField"
    elif typedef == "dateTime":
        return "DateTimeField"
    elif typedef == "decimal":
        return "DecimalField"
    elif typedef == "duration":
        return "DurationField"
    elif typedef == "email":
        return "EmailField"
    elif typedef == "file":
        return "FileField"
    elif typedef == "filePath":
        return "FilePathField"
    elif typedef == "float":
        return "FloatField"
    elif typedef == "image":
        return "ImageField"
    elif typedef == "nullBoolean":
        return "NullBooleanField"
    elif typedef == "positiveInteger":
        return "PositiveIntegerField"
    elif typedef == "slug":
        return "SlugField"
    elif typedef == "smallInteger":
        return "SmallIntegerField"
    elif typedef == "text":
        return "TextField"
    elif typedef == "time":
        return "TimeField"
    elif typedef == "URL":
        return "URLField"
    elif typedef == "UUID":
        return "UUIDField"
    elif typedef == "foreignKey":
        return "ForeignKey"
    elif typedef == "oneToOne":
        return "OneToOneField"
    elif typedef == "manyToMany":
        return "ManyToManyField"


def checkType(someitem):
    if someitem == 'foreignKey' or someitem == 'oneToOne' or someitem == 'manyToMany':
        return True
    else:
        return False


def generate(template_name, output_name, render_vars):
    env = Environment(trim_blocks=True, lstrip_blocks=True, loader=PackageLoader("generated", "templates"))
    env.filters["typeDef"] = typeDef
    env.tests["checkType"] = checkType

    template = env.get_template(template_name)
    rendered = template.render(render_vars)
    # i pisemo u fajl
    file_name = os.path.join(SRC_DIR, "output", output_name)
    print(file_name)
    with open(file_name, "w+") as f:
        f.write(rendered)


def main(debug=False):
    model = execute(os.path.join(SRC_DIR, "model"), 'model.tx', 'test.rbt', debug, debug)
    generate("tmodels.tx", "models.py", {"model": model})


if __name__ == '__main__':
    main(False)
