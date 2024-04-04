quiz_list = [
    #[ 問題, 選択肢1,選択肢2, 選択肢3, 答え]
    ["スターバックス1号店の場所は？", "シアトル", "ニューヨーク", "ロサンゼルス", 1 ],
    ["世界遺産に登録されていないのは？", "屋久島", "宮島", "松島", 3],
    ["リニアモーターカー(大阪-東京)が通過しない予定なのは？", "京都府", "静岡県", "岐阜県", 1],
    ["将棋にも全く動きがおなじコマがあるのは？", "クイーン", "ナイト", "ビショップ", 3]
]

import random
random.shuffle(quiz_list)

for quiz in quiz_list:
    print("[問題]")
    print(quiz[0])
    for i in range(3):
        no = i + 1
        print(str(no) + ": " + quiz[no])
    user = int(input(" 答えは何番？："))
    ans = quiz[4]
    if user == ans:
        print("\n>>>>>>> 正解です〜！！")
    else:
        print("\n>>>>>>> ハズレ、、答えは：" + quiz[ans])
    print("\n---------------")
