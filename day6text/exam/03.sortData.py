import json


# 3.请将上述生成的两个字典,按照其中的出现次数进行从大到小排序？
addContent = []
with open(file='../txtFile/sanguo.txt', mode='r', encoding='utf8') as file:
    for lines in file.readlines():
        content = json.loads(lines)
        a = dict(sorted(content.items(), key=lambda x: x[1], reverse=True))
        addContent.append(a)

# with open(file='../txtFile/sanguo.txt', mode='a', encoding='utf8') as file:
#     file.write("\n")
#     json.dump(addContent, file, ensure_ascii=False)
#
