import os

from generated.base_generator import BaseGenerator
from root import BASE_PATH


class PlayGenerator(BaseGenerator):
    def __init__(self, model):
        BaseGenerator.__init__(self, model)
        pass
    
    @staticmethod
    def init_folder_structure(folder_list):
        for folder in folder_list:
            if not os.path.exists(folder):
                os.makedirs(folder)
                

    # @staticmethod
    #  def init_folder_structure(base_path, templates_path, final_templates_path):
    #     if not os.path.exists(base_path):
    #        os.makedirs(base_path)
    #
    #   if not os.path.exists(templates_path):
    #      os.makedirs(templates_path)
    #
    # if not os.path.exists(final_templates_path):
    #    os.makedirs(final_templates_path)

    def generate_application(self):
        # path to django templates
        base_source_path = os.path.join('play_templates')
        
        # path to the target folder
        base_path = os.path.join(BASE_PATH, self.model.name)
        play_class_html_path = os.path.join(base_path, self.model.name, 'play_class_html')
        folder_gen_list = [base_path,
                           play_class_html_path]

        # create the folders
        self.init_folder_structure(folder_gen_list)
        self.generate_play_class_html(base_source_path, play_class_html_path)

    def generate_play_class_html(self, base_source_path, play_class_html_path):
        # list of template files
        file_gen_list = {'login_play', 'logout_play'}

        # generate the template files
        for e in file_gen_list:
            self.generate(base_source_path + '/templates' + '/play_class_html' + '/t{e}.tx'.format(e=e),
                          '{e}.html'.format(e=e), {'model': self.model}, play_class_html_path)    

