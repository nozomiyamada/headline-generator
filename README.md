# Headline Generator

generate "headline" (ประมาณ 20-4 คำ) จาก description ของข่าว โดยใช้ seq2seq

## Introduction
seq2seq เป็นวิธีหนึ่งที่เปลี่ยน time series data เป็น time series data อีกอย่างหนึ่ง

การประยุคใช้ของ seq2seq มีจำนวนมาก เช่น
- Machine Translation
- Text Summarization
- Chatbot
- Automatic Email Reply

โครงการนี้เป็น Text Summarization ชนิดหนึ่ง

## Method
ข้อมูล : ข่าวไทยรัฐ 8 ปีที่ผ่านมา ทั้งหมด 5 แสนกว่าบทความ

โมเดลที่จะใช้ : single layer LSTM, multi layer BiLSTM, Attension

### Model 1: single layer LSTM
model for training
![mono2](https://user-images.githubusercontent.com/44984892/57869145-9aa76080-782e-11e9-8a93-39922bd04d26.png)

model for generating
![mono1](https://user-images.githubusercontent.com/44984892/57869139-9713d980-782e-11e9-91e7-1e8b4ca6fc8b.png)

## Result

## Discussion
