# 今回集計するデータ
s = """
 サンマ ,  カツオ ,  サンマ ,  マグロ ,  サーモン,  イワシ,  イワシ,  サーモン , マグロ ,  マグロ ,  イワシ ,  マグロ
 """

s = s.strip()
s_list = s.split(",")

result = {}
for name in s_list:
    name = name.strip()
    if not name in result:
        result[name] = 0
    result[name] += 1;

for name, v in result.items():
    print(name + " = " + str(v))
