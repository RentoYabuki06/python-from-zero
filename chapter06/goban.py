from tkinter import *

# ウィンドウを作成
win = Tk()

 # 描画のためキャンパスを作成
cv = Canvas(win, width = 380, height = 380)

# ウィンドウ全体に載せる
cv.pack()

# 碁盤を描画する
for i in range(19):
    y = i * 20
    cv.create_line(0, y, 380, y, fill="black", width=2)
    x = i * 20
    cv.create_line(x, 0, x, 380, fill="black", width=2)
# メインループを実行
win.mainloop()
