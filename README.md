# jsd-project

The main entry point to the generator is located in the following path : <br>
https://github.com/ftn-tim2/jsd-project/blob/master/jsd/src/generated/generate.py

> if __name__ == '__main__': <br>
> main(False, 'play')

Changing this parameter would determine whether you want to generate *play* application or *django* application.

The following file provides a sample code to the DSL language which describes the model of the web applications:
https://github.com/ftn-tim2/jsd-project/blob/master/jsd/src/model/test.rbt

# Django application

After executing the generate.py a new folder should appear named : output, in which the generated application will be created.
If the sample DSL code was not changed the newly created folder name will be "jsd_app_name" and the database folder will be "jsd_app_name_db".

In the folder "jsd_app_name" the django application is generated alongside with a Dockerfile which can be built into an image using the following command :
> docker build -t imageName .

The database Dockerfile is also ready to be built into a docker image. The database image is a MySQL image.
Please note that the django application expecing the backend to be located at the following settings:
jsd_app_name/apps/settings.py

DATABASES = {
    'default': {
        'NAME': 'jsd_app_name_db',
        'ENGINE': 'django.db.backends.mysql',
        'USER': 'admin',
        'PASSWORD': 'admin',
        'HOST': '10.0.2.15', #docker machine ip
        'PORT': '3306',
        'OPTIONS': {
          'autocommit': True,
        },
    }
}

This should be further configurated to meet the needs of the user.
If the user whishes not to use Docker for developing the application, the user should follow the Dockerfile to set up all necessary tools.

# Play application
