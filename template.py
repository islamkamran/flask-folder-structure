# automating the whole process of doing the folder structure of flask

import os
from pathlib import Path

PORJECT_NAME = "flask-folder-structure"

LIST_FILES = [
    "Dockerfile",
    ".env",
    ".gitignore",
    "app.py",
    "init_setup.py",
    "README.md",
    "requirements.txt",
    "src/__init__.py",
    
    # files inside src file
    
    # 1- Config file for configuration
    "src/config/__init__.py",
    "src/config/config.py",
    "src/config/dev_config.py",
    "src/config/production_config.py",

    # 2- Controller of the Application
    "src/controllers/__init__.py",
    "src/controllers/auth_controller.py",

    # 3- Middlewares

    "src/middlewares/__init__.py",

    # 4- Model of the Application
    "src/models/__init__.py",
    "src/models/user_model.py",

    # 5- Servies
    "src/services/__init__.py",
    "src/services/jwt-service.py",

    # 6- Routes and Utilities(Utils) in main src folder
    "src/routes.py",
    "src/utils.py",
]

# now performing the magic

for file_path in LIST_FILES:
    file_path = Path(file_path)
    file_dir, file_name = os.path.split(file_path)

    # first make the directory

    if file_dir!="":
        os.makedirs(file_dir, exist_ok=True)
        print(f"Creating Directory: {file_dir} for file: {file_name}")


    if (not os.path.exists(file_path)) or (os.path.getsize(file_path)==0):
        with open(file_path, "w") as f:
            # pass
            print(f"Creating an emtpy file: {file_path}")

    else:
        print(f"File already exists {file_path}")