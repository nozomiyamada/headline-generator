# Headline Generator

generate "headline" จาก description ของข่าว โดยใช้ seq2seq

https://colab.research.google.com/drive/1clABG38xBRoYwcy6UHBztVuB8ztDEY9f
https://colab.research.google.com/drive/1UvPUA4_BJV0UPtocC0AJvUiN3fg-xL3L

## Introduction
seq2seq เป็นวิธีหนึ่งที่เปลี่ยน time series data เป็น time series data อีกอย่างหนึ่ง

การประยุคใช้ของ seq2seq มีจำนวนมาก เช่น
- Machine Translation
- Text Summarization
- Chatbot
- Automatic Email Reply

โครงการนี้เป็น Text Summarization ชนิดหนึ่ง

## Method
ข้อมูล : ข่าวไทยรัฐ 8 ปีที่ผ่านมา ทั้งหมด 448299 บทความ ข่าวที่ scrape มามีสามส่วน: headline(~ 50คำ), description(~ 250คำ) และ เนื้อหา

ทีนี้ ใช้แค่ headline และ description เท่านั้น

ขนาดไฟล์
- headine: 69MB
- description: 227MB

โมเดลที่จะใช้ : single layer LSTM, multi layer BiLSTM with attention

total vocaburary : 57908 คำ (เอาแค่คำที่ปรากฏ 3 ครั้งขึ้นไปเท่านั้น)

train ใช้เวลานานมากเกือบเป็นวัน Google Colab จะปิด runtime โดยอัตโนมัติหลัง 90 นาที เพราะฉะนั้น ใช้ auto refresh ทุก 60 นาที

https://chrome.google.com/webstore/detail/auto-refresh/ifooldnmmcmlbdennkpdnlnbgbmfalko

### Model 1: Single Layer LSTM
model for training
![mono2](https://user-images.githubusercontent.com/44984892/57869145-9aa76080-782e-11e9-8a93-39922bd04d26.png)

model for generating
![mono1](https://user-images.githubusercontent.com/44984892/57869139-9713d980-782e-11e9-91e7-1e8b4ca6fc8b.png)

## Result
### Model 1: Single Layer LSTM with Greedy Algorithm

| input (description) | answer (headline) | output (headline) |
|:-:|:-:|:-:|
| ปิดประชุมเครือจักรภพอังกฤษ เน้นการปฏิรูป แต่ยังหาฉันทามติเรื่องสิทธิมนุษยชนได้ | ปิดประชุมเครือจักรภพ ยังขัดเรื่องสิทธิมนุษยชน |อาเล็ก' ยัน 'อาเล็ก' ยัน 'อาเล็ก' ไม่ซีเรียส 'อั้ม'|
|รมว.วัฒนธรรมตรวจสอบ โบราณสถานเขาขุนพนมเมืองคอน หลังมีสิ่งก่อสร้างใหม่เพิ่มขึ้นเรื่อยๆโดยไม่ขออนุญาต สั่งยุติการก่อสร้างตกแต่งที่อาจทำให้เอกลักษณ์และประวัติความเป็นมาแต่เดิมเปลี่ยนแปลง | รมว.วธ.รุดตรวจสอบโบราณสถานเมืองคอน |อาเล็ก' ยัน 'อาเล็ก' ยัน 'อาเล็ก' ไม่ซีเรียส 'อั้ม'|

เหมือนเป๊ะ แสดงว่า train ไม่สำเร็จหรือ Greedy Algorithm ไม่ข่วย


## Discussion
