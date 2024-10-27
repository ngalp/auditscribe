from PIL import Image
from urllib.request import urlopen

from webapp.utils import get_project_root

icon =Image.open(urlopen('get_project_root() / "webapp" / "logo" / "logo.png?raw=true"'))