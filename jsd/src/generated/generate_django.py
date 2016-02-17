import os

from generated.base_generator import BaseGenerator
from root import BASE_PATH, ROOT_DIR


class DjangoGenerator(BaseGenerator):
    def __init__(self, model):
        BaseGenerator.__init__(self, model)
        pass

    def typeDef(self, typedef):
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

    @staticmethod
    def init_folder_structure(folder_list):
        for folder in folder_list:
            if not os.path.exists(folder):
                os.makedirs(folder)

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

        folder_gen_list = [base_path,
                           app_path,
                           program_path,
                           templates_path,
                           final_templates_path,
                           registration_path]

        # create the folders
        self.init_folder_structure(folder_gen_list)
        self.copy_assets_folder(assets_source_path, assets_path)
        self.generate_program_files(base_source_path, program_path)
        self.generate_templates(base_source_path, final_templates_path)
        self.generate_registration_files(base_source_path, registration_path)
        self.generate_app_files(base_source_path, app_path)
        self.generate_root_html(base_source_path, root_html_path)

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
        file_gen_list = {'logged_out', 'login'}

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

    def copy_assets_folder(self, assets_folder, assets_path):
        import distutils.core
        distutils.dir_util.copy_tree(assets_folder, assets_path)