import os

from fixtures import cwd

DOMAIN = 'http://hrm-online.portnov.com'

DEFAULT_PASSWORD = 'password'

BROWSER_TYPE = 'chrome'

# cwd was moved to the fixtures/__init__.py file because it is not a "parameter"
CHROME_EXECUTABLE_PATH = os.path.join(cwd, 'browser_drivers/chromedriver')
FIREFOX_EXECUTABLE_PATH = os.path.join(cwd, 'browser_drivers/geckodriver')

EXPLICIT_TIMEOUT = 2

# Just examples of some other waits you can add/create
# SLOW_TIMEOUT = 30
#
# FILE_UPLOAD_TIMEOUT = 120