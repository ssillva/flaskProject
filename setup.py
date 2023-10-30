from setuptools import setup, find_packages

requires = [
	'flask',
	'flask-sqlalchemy',
	'psycopg2',
]

setup(
	name='flaskProject',
	version='1.0',
	description='Trabalho Final Flask Sistema Controle de Estoque',
	author='<Sandro Oliveira>',
	author_email='<sandro2007am@gmail.com>',
	keywords='web flask',
	packages=find_packages(),
	include_package_data=True,
	install_requires=requires
)