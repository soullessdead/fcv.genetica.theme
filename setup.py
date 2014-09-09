from setuptools import setup, find_packages
import os

version = '0.1'

setup(name='fcv.genetica.theme',
      version=version,
      description="Tema del proyecto genetica animal",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from
      # http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='tema fcv genetica luz diazo tema theme proyecto veterinaria zulia universidad',
      author='Carlos Gonzalez',
      author_email='soulless_dead@hotmail.com',
      url='https://github.com/soullessdead/fcv.genetica.theme',
      license='GPL version 2',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['fcv', 'fcv.genetica'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'z3c.jbot',
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
