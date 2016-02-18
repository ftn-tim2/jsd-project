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


    def annotationdef(self, annotationDef):
        if annotationDef == "ForeignKey":
            return "@OneToMany"
        elif annotationDef == "OneToOneField":
            return "@OneToOne"
        elif annotationDef == "manyToMany":
            return "@ManyToMany"

    
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
        folder_gen_list = [base_path,
                           play_class_html_path,
                           play_model_pojo_classes_path]

        # create the folders
        self.init_folder_structure(folder_gen_list)
        self.generate_play_class_html(base_source_path, play_class_html_path)
        self.generate_play_model_bean_classes(base_source_path, play_model_pojo_classes_path)

    def generate_play_class_html(self, base_source_path, play_class_html_path):
        # list of template files
        file_gen_list = {'login_play', 'logout_play', 'change_password_play'}

        # generate the template files
        for e in file_gen_list:
            self.generate(base_source_path + '/templates' + '/play_class_html' + '/t{e}.tx'.format(e=e),
                          '{e}.html'.format(e=e), {'model': self.model}, play_class_html_path)    

    def generate_play_model_bean_classes(self, base_source_path, play_model_pojo_classes_path):
        # list of template files
        # file_gen_list = "classname.java"

        # generate the template files
        for definition in self.model.classes:
            # output_file_name = file_gen_list.replace('class', definition.name)
            self.generate(base_source_path + '/templates' + '/' + 'play_model_pojo_classes' + '/tmodel_play.tx',
                          '{classname}.java'.format(classname=definition.name),
                          {'model': self.model, 'definition': definition}, play_model_pojo_classes_path)


