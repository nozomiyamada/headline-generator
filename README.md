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
- headine: 72.7MB
- description: 237.9MB

โมเดลที่จะใช้ : single layer LSTM, multi layer BiLSTM with attention

### Model 1: single layer LSTM
model for training
![mono2](https://user-images.githubusercontent.com/44984892/57869145-9aa76080-782e-11e9-8a93-39922bd04d26.png)

model for generating
![mono1](https://user-images.githubusercontent.com/44984892/57869139-9713d980-782e-11e9-91e7-1e8b4ca6fc8b.png)

## Result

## Discussion
