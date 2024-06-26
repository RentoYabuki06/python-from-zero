import datetime

# 特定の日付から東京オリンピックまでの日付を調べる関数

def calc_days(y, m, d) :
    olympic = datetime.datetime(2020, 7, 24).timestamp()
    target = datetime.datetime(y, m, d).timestamp()
    perday = 24 * 60 * 60
    days = (olympic - target) // perday
    s = "{0}/{1}/{2}から{3}日後".format(y, m, d, int(days))
    print (s)

# 特定の日から何日後か調べる
calc_days(2017,12,1)
calc_days(2018,3,1)

# 今日から何日？
t = datetime.date.today()
calc_days(t.year, t.month, t.day)
