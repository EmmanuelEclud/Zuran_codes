# QR Code Generator 🖼

## 📌 Description

This is a small Python script that generates a QR code from a given text. The QR is saved as an image (`qrcode.png`) in the same folder where the script is executed.

## ⚙️ How does it work?

1. The text to be converted into a QR code is defined.
2. The QR is configured with a specific size and an error correction level.
3. The black-and-white QR code image is generated.
4. The image is saved with the name `qrcode.png`.
5. Once finished, the script prints `QR generated.` in the console.

## 🚀 Requirements

To run this script, you need to have the `qrcode` library installed. If you don’t have it, you can install it with:

```bash
pip install qrcode[pil]
```

After executing it, you will find the `qrcode.png` image in the same folder as the script.

## 🎯 Notes

- You can modify the text in the `text` variable to generate a QR code with your own content.
- If you want to change the QR code color, you can adjust the values of `fill` and `back_color` in `make_image`.

That's it! Now you can easily generate QR codes with Python. 🚀
