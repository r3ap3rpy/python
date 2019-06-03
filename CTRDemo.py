import requests
from collections import Counter

RNJ = "https://www.gutenberg.org/files/1513/1513-0.txt"

Result = requests.get(url=RNJ)

Text = Counter([word for word in Result.text.replace("\r\n", " ").split(" ") if word])

print(Text.most_common(n=5))
print(Text["I"])
