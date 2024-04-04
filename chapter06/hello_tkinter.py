from tkinter import *

# ウィンドウ生成
win = Tk()

# 描画のためキャンバスを作成
cv = Canvas(win, width = 400, height = 300)

# ウィンドウ全体に載せる
cv.pack()

# メインループを実行
win.mainloop()
