import os

from generated.base_generator import BaseGenerator
from root import BASE_PATH


class PlayGenerator(BaseGenerator):
    model = object

    def __init__(self, model):
        BaseGenerator.__init__(self, model)
        self.model = model;
        pass

    def typeDef(self, typedef):
        if typedef == "char":
            return "char"
        elif typedef == "int":
            return "Integer"
        elif typedef == "bigInteger":
            return "BigInteger"
        elif typedef == "binary":
            return "byte[]"
        elif typedef == "boolean":
            return "Boolean"
        elif typedef == "commaSeparatedInteger":
            return "<<PLEASE USE ANOTHER TYPE>>"
        elif typedef == "date":
            return "Date"
        elif typedef == "dateTime":
            return "Date"
        elif typedef == "decimal":
            return "BigDecimal"
        elif typedef == "duration":
            return "Integer"
        elif typedef == "email":
            return "String"
        elif typedef == "file":
            return "String"
        elif typedef == "filePath":
            return "String"
        elif typedef == "float":
            return "Float"
        elif typedef == "image":
            return "ImageIcon"
        elif typedef == "nullBoolean":
            return "<<PLEASE USE ANOTHER TYPE>>"
        elif typedef == "positiveInteger":
            return "Integer"
        elif typedef == "slug":
            return "<<PLEASE USE ANOTHER TYPE>>"
        elif typedef == "smallInteger":
            return "Short"
        elif typedef == "text":
            return "String"
        elif typedef == "time":
            return "Time"
        elif typedef == "URL":
            return "String"
        elif typedef == "UUID":
            return "UUIDField"
        else:
            return typedef


    def annotationdef(self, annotationDef):
        if annotationDef == "ForeignKey":
            return "@OneToMany"
        elif annotationDef == "OneToOneField":
            return "@OneToOne"
        elif annotationDef == "manyToMany":
            return "@ManyToMany"

    def annotation_attribute_def(self, attribute_def):
        if attribute_def == "db_column":
            return "name"
        if attribute_def == "null":
            return "nullable"
        if attribute_def == "max_length":
            return "length"
        if attribute_def == "max_digits":
            return "length"
        else:
            return attribute_def

    
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
        base_output_path = os.path.join(BASE_PATH, "PLAY")

        # path to source folders
        source_play_controllers = os.path.join(base_source_path, 'app', 'controllers')
        source_play_models = os.path.join(base_source_path, 'app', 'models')
        source_play_views = os.path.join(base_source_path, 'app', 'views')
        source_play_views_CRUD = os.path.join(base_source_path, 'app', 'views', 'CRUD')
        source_play_views_Secure = os.path.join(base_source_path, 'app', 'views', 'Secure')
        source_play_views_errors = os.path.join(base_source_path, 'app', 'views', 'errors')
        source_play_views_tags_crud = os.path.join(base_source_path, 'app', 'views', 'tags', 'crud')
        source_play_public_javascript = os.path.join(base_source_path, 'public', 'javascript')
        source_play_public_stylesheets = os.path.join(base_source_path, 'public', 'stylesheets')
        source_play_conf = os.path.join(base_source_path, 'conf')
        source_play_run = os.path.join(base_source_path)

        # path to the target folder
        output_play_controllers = os.path.join(base_output_path, 'app', 'controllers')
        output_play_models = os.path.join(base_output_path, 'app', 'models')
        output_play_views = os.path.join(base_output_path, 'app', 'views')
        output_play_views_CRUD = os.path.join(base_output_path, 'app', 'views', 'CRUD')
        output_play_views_Secure = os.path.join(base_output_path, 'app', 'views', 'Secure')
        output_play_views_errors = os.path.join(base_output_path, 'app', 'views', 'errors')
        output_play_views_tags_crud = os.path.join(base_output_path, 'app', 'views', 'tags', 'crud')
        output_play_public_javascript = os.path.join(base_output_path, 'public', 'javascript')
        output_play_public_stylesheets = os.path.join(base_output_path, 'public', 'stylesheets')
        output_play_conf = os.path.join(base_output_path, 'conf')
        output_play_run = os.path.join(base_output_path)

        folder_gen_list = [base_output_path,
                           output_play_controllers,
                           output_play_models,
                           output_play_views,
                           output_play_views_CRUD,
                           output_play_views_Secure,
                           output_play_views_errors,
                           output_play_views_tags_crud,
                           output_play_public_javascript,
                           output_play_public_stylesheets,
                           output_play_conf,
                           output_play_run]

        # create the folders
        self.init_folder_structure(folder_gen_list)
        self.generate_play_view_CRUD(source_play_views_CRUD, output_play_views_CRUD)
        # self.generate_play_view_secure(source_play_views_Secure, output_play_views_Secure)
        # self.generate_play_view_errors(source_play_views_errors, output_play_views_errors)
        self.generate_play_view_tags_crud(source_play_views_tags_crud, output_play_views_tags_crud)
        self.generate_play_view(source_play_views, output_play_views)
        self.generate_play_models_DSL(source_play_models, output_play_models)
        self.generate_play_controllers_DSL(source_play_controllers, output_play_controllers)
        self.generate_play_public_javascript(source_play_public_javascript, output_play_public_javascript)
        self.generate_play_public_stylesheet(source_play_public_stylesheets, output_play_public_stylesheets)
        self.generate_play_conf(source_play_conf, output_play_conf)
        self.generate_play_run(source_play_run, output_play_run)
        self.generate_play_app_controllers_CRUD(source_play_controllers, output_play_controllers)
        self.generate_play_models_rest(source_play_models, output_play_models)
        self.generate_play_controllers_rest(source_play_controllers, output_play_controllers)

    def generate_play_controllers_rest(self, source, output):
        # list of template files
        file_gen_list = {'Users', 'Security'}

        # generate the template files
        for e in file_gen_list:
            self.generate(os.path.join(source, 't{e}.tx'.format(e=e)),
                          '{e}.java'.format(e=e), {'classname': e}, output)

    def generate_play_models_rest(self, source, output):
        # list of template files
        file_gen_list = {'Bootstrap', 'User'}

        # generate the template files
        for e in file_gen_list:
            self.generate(os.path.join(source, 't{e}.tx'.format(e=e)),
                          '{e}.java'.format(e=e), {'model': self.model}, output)

    def generate_play_app_controllers_CRUD(self, source, output):
        # list of template files
        file_gen_list = {'CRUD'}

        # generate the template files
        for e in file_gen_list:
            self.generate(os.path.join(source, 't{e}.tx'.format(e=e)),
                          '{e}.java'.format(e=e), {'model': self.model}, output)

    def generate_play_run(self, source, output):
        # list of template files
        file_gen_list = {'run'}

        # generate the template files
        for e in file_gen_list:
            self.generate(os.path.join(source, 't{e}.tx'.format(e=e)),
                          '{e}.sh'.format(e=e), {'model': self.model}, output)

    def generate_play_conf(self, source, output):
        # list of template files
        file_gen_list = {'application.conf' , 'dependencies.yml', 'initial-data.yml', 'messages', 'routes'}

        # generate the template files
        for e in file_gen_list:
            self.generate(os.path.join(source, 't{e}'.format(e=e)),
                          '{e}'.format(e=e), {'model': self.model}, output)

    def generate_play_view_CRUD(self, source, output):
        # list of template files
        file_gen_list = {'list', 'index', 'layout', 'show', 'blank'}

        # generate the template files
        for e in file_gen_list:
            self.generate(os.path.join(source, 't{e}.tx'.format(e=e)),
                          '{e}.html'.format(e=e), {'model': self.model}, output)

    def generate_play_view_secure(self,source, output):
        # list of template files
        file_gen_list = {'login'}

        # generate the template files
        for e in file_gen_list:
            self.generate(os.path.join(source, 't{e}.tx'.format(e=e)),
                          '{e}.html'.format(e=e), {'model': self.model}, output)

    def generate_play_view_errors(self,source, output):
        # list of template files
        file_gen_list = {'404', '500'}

        # generate the template files
        for e in file_gen_list:
            self.generate(os.path.join(source, 't{e}.tx'.format(e=e)),
                          '{e}.html'.format(e=e), {'model': self.model}, output)

    def generate_play_view_tags_crud(self,source, output):
        # list of template files
        file_gen_list = {'checkField', 'custom', 'dateField', 'enumField', 'fileField', 'form', 'hiddenField',
                         'longtextField', 'navigation', 'numberField', 'pagination', 'passwordField', 'relationField',
                         'search', 'serializedField', 'table', 'textField', 'types'}

        # generate the template files
        for e in file_gen_list:
            if e == 'types':
                self.generate(os.path.join(source, 't{e}.tx'.format(e=e)),
                          '{e}.tag'.format(e=e), {'model': self.model}, output)
            else:
                self.generate(os.path.join(source, 't{e}.tx'.format(e=e)),
                          '{e}.html'.format(e=e), {'model': self.model}, output)

    def generate_play_view(self,source, output):
        # list of template files
        file_gen_list = {'logout'}

        # generate the template files
        for e in file_gen_list:
            self.generate(os.path.join(source, 't{e}.tx'.format(e=e)),
                          '{e}.html'.format(e=e), {'model': self.model}, output)

    def generate_play_public_javascript(self,source, output):
        # list of template files
        file_gen_list = {'jquery-1.5.2.min'}

        # generate the template files
        for e in file_gen_list:
            self.generate(os.path.join(source, '{e}.js'.format(e=e)),
                          '{e}.js'.format(e=e), {'model': self.model}, output)

    def generate_play_public_stylesheet(self,source, output):
        # list of template files
        file_gen_list = {'crud', 'main', 'secure'}

        # generate the template files
        for e in file_gen_list:
            self.generate(os.path.join(source, '{e}.css'.format(e=e)),
                          '{e}.css'.format(e=e), {'model': self.model}, output)

    def prepare_play_data_model(self):
        class PreparedClass:
            def __init__(self, name, prepared_attributes):
                self.name = name
                self.prepared_attributes = prepared_attributes

            name = ""
            prepared_attributes = dict()

        class PreparedAttribute:
            def __init__(self, type, name, annotation, prepared_arguments):
                self.type = type
                self.name = name
                self.annotation = annotation
                self.prepared_arguments = prepared_arguments

            type = ""
            name = ""
            annotation = ""
            prepared_arguments = dict()

        class PreparedArgument:
            def __init__(self, name, value):
                self.name = name
                self.value = value

            name = ""
            value = ""

        prepared_classes = dict()

        for clazz in self.model.classes:
            attributes = dict()

            for attribute in clazz.attributes:
                arguments = dict()
                arguments_key_value = ""

                for argument in attribute.arguments:

                    if argument.name == "db_column" or argument.name == "null" or argument.name == "max_length" or argument.name == "unique" or argument.name == "max_digits":
                        prepared_argument = PreparedArgument(argument.name, str(argument.value))
                        arguments[prepared_argument.name] = prepared_argument
                    if argument.name == "key":
                        arguments_key_value = str(argument.value)


                if attribute.type == "foreignKey":
                    prepared_attribute = PreparedAttribute(arguments_key_value, attribute.name, "@ManyToOne", arguments)
                elif attribute.type == "manyToMany":
                    prepared_attribute = PreparedAttribute(arguments_key_value, attribute.name, "@ManyToMany", arguments)
                elif attribute.type == "oneToOne":
                    prepared_attribute = PreparedAttribute(arguments_key_value, attribute.name, "@OneToOne", arguments)
                else:
                    prepared_attribute = PreparedAttribute(attribute.type, attribute.name, "@Column", arguments)

                attributes[prepared_attribute.name] = prepared_attribute

            prepared_class = PreparedClass(clazz.name, attributes)
            prepared_classes[prepared_class.name] = prepared_class

        for class_key, class_value in prepared_classes.items():
            for attribute_key, attribute_value in class_value.prepared_attributes.items():
                if attribute_value.annotation == "@ManyToOne":
                    related_class = prepared_classes.get(attribute_value.type)
                    related_class.prepared_attributes[class_value.name] = PreparedAttribute("List<" + class_value.name + ">", class_value.name.lower() + "s", "@OneToMany", {"mappedBy" : PreparedArgument("mappedBy", "\"" + related_class.name + "\"")})
                elif attribute_value.annotation == "@ManyToMany":
                    related_class = prepared_classes.get(attribute_value.type)
                    related_class.prepared_attributes[class_value.name] = PreparedAttribute("List<" + class_value.name + ">", class_value.name.lower() + "s", "@ManyToMany-generated ", {"mappedBy" : PreparedArgument("mappedBy", "\"" + related_class.name + "\"")})
                elif attribute_value.annotation == "@OneToOne":
                    related_class = prepared_classes.get(attribute_value.type)
                    related_class.prepared_attributes[class_value.name] = PreparedAttribute(class_value.name, class_value.name.lower(), "@OneToOne-generated", {"mappedBy" : PreparedArgument("mappedBy", "\"" + related_class.name + "\"")})

        return prepared_classes


    def generate_play_models_DSL(self, source, output):
        # list of template files
        # file_gen_list = "classname.java"

        prepared_classes = self.prepare_play_data_model()

        # generate the template files
        for clazz_key, clazz_value in prepared_classes.items():
            # output_file_name = file_gen_list.replace('class', definition.name)

            self.generate(os.path.join(source, 'tmodel_play.tx'),
                          '{classname}.java'.format(classname=clazz_key),
                          {'clazz': clazz_value}, output)

    def generate_play_controllers_DSL(self, source, output):
            # list of template files
            # file_gen_list = "classname.java"

            prepared_classes = self.prepare_play_data_model()

            # generate the template files
            for clazz_key, clazz_value in prepared_classes.items():
                # output_file_name = file_gen_list.replace('class', definition.name)

                self.generate(os.path.join(source, 'tcontroller_play.tx'),
                              '{classname}s.java'.format(classname=clazz_key),
                              {'clazz': clazz_value}, output)
