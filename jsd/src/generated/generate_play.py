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
        
        # path to the target folder
        base_path = os.path.join(BASE_PATH, self.model.name)
        play_class_html_path = os.path.join(base_path, self.model.name, 'play_class_html')
        play_model_pojo_classes_path = os.path.join(base_path, self.model.name, 'play_model_pojo_classes')
        tags_play_path = os.path.join(play_class_html_path, 'tags_play')
        folder_gen_list = [base_path,
                           play_class_html_path,
                           play_model_pojo_classes_path,
                           tags_play_path]

        # create the folders
        self.init_folder_structure(folder_gen_list)
        self.generate_play_class_html(base_source_path, play_class_html_path)
        self.generate_tags_play(base_source_path, tags_play_path)
        self.generate_play_model_bean_classes(base_source_path, play_model_pojo_classes_path)

    def generate_play_class_html(self, base_source_path, play_class_html_path):
        # list of template files
        file_gen_list = {'login_play', 'logout_play', 'change_password_play', 'list' , 'index', 'layout', 'create_Page', 'show', '404', '500' }

        # generate the template files
        for e in file_gen_list:
            self.generate(base_source_path + '/templates' + '/play_class_html' + '/t{e}.tx'.format(e=e),
                          '{e}.html'.format(e=e), {'model': self.model}, play_class_html_path)    

    def generate_tags_play(self, base_source_path, tags_play_path):
        # registration files
        file_gen_list = {'checkField', 'custom', 'dateField', 'enumField', 'fileField', 'form', 'hiddenField',
                         'longtextField', 'navigation', 'numberField', 'pagination', 'passwordField', 'relationFiled',
                         'search', 'serializedField', 'table', 'textField'}

        # generate the basic files
        for e in file_gen_list:
            self.generate(base_source_path +'/templates' + + '/play_class_html' + '/tags_play' + '/t{e}.tx'.format(e=e),
                          '{e}.html'.format(e=e), {'model': self.model}, tags_play_path)
            
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


    def generate_play_model_bean_classes(self, base_source_path, play_model_pojo_classes_path):
        # list of template files
        # file_gen_list = "classname.java"

        prepared_classes = self.prepare_play_data_model()

        # generate the template files
        for clazz_key, clazz_value in prepared_classes.items():
            # output_file_name = file_gen_list.replace('class', definition.name)

            self.generate(base_source_path + '/templates' + '/' + 'play_model_pojo_classes' + '/tmodel_play.tx',
                          '{classname}.java'.format(classname=clazz_key),
                          {'clazz': clazz_value}, play_model_pojo_classes_path)


