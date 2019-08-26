class iteratororcheck:
    def __init__(self,parm):
        self.parm = parm

    def chcek(self):
        try:
            iter(self.parm)
            return True
        except Exception as error:
            return False


list001 = [12345678]
result = iteratororcheck(list001)
resultx = result.chcek()
print(resultx)


info = [0,1,2,3,4,5,6]
result001 =[i+2 for i in info]
print(result001)

info001 = [i for i in range(15)]
print(info001)
info002 = (i for i in range(15))
for x in info002:
    print(x)