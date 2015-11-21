from PIL import Image
import zbarlight
import cv2


def decodeQR(file_path):
    """(str) -> str
    Returns the string obtained by decoding the QR image located at file_path
    """

    with open(file_path, 'rb') as image_file:
        image = Image.open(image_file)
        image.load()

    codes = zbarlight.scan_codes('qrcode', image)
    return str(codes)

