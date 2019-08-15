import json


# 2.统计kingdoms.txt中"青龙偃月刀"、"丈八蛇矛"、"赤兔马"、"雌雄双股剑"各出现的次数？并将其生成字典持久化存储
arms, display = ('青龙偃月刀', '丈八蛇矛', '赤兔马', '双股剑'), {}
with open(file='../txtFile/kingdoms.txt', mode='r', encoding='utf8') as file:
    content = file.read().replace(" ", "").replace("\n", "")
    for a in arms:
        display.setdefault(a, content.count(a))
    print(display)

with open(file='../txtFile/sanguo.txt', mode='a', encoding='utf8') as file:
    file.write('\n')
    json.dump(display, file, ensure_ascii=False)
