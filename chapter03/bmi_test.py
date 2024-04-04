# 体重と身長の入力
weight = float(input("体重は何キログラムですか？"))
height = float(input("身長は何センチですか？"))

#bmi

bmi = weight / (height / 100 ) ** 2
print("your bmi is " + str(int(bmi)))

if bmi < 18.5:
    print("痩せ型")
elif bmi >= 25:
    print("肥満")
else:
    print("普通の体型")
