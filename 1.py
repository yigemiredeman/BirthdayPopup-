import tkinter as tk
import random

class BirthdayApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.withdraw()  # 隐藏主窗口
        self.window_count = 0
        self.max_windows = 50    # 控制总窗口数量
        self.create_window()

    def create_window(self):
        if self.window_count >= self.max_windows:
            return
            
        try:
            # 获取屏幕尺寸并生成随机位置
            screen_width = self.root.winfo_screenwidth()
            screen_height = self.root.winfo_screenheight()
            x = random.randint(0, max(0, screen_width - 300))  # 窗口宽度300
            y = random.randint(0, max(0, screen_height - 150)) # 窗口高度150
            
            # 创建子窗口
            window = tk.Toplevel(self.root)
            window.title('🎉生日快乐🎉')
            window.geometry(f'300x150+{x}+{y}')
            window.attributes('-topmost', True)  # 确保窗口在最前面
            
            # 创建渐变背景画布
            canvas = tk.Canvas(window, width=300, height=150)
            canvas.pack()
            for i in range(150):  # 垂直渐变效果
                color = f'#{int(255-i*1.7):02x}{int(215-i*1.2):02x}ff'  # 蓝紫渐变
                canvas.create_line(0, i, 300, i, fill=color, width=1)
            
            # 添加文字内容
            label = tk.Label(window, 
                           text='生日快乐！\nHappy Birthday!',
                           font=('微软雅黑', 18, 'bold'),
                           fg='#FFD700',  # 金色文字
                           bg='#4B0082') # 深紫色背景
            label.place(relx=0.5, rely=0.5, anchor='center')
            
            # 添加关闭按钮
            close_btn = tk.Button(window, text='🎂', 
                                command=window.destroy,
                                font=('Arial', 14),
                                bg='#FF69B4', fg='white')
            close_btn.place(x=260, y=5)
            
            # 自动关闭定时器
            window.after(3000, window.destroy)
            
            # 控制窗口生成频率（每0.3秒生成一个新窗口）
            self.window_count += 1
            self.root.after(300, self.create_window)

        except Exception as e:
            print(f"窗口创建失败: {e}")

if __name__ == "__main__":
    app = BirthdayApp()
    app.root.mainloop()