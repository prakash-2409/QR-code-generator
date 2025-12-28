from flask import Flask, render_template, request
import base64
from io import BytesIO
import qrcode

app = Flask(__name__)


def build_qr(data: str) -> str:
    """Return a base64-encoded PNG for the provided data."""
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_M,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    buffer = BytesIO()
    img.save(buffer, format="PNG")
    buffer.seek(0)
    return base64.b64encode(buffer.getvalue()).decode("ascii")


@app.route("/", methods=["GET", "POST"])
def index():
    img_data = None
    url_value = request.form.get("url", "")
    if request.method == "POST" and url_value.strip():
        img_data = build_qr(url_value.strip())
    return render_template("index.html", img_data=img_data, url_value=url_value)


if __name__ == "__main__":
    app.run(debug=True)

