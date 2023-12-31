class TV:
    canal=1
    volumen=1
    precio=500
    numTv=0

    def __init__(self, marca, estado):
        self.marca=marca
        self.estado=estado
        TV.numTv+=1

    def setMarca(self,marca):
        self.marca=marca

    def setCanal(self, canal):
        if self.estado==True:
            if canal>=1 and canal<=120:
                self.canal=canal

    def setPrecio(self, precio):
        self.precio=precio
    def setVolumen(self, vol):
        if self.estado==True:
            if vol>=0 and vol<=7:
                self.volumen=vol

    def setControl(self, control):
        self.control=control
    @staticmethod
    def setNumTV(num):
        TV.numTv=num
    
    def getMarca(self):
        return self.marca
    def getCanal(self):
        return self.canal
    def getPrecio(self):
        return self.precio
    def getVolumen(self):
        return self.volumen
    def getControl(self):
        return self.control
    @staticmethod
    def getNumTV():
        return TV.numTv
    
    def getEstado(self):
        return self.estado
    def turnOn(self):
        if (self.estado!=True):
            self.estado=True
    def turnOff(self):
        if (self.estado==True):
            self.estado=False

    def canalUp(self):
        if self.estado==True:
            if self.canal<120:
                self.canal+=1
    def canalDown(self):
        if self.estado==True:
            if self.canal>1:
                self.canal-=1

    def volumenUp(self):
        if self.estado==True:
            if self.volumen<7:
                self.volumen+=1
    def volumenDown(self):
        if self.estado==True:
            if self.volumen>0:
                self.volumen-=1