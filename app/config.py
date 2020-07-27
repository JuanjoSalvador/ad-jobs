import os

PWD = os.path.abspath(os.curdir)

SITE_TITLE = 'Andalucia Developers: Jobs'
SITE_DESCRIPTION = 'Tablón de anuncios de ofertas de trabajo'

SQLALCHEMY_DATABASE_URI = 'sqlite:///{}/dbase.db'.format(PWD)
SQLALCHEMY_TRACK_MODIFICATIONS = False
