class Home:
    def __init__(self,area):
        self.area=area
        self.space=[]
    def __str__(self):
        msg="hemo is rea is....."+str(self.area)
        return msg
    def containItem(self,item):
        bedArea=item.getBedArea()
        if self.area>bedArea:
            self.space.append(item)
            self.area-=bedArea
            print('添加物品%s成功,还剩余%d'%(item.getBedName(),self.area))
        else:
            print("error you %s is too big too put it in yur home"%item.getBedName())


class Bed:
    def __init__(self,name,area):
        self.name=name
        self.area=area
    def __str__(self):
        msg='my bed area is'+str(self.area)
        return msg
    def getBedArea(self):
        return self.area
    def getBedName(self):
        return self.name
home=Home(800)
#home.containItem(bed)
bed=Bed('json',4)
home.containItem(bed)
bed2=Bed('sb',10)
home.containItem(bed2)
bed3=Bed('zairenjian',3000)
home.containItem(bed3)


print(home)
print(bed)