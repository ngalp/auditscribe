from PIL import Image

from utils.utils import get_project_root

icon = Image.open(get_project_root() / "webapp" / "logo" / "logo.png?raw=true")