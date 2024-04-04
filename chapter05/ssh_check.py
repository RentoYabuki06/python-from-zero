import ssl
import urllib.request as req

# SSL証明書の検証を有効にする
context = ssl.create_default_context()

# URLにアクセスしてみる
try:
    res = req.urlopen("https://www.google.com", context=context)
    print("SSL証明書の検証に成功しました")
except Exception as e:
    print("SSL証明書の検証に失敗しました:", e)
