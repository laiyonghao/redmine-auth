from setuptools import setup, find_packages
import sys, os

version = '0.3.0'

setup(name='redmine-auth',
      version=version,
      description="Subversion/Jenkins Authentication Through Redmine",
      long_description="""\
An apache2 authentication provider implementation, redmine database is used for authenticate. It can be used for subversion authentication, etc.
Please visit project home page for more help.
""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='apache, apache2, redmine, auth, svn, subversion',
      author='LaiYonghao',
      author_email='mail@laiyonghao.com',
      url='https://github.com/laiyonghao/redmine-auth',
      license='MIT',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          # -*- Extra requirements: -*-
          'argparse',
          'sqlalchemy',
      ],
      entry_points="""
      # -*- Entry points: -*-
      [console_scripts]
      redmine-auth = redmineauth.main:main
      redmine-auth-jenkins = redmineauth.jenkins:main
      """,
      )
