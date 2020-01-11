class Particle:
    def __init__(self,size,shape):
        self.size = size
        self.shape = shape

    def greet(self):
        print("hello world")

p1 = Particle("sm","round")
print(p1.size,p1.shape)