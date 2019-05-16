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

โมเดลที่จะใช้ : mono layer LSTM, multi layer BiLSTM, Attension


## Result

## Discussion
