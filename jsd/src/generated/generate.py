"""
Created on 06.12.2015.

@author: xx
"""

import os

from jinja2.environment import Environment
from jinja2.loaders import PackageLoader

from execute.execute import execute
from root import BASE_PATH
from root import SRC_DIR


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


def generate(template_name, output_name, render_vars, output_dir):
    env = Environment(trim_blocks=True, lstrip_blocks=True, loader=PackageLoader("generated", "templates"))
    env.filters["typeDef"] = typeDef
    env.tests["checkType"] = checkType

    template = env.get_template(template_name)
    rendered = template.render(render_vars)

    file_name = os.path.join(output_dir, output_name)
    print(file_name)
    with open(file_name, "w+") as f:
        f.write(rendered)


def init_folder_structure(base_path, templates_path, final_templates_path):
    if not os.path.exists(base_path):
        os.makedirs(base_path)

    if not os.path.exists(templates_path):
        os.makedirs(templates_path)

    if not os.path.exists(final_templates_path):
        os.makedirs(final_templates_path)


def main(debug=False):
    model = execute(os.path.join(SRC_DIR, "model"), 'model.tx', 'test.rbt', debug, debug)

    base_path = os.path.join(BASE_PATH, model.name)
    templates_path = os.path.join(base_path, 'templates')
    final_templates_path = os.path.join(templates_path, model.name)

    init_folder_structure(base_path, templates_path, final_templates_path)

    file_gen_list = {'__init__', 'models', 'views', 'urls', 'admin', 'tests'}
    template_file_gen_list = {'class_confirm_delete', 'class_form', 'class_list'}

    for e in file_gen_list:
        generate('t{e}.tx'.format(e=e), '{e}.py'.format(e=e), {'model': model}, base_path)

    for definition in model.classes:
        for e in template_file_gen_list:
            output_file_name = e.replace('class', definition.name.lower())
            generate('htmltemplates/t{e}.tx'.format(e=e), '{e}.html'.format(e=output_file_name),
                     {'model': model, 'definition': definition}, final_templates_path)


if __name__ == '__main__':
    main(False)
