class Reusable:
    def test(self):
        return f'the id is {id(self)}'
    

class ReusablePool:
    def __init__(self,size):
        self.size=size
        self.free=[]
        self.in_use=[]

        for _ in range(size):
            self.free.append(Reusable())

    
    def aquire(self)->Reusable:
        if(len(self.free)<=0):
            raise Exception("no object is created")
        else:
            r=self.free[0]
            self.free.remove(r)
            self.in_use.append(r)
            return r
    
    def release(self,r):
        self.in_use.remove(r)
        self.free.append(r)


if __name__=="__main__":
    pool=ReusablePool(2)
    r=pool.aquire()
    print(r.test())
    r1=pool.aquire()
    print(r1.test())
    print(r1.test())
    pool.release(r1)
    r2=pool.aquire()
    print(r2.test)


