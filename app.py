import openai
import time
import os
import joblib
import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv

def load_keywords_from_file(file_path):
    keywords = []
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            keyword = line.strip()  
            keywords.append(keyword)
    return keywords

# Thay thế YOUR_OPENAI_API_KEY bằng API key của bạn từ trang OpenAI
openai.api_key = '19082001'

def generate_response(prompt):
    response = openai.Completion.create(
        engine="text-davinci-002",  # Chọn một phiên bản của mô hình ngôn ngữ
        prompt=prompt,
        max_tokens=150,  # Giới hạn số từ trong câu trả lời
        temperature=0.7,  # Điều chỉnh sự sáng tạo của câu trả lời (0.0 đến 1.0)
        stop=None  # Dừng sinh câu trả lời khi gặp stop token
    )

    return response.choices[0].text.strip()

def search_bookingcare(keyword):
    # Thực hiện tìm kiếm trên trang http://bookingcare.vn
    search_result = f"Tìm kiếm thông tin về '{keyword}' tại http://bookingcare.vn"
    return search_result

def main():
    print("Chào bạn! Tôi là chatbot tìm kiếm thông tin về bệnh viện, phòng khám và bác sĩ.")
    print("Bạn có thể nhập 'Thoát' bất cứ lúc nào để kết thúc cuộc trò chuyện.")
    
    while True:
        user_input = input("Bạn: ")
        
        if user_input.lower() == 'thoát':
            print("Cảm ơn bạn đã sử dụng dịch vụ của chúng tôi. Hẹn gặp lại!")
            break

        # Gửi prompt đến API và nhận câu trả lời
        prompt = f"Câu giao tiếp\n{user_input}"
        response = generate_response(prompt)

        # Tìm kiếm thông tin trên http://bookingcare.vn nếu câu trả lời chứa từ khóa
        with open('keywords.txt', 'r') as file:
            keywords = file.read().split('\n')

        for keyword in keywords:
            if keyword.lower() in response.lower():
                search_result = search_bookingcare(keyword)
                print("Chatbot:", search_result)
                break
        else:
            print("Chatbot:", response)

if __name__ == "__main__":
    main()
