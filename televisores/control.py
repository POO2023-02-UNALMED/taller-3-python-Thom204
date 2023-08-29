from televisores.tv import TV
class Control:
    def __init__(self):
        pass
    def enlazar(self, TV):
        self.TV=TV
        TV.setControl(self)
    
    def turnOn(self):
        self.TV.turnOn()
    def turnOff(self):
        self.TV.turnOff()
    def canalUp(self):
        self.TV.canalUp()
    def canalDown(self):
        self.TV.canalDown()
    def volumenUp(self):
        self.TV.volumenUp()
    def volumenDown(self):
        self.TV.volumenDown()
    
    def setCanal(self,canal):
        self.TV.setCanal(canal)
    def setVolumen(self,volumen):
        self.TV.setVolumen(volumen)
    
    def setTv(self, tv):
        self.TV=tv
    def getTv (self):
        return self.TV