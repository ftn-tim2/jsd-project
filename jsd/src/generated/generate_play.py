import os

from generated.base_generator import BaseGenerator
from root import BASE_PATH


class PlayGenerator(BaseGenerator):
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

