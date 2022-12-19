import qrcode

def qrcode_generator():
    qr = qrcode.QRCode(version=1,
                       error_correction=qrcode.constants.ERROR_CORRECT_L,
                       box_size=20,
                       border=2)
    
    qrcd = input("Please enter data. ")
    qr.add_data(qrcd)
    qr.make(fit=True)

    img_name = input("Please enter image name. ")
    img = qr.make_image()
    img.save(img_name+".jpg")

qrcode_generator()