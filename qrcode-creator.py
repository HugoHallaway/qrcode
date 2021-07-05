# 1. Open Terminal and type in : "python3 -m pip install qrcode"
# 2. You can replace "img" by the word you want ! And replace the URL of course !
# 2.1 So, you have just to put your word at the img place, at the first and seconde line !

import qrcode
img = qrcode.make('www.youtube.com')
img.show()

# Done! Now, Have fun ! Create QR Code and share them !
