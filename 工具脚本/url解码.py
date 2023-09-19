import urllib.parse

encoded_str = "%7B%E7%BB%9F%E4%B8%80%E8%B5%84%E6%BA%90%E5%AE%9A%E4%BD%8D%E7%AC%A6%E7%BC%96%E7%A0%81%7D"
decoded_str = urllib.parse.unquote(encoded_str, encoding='utf-8')
print(decoded_str)