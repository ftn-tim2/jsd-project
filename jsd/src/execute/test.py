import os
import sys

print("Start cloning JSD project.")
os.system("git clone https://github.com/ftn-tim2/jsd-project.git")
print("Cloning done!")

sys.path.insert(0, '/jsd-project/jsd/src/generated/')
import generate

print("Import done successfully")


