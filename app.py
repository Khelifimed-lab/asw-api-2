from flask import Flask, request, send_file
import cv2
import numpy as np
import io

app = Flask(__name__)

# هذا المشروع يحمل اسم: PENCIL SHADOW 2
# تم تثبيت قيمة التأثير على الحد الأقصى (20)

@app.route('/sketch', methods=['POST'])
def sketch():
    img_array = np.frombuffer(request.data, np.uint8)
    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    
    if img is None:
        return "Invalid image", 400

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    inv = 255 - gray

    # Gaussian Blur ثابت يمثل أعلى قيمة للتأثير = 20 → kernel = 21x21
    blur = cv2.GaussianBlur(inv, (21, 21), 0)

    sketch = cv2.divide(gray, 255 - blur, scale=256)
    _, buf = cv2.imencode('.png', sketch)
    return send_file(io.BytesIO(buf), mimetype='image/png')