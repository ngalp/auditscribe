import urllib.request 
from PIL import Image 
  
urllib.request.urlretrieve( 
  'https://github.com/ngalp/auditscribe/blob/main/webapp/logo/logo.png?raw=true', 
   "logo.png") 
  
logo = Image.open("logo.png") 
