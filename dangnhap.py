from tkinter import *

def login():
    username = username_entry.get()
    password = password_entry.get()
    
    if username == "admin" and password == "password":
        result_label.config(text="Đăng nhập thành công!")
    else:
        result_label.config(text="Sai tên đăng nhập hoặc mật khẩu!")

# Tạo cửa sổ giao diện
window = Tk()
window.title("Đăng nhập")

# Đặt kích thước của cửa sổ
window.geometry("400x600")

# Tạo frame chứa các thành phần giao diện
frame = Frame(window)
frame.pack(pady=50)

# Tạo các thành phần giao diện
username_label = Label(frame, text="Tên đăng nhập:")
username_entry = Entry(frame)
password_label = Label(frame, text="Mật khẩu:")
password_entry = Entry(frame, show="*")  # Hiển thị dấu * thay vì hiển thị mật khẩu thật
login_button = Button(window, text="Đăng nhập", command=login)
result_label = Label(window, text="")

# Định vị các thành phần giao diện
username_label.grid(row=0, column=0, padx=10, pady=5, sticky="e")
username_entry.grid(row=0, column=1, padx=10, pady=5, sticky="w")
password_label.grid(row=1, column=0, padx=10, pady=5, sticky="e")
password_entry.grid(row=1, column=1, padx=10, pady=5, sticky="w")
login_button.pack(pady=10)
result_label.pack()

# Chạy giao diện
window.mainloop()
