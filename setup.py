from setuptools import setup,find_packages
from typing import List



# Declaring variable for setup function
PROJECT_NAME = "housing_predictor"
VERSION = "0.0.1"
AUTHOR = "Shashir Gornal"
DESRCIPTION = "This is my housing project"
#PACKAGES = ["housing"]
REQUIREMENT_FILE_NAME = "requirements.txt"


"""
This below function is going to return the list of requirements mention in the requirements.txt
"""

def get_requirements_list()->List[str]:

    with open(REQUIREMENT_FILE_NAME) as requirement_file :
        return requirement_file.readlines().remove("-e .")
    




setup(
    name=PROJECT_NAME,
    version=VERSION,
    author=AUTHOR,
    description=DESRCIPTION,
    packages=find_packages(),
    install_requires = get_requirements_list() 
)