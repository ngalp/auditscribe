from PIL import Image
import requests
from io import BytesIO

response = requests.get('https://github.com/ngalp/auditscribe/blob/main/webapp/logo/logo.png?raw=true')
logo =Image.open(BytesIO(response.content))