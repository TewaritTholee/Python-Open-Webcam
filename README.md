# การตรวจจับใบหน้าจากเว็บแคมด้วย Flask และ Microsoft Azure Face API

โปรเจกต์นี้เป็นเว็บแอปพลิเคชัน Flask ที่สตรีมวิดีโอสดจากเว็บแคม ทำการตรวจจับใบหน้าโดยใช้ Microsoft Azure Face API และแสดงผลวิดีโอพร้อมข้อมูลการตรวจจับใบหน้า เช่น เพศ และอายุ
(ปล. ในที่นี่คุณต้องไปโหลด API และ สมัคร Microsoft Azure Face API เพิ่มครับ)

## ความต้องการเบื้องต้น

ก่อนเริ่มต้น โปรดตรวจสอบให้แน่ใจว่าคุณได้ติดตั้งสิ่งต่อไปนี้ในระบบของคุณ:

- Python 3.x
- pip (ตัวติดตั้งแพ็กเกจของ Python)
- เว็บแคมที่เชื่อมต่อกับเครื่องของคุณ
- บัญชี Microsoft Azure พร้อมทรัพยากร Face API

## การติดตั้ง

**โคลนโปรเจกต์จาก GitHub:**

https://github.com/TewaritTholee/Python-Open-Webcam.git


python -m venv venv
source venv/bin/activate  # บน Windows: venv\Scripts\activate

(ปล. ของผมจะเป็นการ py แล้วตามหลังด้วยคำสั่งต่าง ๆ ในการรันโปรเจคต์ python)

## ติดตั้งแพ็กเกจ Python ที่จำเป็น:
pip install -r requirements.txt

## หมายเหตุ: ตรวจสอบให้แน่ใจว่า requirements.txt มีแพ็กเกจดังต่อไปนี้:
Flask==2.1.1
opencv-python==4.5.5.64
requests==2.27.1
(แล้วแต่เวอร์ชั่นครับ)


subscription_key = "YOUR_AZURE_FACE_API_KEY"
endpoint = "YOUR_AZURE_FACE_API_ENDPOINT"


## เริ่มต้นแอปพลิเคชัน Flask:
python app.py

port : http://127.0.0.1:5000/




