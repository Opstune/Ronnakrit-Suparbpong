#โปรแกรมรับค่าคะแนน ถ้ามากกว่า 60 ขึ้นไป แต่น้อยกว่า 100 ให้แสดงคำว่า .ผ่าน
#ถ้ารับค่าน้อยกว่า 60 ให้แสดงคำว่า "ไม่ผ่าน"
score = int(input("ป้อนค่าคะแนน:"))
if(score >= 60 and score <= 100):
    print("ผ่าน")
else:
    print("ไม่ผ่าน")
    