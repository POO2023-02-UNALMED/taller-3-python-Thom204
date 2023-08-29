class TV:
    canal=1
    volumen=1
    precio=500
    _numTv=0

    def __init__(self, marca, estado):
        self.marca=marca
        self.estado=bool(estado)
        TV._numTv+=1

    def setMarca(self,marca):
        self.marca=marca
    def setCanal(self, canal):
        self.canal=canal
    def setPrecio(self, precio):
        self.precio=precio
    def setVolumen(self, volumen):
        self.volumen=volumen
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
        if (self.estado):
            self.estado=False

    def canalUp(self):
        if self.canal<120 and self.estado:
            self.canal+=1
    def canalDown(self):
        if self.canal>0 and self.estado:
            self.canal-=1

    def volumenUp(self):
        if self.volumen<7 and self.estado:
            self.volumen+=1
    def volumenDown(self):
        if self.volumen>1 and self.estado:
            self.volumen-=1