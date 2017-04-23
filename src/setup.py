from setuptools import setup , find_packages

setup(
    name='kalkulacka',
    version='0',
    packages=find_packages('zdroj', exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
 
    entry_points={
          'console_scripts': [
              'kalkulacka = gui.kalkulacka:main'              
          ]
      },
    package_dir={'': 'zdroj/'},
    data_files=[
        ('share/applications/', ['zdroj/ikonka/kalkulacicka.desktop'])
        ]
)
