import os
from distutils.dir_util import copy_tree

my_project = r"C:\Users\111\Desktop\Python_geek\lesson7\my_project"
for root, dirs, files in os.walk(my_project, topdown=False):
    for dir in dirs:
        if dir == "templates":
            print(os.path.join(root, dir))
            from_directory = os.path.join(root, dir)
            to_directory = "templates"
            copy_tree(from_directory, to_directory)
