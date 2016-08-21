from setuptools import setup

setup(name='generated',
      version='0.1',
      description='Generate some Django and Play code',
      url='https://github.com/ftn-tim2/jsd-project.git',
      author='FTN',
      author_email='ftn@ftn.com',
      license='MIT',
      packages=['generated'],
      package_dir={
            'source': '/src'
      },
      package_data={
            'source': [
                              'generated/templates/django_templates/apps/*',
                              'generated/templates/django_templates/assets/css/*',
                              'generated/templates/django_templates/assets/fonts/LigatureSymbols/*',
                              'generated/templates/django_templates/assets/img/*',
                              'generated/templates/django_templates/assets/js/vendor/*',
                              'generated/templates/django_templates/database/*',
                              'generated/templates/django_templates/necessary_files/*',
                              'generated/templates/django_templates/program/templates/class_html/*',
                              'generated/templates/django_templates/program/templates/registration/*',
                              'generated/templates/django_templates/program/templates/*.tx',
                              'generated/templates/django_templates/program/*.tx',
                              'generated/model/*.tx',
                              'generated/model/*.rbt'
                              ],
      },
      install_requires=[
      		'Arpeggio==1.2.1',
      		'Jinja2==2.8',
      		'MarkupSafe==0.23',
      		'Pillow==3.3.1',
      		'pydot',
      		'pyparsing==2.0.6',
      		'textX==0.4.2',
      		'Unipath==1.1'
      ],
      include_package_data=True,
      zip_safe=False)