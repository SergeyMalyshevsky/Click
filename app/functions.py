import qrcode
from .models import Url
from click.settings import MEDIA_URL


def generate_url(domain, long_url):
    '''
    Function generate short URL and image with QR-code
    '''
    if len(long_url) < 256:
        if Url.objects.filter(long_url=long_url).exists():
            url = Url.objects.get(long_url=long_url)
            char_array = url.short_path
        else:
            url = Url.objects.create(long_url=long_url)
            number = url.id
            char_array = generate_string(number)
            url.short_path = char_array
            url.save()

        short_url = ''.join(['http://', domain, '/', char_array])
        img = generate_qr_code(short_url, char_array)
    else:
        short_url = long_url
        img = ""

    return short_url, img


def generate_string(number):
    '''
    Function generate short string for short URL
    '''
    result = ""
    char_array = "1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    char_array_length = len(char_array)

    remainder = number
    while number > char_array_length:
        remainder = number % char_array_length
        number = number // char_array_length
        result += char_array[remainder - 1]

    result += char_array[remainder - 1]
    return result[::-1]


def generate_qr_code(url, name):
    '''
    Function generate QR-code from input URL
    '''
    img_format = '.png'
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)
    img = qr.make_image()
    filename = ''.join([MEDIA_URL, name, img_format])

    try:
        img.save(filename)
    except Exception:
        print("System cannot save file {}".format(filename))

    return filename
