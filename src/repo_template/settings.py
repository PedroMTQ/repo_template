import os
import tomllib
from importlib.metadata import version

ROOT = os.path.abspath(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
PYPROJECT_PATH = os.path.join(ROOT, 'pyproject.toml')


with open(PYPROJECT_PATH, 'rb') as f:
    data = tomllib.load(f)
    SERVICE_NAME = data['project']['name']

DEBUG = int(os.getenv('DEBUG', '0'))



DATA = os.path.join(ROOT, 'data')
TEMP = os.path.join(ROOT, 'tmp')
TESTS = os.path.join(ROOT, 'tests')
TESTS_DATA = os.path.join(TESTS, 'data')
CONFIG = os.path.join(ROOT, 'config')
CODE_VERSION = version(SERVICE_NAME)
