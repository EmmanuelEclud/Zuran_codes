import qrcode

# Text to convert into QR
text = "HELLO WORLD!"

# Create the QR code
qr = qrcode.QRCode(
    version=1,  
    # QR size (1 is the smallest)
    error_correction=qrcode.constants.ERROR_CORRECT_L,  
    # Error correction level
    box_size=10,  
    # Size of each QR box
    border=4  
    # Border around the QR
)

qr.add_data(text)
qr.make(fit=True)

# Generate the QR image
img = qr.make_image(fill="black", back_color="white")

# Save the image
img.save("qrcode.png")

print("QR generated.")
