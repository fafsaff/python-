class Beizi:
    __cle = ""
    __brand = 0 #高度
    __num = 0 #容量
    __color = ""#颜色
    __byk = ""#材质

    def setHigh(self,brand):
        if brand > 0 and brand < 10:
            self.__brand = brand
        else:
            print("杯子过高或过矮")
    def getHigh(self):
        return self.__brand

    def setnum(self,num):
        if num > 0 and num < 500:
            self.__num = num
        else:
            print("这个杯子的容量是多少")
    def getnum(self):
        return self.__num

    def setcolor(self,color):
            self.__color = color
    def getcolor(self):
        return self.__color

    def setdyk(self, byk):
        self.__byk = byk
    def getdyk(self):
        return self.__byk


    def run(self):
        print(self.__cle,"中国制造",self.__brand,self.__num,self.__color,self.__byk)


wc = Beizi()

wc.setHigh(int(input("请输入水杯的高度，单位是厘米：")))
wc.setnum(int(input("请输入水杯的容量，单位是毫升：")))
wc.setcolor(input("请输入水杯的颜色："))
wc.setdyk(input("请输入水杯的材质："))

wc.run()



