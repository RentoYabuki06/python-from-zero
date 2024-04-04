import requests

url = "https://weather.tsukumijima.net/api/forecast/city/400040"

try:
    response = requests.get(url)
    response.raise_for_status()  # エラーチェック

    data = response.json()

    # 結果を表示
    for row in data["forecasts"]:
        label = row["dateLabel"]
        telop = row["telop"]
        print(label + " : " + telop)

except Exception as e:
    print("エラー:", e)
