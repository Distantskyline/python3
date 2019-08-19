import json


# 1.统计kingdoms.txt中"曹操"、"刘备"、"卧龙"、"孙权"各出现的次数？并将其生成字典持久化存储
character, display = ('曹操', '刘备', '卧龙', '孙权'), {}
with open(file='../txtFile/kingdoms.txt', mode='r', encoding='utf8') as file:
    content = file.read()
    text = content.replace(" ", "").replace("\n", "")
    for c in character:
        display.setdefault(c, text.count(c))
    print(display)

with open(file='../txtFile/sanguo.txt', mode='w', encoding='utf8') as file:
    json.dump(display, file, ensure_ascii=False)
