class GPCM:
   
    def __init__ (self, semilla,a,c,m):
        self.semilla = semilla
        self.a = a
        self.c = c
        self.m = m
    
    def generate(self):
        self.semilla = (self.a * self.semilla + self.c)%self.m
        return self.semilla/self.m

    
   