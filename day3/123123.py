with open(file='./txtFile/access_log',mode='r+',encoding='utf8') as file:
    content = file.readlines()

    #取出所有ip
    all_ip=[]
    all_ip_number ={}
    for element in content:
        ip = element.split("-")[0].strip()
        all_ip.append(ip)
    all_ip_set = set(all_ip)
    print(all_ip_set)

    #算出每个ip的数量并写入字典中
    for i in all_ip_set:
        ip_number = all_ip.count(i)
        all_ip_number[i]=ip_number
    print(all_ip_number)

number = []
all_ip_number_sort = {}
for element in all_ip_number:
    number.append(element[1])
print(number)
# number.sort(reverse=1)
# print(number)
