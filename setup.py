from setuptools import find_packages,setup
from typing import List

Hypen_e_Dot='-e .'
def get_requirements(file_path:str)->List[str]:

    '''
    This function will return list of requirements
    '''

    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()

        requirements=[req.replace("\n","" ) for req in requirements]

        if Hypen_e_Dot in requirements:
            requirements.remove(Hypen_e_Dot)
    return requirements        

setup(
    name='mlproject',
    version='0.01',
    author='subash',
    author_email='subashchella15@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)