# Question 1  Please translate the comments in this program into your own language
# မေးခွန်း ၁  ကျေးဇူးပြု၍ ဒီပရိုဂရမ်ထဲက မှတ်ချက်တွေကို မင်းရဲ့ဘာသာစကားကို ဘာသာပြန်ပေးပါ။
# प्रश्न १ कृपया यस कार्यक्रममा टिप्पणीहरूलाई तपाईंको आफ्नै भाषामा अनुवाद गर्नुहोस्।
# 问题 1 请将此程序中的注释翻译成您自己的语言。
# প্রশ্ন ১ অনুগ্রহ করে এই প্রোগ্রামের মন্তব্যগুলি আপনার নিজের ভাষায় অনুবাদ করুন।
# Асуулт 1 Энэ програм дахь тайлбаруудыг өөрийн хэл рүү орчуулна уу.
# Câu hỏi 1 Vui lòng dịch các nhận xét trong chương trình này sang ngôn ngữ của bạn.
# Вопрос 1 Пожалуйста, переведите комментарии в этой программе на ваш родной язык

"""
This program creates a beautiful Tkinter window with multiple widgets.
The widgets' background colors change randomly every 500 milliseconds.
The widgets include labels, entries, and buttons, each displaying "Hello" in different languages.

Author: momokita
Created with: Github Copilot
Creation Date: 2023-10-05
"""

#Welcome to GitHub Copilot Programming World

import tkinter as tk
import random

# Function to change colors of all widgets
def change_colors():
    colors = ["red", "green", "blue", "yellow", "purple", "orange", "pink", "cyan"]
    # Iterate through each widget and change its background color
    for widget in widgets:
        color = random.choice(colors)
        widget.config(bg=color)
    # Schedule the function to run again after 500 milliseconds
    root.after(500, change_colors)

# Create the main window
root = tk.Tk()
root.title("Beautiful Tkinter Program")

# Set window size and center it on the screen
window_width = 800
window_height = 600
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
position_top = int(screen_height / 2 - window_height / 2)
position_right = int(screen_width / 2 - window_width / 2)
root.geometry(f"{window_width}x{window_height}+{position_right}+{position_top}")

# Create a list to store widgets
widgets = []

# Texts for "Hello" in different languages
hello_texts = [
    "こんにちは",  # Japanese
    "မင်္ဂလာပါ",  # Burmese (Myanmar)
    "Xin chào",  # Vietnamese
    "你好",  # Chinese
    "नमस्ते",  # Nepali
    "Сайн байна уу",  # Mongolian
    "হ্যালো",  # Bengali
    "안녕하세요"  # Korean
]

# Create and place multiple widgets
for i, text in enumerate(hello_texts):
    label = tk.Label(root, text=text, font=("Helvetica", 16), width=15, height=2)
    label.grid(row=i, column=0, padx=10, pady=10)
    widgets.append(label)

for i, text in enumerate(hello_texts):
    entry = tk.Entry(root, font=("Helvetica", 16), width=15)
    entry.grid(row=i, column=1, padx=10, pady=10)
    widgets.append(entry)

for i, text in enumerate(hello_texts):
    button = tk.Button(root, text=text, font=("Helvetica", 16), width=15, height=2)
    button.grid(row=i, column=2, padx=10, pady=10)
    widgets.append(button)

# Start changing colors
change_colors()

# Start the main loop
root.mainloop()