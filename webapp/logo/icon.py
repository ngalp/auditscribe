from PIL import Image
import requests
from io import BytesIO

response = requests.get('https://github.com/ngalp/auditscribe/blob/main/webapp/logo/icon.ico?raw=true')
icon =Image.open(BytesIO(response.content))