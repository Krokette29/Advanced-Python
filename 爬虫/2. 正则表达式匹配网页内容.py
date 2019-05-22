from urllib.request import urlopen
import re # regular expressions


# if has Chinese, apply decode()
html = urlopen(
    "https://krokette29.github.io/Code-Lab/"
).read().decode('utf-8')
# print(html)

# 匹配标题
res = re.findall(r"<title>(.+?)</title>", html)
print("\nPage title is: ", res[0])

# 匹配段落
# re.DOTALL表示获取换行，如果不加该flags则获取不到newline，只会读取内容
res = re.findall(r"<p>(.*?)</p>", html, flags=re.DOTALL)    # re.DOTALL if multi line
print("\nPage paragraph is: ", res[:5])

# 匹配链接
res = re.findall(r'href="(.*?)"', html)
print("\nAll links: ", res)