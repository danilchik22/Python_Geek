import os

name_root = "myproject"
name_childrens  = ["setting", "mainapp", "adminapp", "authapp"]
if not os.path.exists(name_root):
    os.mkdir(name_root)
for name_dir in name_childrens:
    dir_path = os.path.join(name_root, name_dir)
    if not os.path.exists(dir_path):
        os.mkdir(dir_path)