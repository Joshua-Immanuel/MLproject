from setuptools import find_packages,setup
from typing import List

hifenedot='-e .'
def get_requirements(filename)->List[str]:

   requiremets=[]
   with open(filename) as file_obj:
      requiremets=file_obj.readlines()
      requiremets=[req.replace('\n','') for req in requiremets]
      
   if  hifenedot in requiremets:
      requiremets.remove(hifenedot)

   return requiremets

setup(
    name='mlproject',
    version='0.0.1',
    author="Joshua",
    author_email="joshuawarrior567@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)