import os

PWD = os.path.abspath(os.curdir)

SITE_TITLE = 'Andalucia Developers: Jobs'
SITE_DESCRIPTION = 'Tablón de anuncios de ofertas de trabajo'
SITE_GITHUB_TITLE = 'Andalucia Developers'
SITE_GITHUB_URL = ''

SITE_EMAIL = 'admin@andaluciadev.com'
SITE_TELEGRAM_TITLE = 'Andalucia Developers'
SITE_TELEGRAM_URL = 'https://t.me/andaluciadev'


SQLALCHEMY_DATABASE_URI = 'sqlite:///{}/dbase.db'.format(PWD)
SQLALCHEMY_TRACK_MODIFICATIONS = False
