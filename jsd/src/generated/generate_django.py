import distutils.core
import os

from generated.base_generator import BaseGenerator
from root import BASE_PATH, ROOT_DIR


class DjangoGenerator(BaseGenerator):
    def __init__(self, model):
        BaseGenerator.__init__(self, model)
        pass

    def typeDef(self, typedef):
        type_list = ['bigInteger', 'binary', 'boolean', 'char', 'commaSeparatedInteger', 'date', 'dateTime', 'decimal',
                     'duration', 'email', 'file', 'filePath', 'float', 'image', 'nullBoolean', 'positiveInteger',
                     'positiveSmallInteger', 'slug', 'smallInteger', 'text', 'time', 'URL', 'UUID',
                     'manyToMany', 'oneToOne']
        if typedef in type_list:
            return typedef.title() + 'Field'

        type_list_special_case = ['int', 'foreignKey']
        if typedef in type_list_special_case:
            if typedef == 'int':
                return 'IntegerField'
            if typedef == 'foreignKey':
                return 'ForeignKey'
        else:
            raise NameError('Unsupported typeDef was found : ' + typedef)

    @staticmethod
    def init_folder_structure(folder_list):
        for folder in folder_list:
            if not os.path.exists(folder):
                os.makedirs(folder)

    @staticmethod
    def copy_assets_folder(assets_folder, assets_path):
        distutils.dir_util.copy_tree(assets_folder, assets_path)

    @staticmethod
    def copy_necessary_files(necessary_source_path, base_path):
        distutils.dir_util.copy_tree(necessary_source_path, base_path)

    @staticmethod
    def call_post_gen_script(base_path):
        os.chdir(base_path)
        os.system('python3.5 ./manage.py migrate')
        os.system('python3.5 ./manage.py collectstatic --noinput')
        # os.system('python ./manage.py runserver')

    def generate_application(self):
        # path to django templates
        base_source_path = os.path.join('django_templates')

        # path to the target folder
        base_path = os.path.join(BASE_PATH, self.model.name)

        app_path = os.path.join(base_path, 'apps')
        program_path = os.path.join(base_path, self.model.name)
        templates_path = os.path.join(base_path, self.model.name, 'templates')
        final_templates_path = os.path.join(templates_path, self.model.name)
        registration_path = os.path.join(templates_path, 'registration')

        root_html_path = templates_path
        assets_path = os.path.join(base_path, 'assets')
        assets_source_path = os.path.join(ROOT_DIR, 'src', 'generated', 'templates', base_source_path, 'assets')
        necessary_source_path = os.path.join(ROOT_DIR, 'src', 'generated', 'templates', base_source_path,
                                             'necessary_files')

        folder_gen_list = [base_path,
                           app_path,
                           program_path,
                           templates_path,
                           final_templates_path,
                           registration_path]

        # create and copy
        self.init_folder_structure(folder_gen_list)
        self.copy_assets_folder(assets_source_path, assets_path)
        self.copy_necessary_files(necessary_source_path, base_path)

        # generate files
        self.generate_program_files(base_source_path, program_path)
        self.generate_templates(base_source_path, final_templates_path)
        self.generate_registration_files(base_source_path, registration_path)
        self.generate_app_files(base_source_path, app_path)
        self.generate_root_html(base_source_path, root_html_path)

        # post gen events
        self.call_post_gen_script(base_path)

    def generate_program_files(self, base_source_path, program_path):
        # program files
        file_gen_list = {'__init__', 'models', 'views', 'urls', 'admin', 'tests'}

        # generate the basic files
        for e in file_gen_list:
            self.generate(base_source_path + '/program' + '/t{e}.tx'.format(e=e), '{e}.py'.format(e=e),
                          {'model': self.model}, program_path)

    def generate_templates(self, base_source_path, final_templates_path):
        # list of template files
        template_file_gen_list = {'class_confirm_delete', 'class_form', 'class_list'}

        # generate the template files
        for definition in self.model.classes:
            for e in template_file_gen_list:
                output_file_name = e.replace('class', definition.name.lower())
                self.generate(base_source_path + '/program' + '/templates' + '/class_html' + '/t{e}.tx'.format(e=e),
                              '{e}.html'.format(e=output_file_name), {'model': self.model, 'definition': definition},
                              final_templates_path)

    def generate_registration_files(self, base_source_path, registration_path):
        # registration files
        file_gen_list = {'login', 'registration_form', 'registration_complete', 'password_change_form',
                         'password_change_done'}

        # generate the basic files
        for e in file_gen_list:
            self.generate(base_source_path + '/program' + '/templates' + '/registration' + '/t{e}.tx'.format(e=e),
                          '{e}.html'.format(e=e), {'model': self.model}, registration_path)

    def generate_app_files(self, base_source_path, app_path):
        # program files
        file_gen_list = {'__init__', 'settings', 'views', 'urls', 'wsgi'}

        # generate the basic files
        for e in file_gen_list:
            self.generate(base_source_path + '/apps' + '/t{e}.tx'.format(e=e), '{e}.py'.format(e=e),
                          {'model': self.model}, app_path)

    def generate_root_html(self, base_source_path, root_html_path):
        # registration files
        file_gen_list = {'base', 'index'}

        # generate the basic files
        for e in file_gen_list:
            self.generate(base_source_path + '/program' + '/templates' + '/t{e}.tx'.format(e=e),
                          '{e}.html'.format(e=e), {'model': self.model}, root_html_path)
