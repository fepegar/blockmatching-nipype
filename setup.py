from setuptools import setup, find_packages

setup(name='blockmatching',
      version='0.1.0',
      author='Fernando Perez-Garcia',
      author_email='fernando.perezgarcia.17@ucl.ac.uk',
      packages=find_packages(),
      install_requires=[
          'nipype',
          ],
     )
