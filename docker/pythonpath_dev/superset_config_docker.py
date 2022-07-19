from customAuth import CustomSecurityManager
import os
# Additional config
WEBDRIVER_BASEURL = os.environ.get('WEBDRIVER_BASEURL')
SECRET_KEY = os.environ.get('SECRET_KEY')
SESSION_COOKIE_SAMESITE = os.environ.get('SESSION_COOKIE_SAMESITE')
SESSION_COOKIE_SECURE = os.environ.get('SESSION_COOKIE_SECURE')

# The limit of queries fetched for query search
QUERY_SEARCH_LIMIT = os.environ.get('QUERY_SEARCH_LIMIT')

# Flask-WTF flag for CSRF
WTF_CSRF_ENABLED = os.environ.get('WTF_CSRF_ENABLED')

# Branding
APP_NAME = os.environ.get('APP_NAME')
# Specify the App icon
APP_ICON = os.environ.get('APP_ICON')
APP_ICON_WIDTH = os.environ.get('APP_ICON_WIDTH')
# ---------------------------------------------------
# Babel config for translations
# ---------------------------------------------------
# Setup default language
BABEL_DEFAULT_LOCALE = os.environ.get('BABEL_DEFAULT_LOCALE')

#Custom Security manager
JWT_SECRET = os.environ.get('JWT_SECRET')
JWT_ALG = ['HS256']
CUSTOM_SECURITY_MANAGER = CustomSecurityManager

MAPBOX_API_KEY = os.environ.get('MAPBOX_API_KEY')
