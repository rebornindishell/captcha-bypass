import requests
from bs4 import BeautifulSoup
url1='https://URL/path/to/submit.php'
myobj1= 'username=johndoe&get_captcha=antidos' # this post request gets captcha image in base64, username not necessary to be correct
# xmlstr is your xml in a string
y = requests.post(url1, data = myobj1, verify=False) 
#print(y.text)
soup = BeautifulSoup(y.text)
imgstring = soup.find('image_data').string #extracting base64 tag in xml to convert to image file
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
myobj = 'param1=value1&user=johndoe&password=password&captchaText='+ocr_core('captcha.jpg')+'+&anotherparam=anothervalue2&etc=etc'
x = requests.post(url, data = myobj,  verify=False) # request after decoding of captcha img to text
print(x.text) # prints server msg response after submitting captcha request.
