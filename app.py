# from flask import Flask, render_template, Response
# import cv2

# app = Flask(__name__)
# camera = cv2.VideoCapture(0)  # เปิดเว็บแคม

# def gen_frames():
#     while True:
#         success, frame = camera.read()  # อ่านภาพจากเว็บแคม
#         if not success:
#             break
#         else:
#             ret, buffer = cv2.imencode('.jpg', frame)
#             frame = buffer.tobytes()
#             yield (b'--frame\r\n'
#                    b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')  # ส่งภาพเป็น stream

# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route('/video_feed')
# def video_feed():
#     return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

# if __name__ == '__main__':
#     app.run(debug=True)




from flask import Flask, render_template, Response
import cv2

app = Flask(__name__)

# เปิดเว็บแคม
camera = cv2.VideoCapture(0)

# โหลดตัวตรวจจับใบหน้าจาก OpenCV (Haar Cascade)
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

def gen_frames():
    while True:
        success, frame = camera.read()  # อ่านภาพจากเว็บแคม
        if not success:
            break
        else:
            # แปลงภาพเป็นขาวดำเพื่อใช้ในการตรวจจับใบหน้า
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            # ตรวจจับใบหน้า
            faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

            # วาดสี่เหลี่ยมล้อมรอบใบหน้าที่ตรวจพบ
            for (x, y, w, h) in faces:
                cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')  # ส่งภาพเป็น stream

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video_feed')
def video_feed():
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(debug=True)

