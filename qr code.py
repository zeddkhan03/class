import qrcode

data = "Hello World! This is Kritii"

# Create QR Code
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(data)
qr.make(fit=True)

# Generate Image
img = qr.make_image(fill="black", back_color="white")
img.save("mycode.png")

print("QR Code generated successfully!")