
# 1-m
class Odam:
    def __init__(self,ism,yosh):
        self.ism = ism
        self.yosh = yosh

    def salom(self):
        print("Salom,")

class Talaba(Odam):
        def salom(self):
            print("Salom, men talaba")


o1 = Odam("Ali", 20)
t1 = Talaba("Vali", 22)


o1.salom()
t1.salom()


# 2-m
class Hayvon:
    def ovoz(self):
        print("Ovoz chiqardi")


class Mushuk(Hayvon):
    def ovoz(self):
        super().ovoz()
        print("Miyov")

m = Mushuk()
m.ovoz()


# 3-m
class Transport:
    def harakat(self):
        print(f'harakatlanmoqda')

class mashina(Transport):
    def harakat(self):
        super().harakat()
        print(f'mashina yurmoqda')
m = mashina()
m.harakat()

# 4-m
class kitob:
    def __init__(self,nomi,muallif):
        self.nomi = nomi
        self.muallif = muallif
    def info(self):
        print(f'kitob nomi: chiqaradi')

class darslik(kitob):
    def info(self):
        super().info()
    print(f'bu darslik')

k1 = darslik('matematika','aliyev')
k1.info()

# 5-m
class Ishchi:
    def __init__(self,ism,maosh):
        self.ism = ism
        self.maosh = maosh
    def ishla(self):
        print(f'ishlamoqda')


class dasturchi(Ishchi):
    def ishla(self):
        super().ishla()
        print(f'kod yozmoqda')
k1 = Ishchi("ali",'aliyev alisher')
k1.ishla()
