"""
Created on 06.12.2015.

@author: xx
"""

from jinja2.environment import Environment
from jinja2.loaders import PackageLoader
from execute.execute import execute
from root import SRC_DIR
from root import OUTPUT_DIR
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

    file_name = os.path.join(SRC_DIR, OUTPUT_DIR, output_name)
    print(file_name)
    with open(file_name, "w+") as f:
        f.write(rendered)


def init_folder_structure():
    if not os.path.exists(os.path.join(SRC_DIR, OUTPUT_DIR)):
        os.makedirs(os.path.join(SRC_DIR, OUTPUT_DIR))

    if not os.path.exists(os.path.join(SRC_DIR, OUTPUT_DIR, 'templates')):
        os.makedirs(os.path.join(SRC_DIR, OUTPUT_DIR, 'templates'))

    if not os.path.exists(os.path.join(SRC_DIR, OUTPUT_DIR, 'templates', OUTPUT_DIR)):
        os.makedirs(os.path.join(SRC_DIR, OUTPUT_DIR, 'templates', OUTPUT_DIR))


def main(debug=False):
    model = execute(os.path.join(SRC_DIR, "model"), 'model.tx', 'test.rbt', debug, debug)

    # TODO push this settings into the grammar, then remove this line
    model.OUTPUT_DIR = OUTPUT_DIR

    init_folder_structure()

    file_gen_list = {'__init__', 'models', 'views', 'urls', 'admin', 'tests'}
    for e in file_gen_list:
        generate("t{e}.tx".format(e=e), "{e}.py".format(e=e), {"model": model})


if __name__ == '__main__':
    main(False)
