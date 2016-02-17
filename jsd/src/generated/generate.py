"""
Created on 06.12.2015.

@author: xx
"""

import os

from execute.execute import execute
from generated.generate_django import DjangoGenerator
from generated.generate_play import PlayGenerator
from root import SRC_DIR


def main(debug=False, project_type='play'):
    model = execute(os.path.join(SRC_DIR, "model"), 'model.tx', 'test.rbt', debug, debug)
    if project_type == 'play':
        generator = PlayGenerator(model)
        generator.generate_application()

    if project_type == 'django':
        generator = DjangoGenerator(model)
        generator.generate_application()


if __name__ == '__main__':
    main(False, 'play')
