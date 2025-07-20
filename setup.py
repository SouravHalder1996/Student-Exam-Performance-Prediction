from setuptools import setup, find_packages
from typing import List


HYPHEN_E_DOT = '-e .'
def get_requirements(file_path: str) -> List[str]:
    """
    This function reads a requirements file and returns a list of packages.
    """
    requirements = []
    with open(file_path, 'r') as file:
        requirements = file.readlines()
        requirements = [req.replace("\n", "").strip() for req in requirements]
    
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)

    return requirements


setup(
    name='Student-Exam-Performance-Prediction',
    version='0.0.1',
    author='Sourav Halder',
    author_email='halder.sourav1996@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)