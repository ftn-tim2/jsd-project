import os

from base_generator import BaseGenerator
from root import BASE_PATH


class DjangoGenerator(BaseGenerator):
    def __init__(self, model):
        BaseGenerator.__init__(self, model)
        pass

    @staticmethod
    def init_folder_structure(base_path, templates_path, final_templates_path):
        if not os.path.exists(base_path):
            os.makedirs(base_path)

        if not os.path.exists(templates_path):
            os.makedirs(templates_path)

        if not os.path.exists(final_templates_path):
            os.makedirs(final_templates_path)

    def generate_application(self):
        # path to django templates
        base_source_path = os.path.join('django_templates')

        # path to the target folder
        base_path = os.path.join(BASE_PATH, self.model.name)
        templates_path = os.path.join(base_path, 'templates')
        final_templates_path = os.path.join(templates_path, self.model.name)

        # create the folders
        self.init_folder_structure(base_path, templates_path, final_templates_path)

        file_gen_list = {'__init__', 'models', 'views', 'urls', 'admin', 'tests'}
        template_file_gen_list = {'class_confirm_delete', 'class_form', 'class_list'}

        # generate the basic files
        for e in file_gen_list:
            self.generate(os.path.join(base_source_path, 't{e}.tx'.format(e=e)), '{e}.py'.format(e=e),
                          {'model': self.model},
                          base_path)

        # generate the template files
        for definition in self.model.classes:
            for e in template_file_gen_list:
                output_file_name = e.replace('class', definition.name.lower())
                self.generate(os.path.join(base_source_path, 'htmltemplates', 't{e}.tx'.format(e=e)),
                              '{e}.html'.format(e=output_file_name), {'model': self.model, 'definition': definition},
                              final_templates_path)
