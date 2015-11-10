from PIL import Image
import zbarlight
import cv2

file_path = 'sample2.png'

with open(file_path, 'rb') as image_file:
    image = Image.open(image_file)
    image.load()

cvImage = cv2.imread(file_path)
edges = cv2.Canny(cvImage,100,200)
print(type(edges))

codes = zbarlight.scan_codes('qrcode', image)
print('QR codes: %s' % codes)