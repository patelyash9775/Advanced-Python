class Change:
    def __init__(self,x,y,z):
        self.a=x+y+z
        
x=Change(1,2,3)
y=getattr(x,'a')
setattr(x,'a',y+1)
print(x.a)