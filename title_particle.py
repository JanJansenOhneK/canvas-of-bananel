
class TitleParticle:

    def __init__(self,pos=list[float,float],vel=list[float,float],alpha=float,size=float):
        self.pos = pos
        self.vel = vel
        self.alpha = alpha
        self.size = size
    
    def frame(self):
        self.pos[0] += self.vel[0]
        self.pos[1] += self.vel[1]
        
        self.pos[0] = self.pos[0] % 700
        self.pos[1] = self.pos[1] % 700