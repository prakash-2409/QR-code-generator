from project.app import app


if __name__ == "__main__":
    app.run(debug=True)
url=input("Enter URL to convert to QR code: ")
img=qrcode.make(url)
img.save("qrcode.png")
print("QR code saved as qrcode.png")


project/
 ├─ app.py
 ├─ templates/
 │    └─ index.html

