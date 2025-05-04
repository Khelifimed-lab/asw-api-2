
from flask import Flask, request, send_file
import cv2
import numpy as np
import io

app = Flask(__name__)

@app.route('/sketch', methods=['POST'])
def sketch():
    img_array = np.frombuffer(request.data, np.uint8)
    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)

    if img is None:
        return "Invalid image", 400

    pencil_shadow = request.headers.get("Pencil-Shadow", 2)
    try:
        pencil_shadow = int(pencil_shadow)
    except ValueError:
        pencil_shadow = 2

    pencil_shadow = max(0, min(pencil_shadow, 20))
    blur_value = max(1, pencil_shadow * 2 + 1)

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    inv = 255 - gray
    blur = cv2.GaussianBlur(inv, (blur_value, blur_value), 0)
    sketch = cv2.divide(gray, 255 - blur, scale=256)

    _, buf = cv2.imencode('.png', sketch)
    return send_file(io.BytesIO(buf), mimetype='image/png')
