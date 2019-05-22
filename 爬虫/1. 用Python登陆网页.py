from urllib.request import urlopen

# if has Chinese, apply decode()
html = urlopen(
    "https://krokette29.github.io/Code-Lab/"
).read().decode('utf-8')
print(html)