import requests
from bs4 import BeautifulSoup

url1='https://URL/path/to/submit.php'
myobj1= 'username=johndoe&get_captcha=antidos' # this post request gets captcha image in base64 in response, different URL in every case
y = requests.post(url1, data = myobj1, verify=False) 
#print(y.text)

soup = BeautifulSoup(y.text)
imgstring = soup.find('image_data').string #extracting base64 string in <image_data> tag of xml response to convert to image file, you need to do differently if response is in html
filename = 'captcha.jpg' 

import base64
imgdata = base64.b64decode(imgstring)

with open(filename, 'wb') as f:
    f.write(imgdata)  #save img file

try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
def ocr_core(filename):
    """
    This function will handle the core OCR processing of images.
    """
    text = pytesseract.image_to_string(Image.open(filename))  # We'll use Pillow's Image class to open the image and pytesseract to detect the string in the image
    return text

print(ocr_core('captcha.jpg')) # reads image captcha and displays in text

url = 'https://URL/path/to/submit/for/captcha/bypass.php'
myobj = 'param1=value1&user=johndoe&password=password&captchaText='+ocr_core('captcha.jpg')+'+&anotherparam=anothervalue2&etc=etc' #actual post request that bypass captcha image and posts the value of captcha
x = requests.post(url, data = myobj,  verify=False) # request after decoding of captcha img to text
print(x.text) # prints server msg response after submitting captcha request.
