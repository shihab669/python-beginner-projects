import qrcode

userInput = input("Enter the text or URL to generate QR code: ")

qr = qrcode.QRCode(
    box_size=20,
    border=2
)

qr.add_data(userInput)
qr.make(fit=True)

img = qr.make_image(fill_color="white", back_color="black").save("qr-code.png")

print("QR code generated and saved as 'qr-code.png'")
