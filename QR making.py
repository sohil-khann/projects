# this code is for simple qr code//

import qrcode as qr

img=qr.make("https://www.youtube.com/@glauniversity2879")

img.save("GLA_UNIVERSITY_youtube.png")


# /**************************************************************************
# **************************************************************************
# **************************************************************************/

# here start the colourfull qrcode


import qrcode
from PIL import Image

qr=qrcode.QRCode(version=1,
                 error_correction=qrcode.constants.ERROR_CORRECT_H,
                 box_size=10,border=4,)

qr.add_data("https://glauniversity.in:8085/Main/Index")
qr.make(fit=True)

img=qr.make_image(fill="pink",back_color="violet")
img.save("GLA_UNIVERSITY.png")

