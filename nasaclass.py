class nasa:
    def __init__(self,sor):
        vag=sor.split("*")
        self.url=vag[0]
        self.date=vag[1]
        self.img=vag[2]
        self.status=vag[3].split(" ")[0]
        self.size=vag[3].split(" ")[1]
    def ByteMeret(self):
        int(self.size)
        if self.size =="-":
            return 0
        else:
            return int(self.size)