# import requests
#
# info = requests.get("http://10.36.145.100:5000/v2/_catalog")
# jsoninfo = info.json()
# # print(jsoninfo)
# name = dict(jsoninfo)
# listname = name['repositories']
# for imagename in listname:
#     x='http://10.36.145.100:5000/v2/{}/tags/list'.format(imagename)
#     info2 = requests.get(x)
#     y = info2.json()
#     z = dict(y)
#     namea = z['name']
#     for tags in z['tags']:
#         nameb = namea.upper()
#         tagsb = tags.upper()
#         print("{:<20}".format('Name'),"{:>20}".format("Tags"))
#         print("{:<20}".format(nameb),"{:>20}".format(tagsb))
#
#

def image():
    import requests
    cc = ""
    info = requests.get("http://10.36.145.100:5000/v2/_catalog")
    jsoninfo = info.json()
    # print(jsoninfo)
    name = dict(jsoninfo)
    listname = name['repositories']
    for imagename in listname:
        x = 'http://10.36.145.100:5000/v2/{}/tags/list'.format(imagename)
        info2 = requests.get(x)
        y = info2.json()
        z = dict(y)
        namea = z['name']
        for tags in z['tags']:
            nameb = namea
            tagsb = tags
            # aa = ("{:<20}".format('Name'), "{:>20}".format("Tags"))
            bb = ("{:<20}".format(nameb)+"{:>20}".format(tagsb))
            # print(bb)

            cc = cc + bb + '\n'
    print(cc)
    return cc


image()