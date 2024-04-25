# https://platform.openai.com/docs/quickstart
# pip install --upgrade openai
my_key='YOUR_KEY' 
from openai import OpenAI
from time import sleep
import tkinter as tk
from tkinter import messagebox

tk.Tk().withdraw()  # 메인 윈도우를 숨김
client = OpenAI(my_key)

def get_completion():
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo-1106",
            messages=[
                {"role": "system", "content": "You are a poetic assistant"},
                {"role": "user", "content": "대한민국에 대해서 말해라. json"}
            ]
        )
        print(response.choices[0].message.content)
    except Exception as e:
        if e.response.status_code == 429:
            # print(f"에러 요청 한도를 초과했습니다. 잠시 후 다시 시도해 주세요.\n상세 정보: {e.response.text} ")            
            messagebox.showinfo("에러", "요청 한도를 초과했습니다. 잠시 후 다시 시도해 주세요.\n상세 정보: {}".format(e.response.text))
          
            # 예를 들어 10분 후에 다시 시도
            sleep(600)
            get_completion()
        else:
            messagebox.showerror("예상치 못한 오류", f"예상치 못한 오류가 발생했습니다: {str(e)}")

        




# API 호출 실행
get_completion()
