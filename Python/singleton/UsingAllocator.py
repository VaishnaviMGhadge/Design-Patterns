import random
class Database:
    _instance=None
    def __new__(cls,*args,**kwargs):
        if cls._instance==None:
            cls._instance=super().__new__(cls,*args,**kwargs)
        return cls._instance
    
    def __init__(self):
        id=random.randint(1,10)
        print("the initilization is going to be done",id)
    
if __name__=="__main__":
    d1=Database()
    d2=Database()
    print(d1==d2)
    print(id(d1))
    print(id(d2))



    # using allocator you're using the __new__ method to create or construct the object only once but 
    # when we inilialize the obejct at that that time it is instantiating two times and it is violating the singlton rule 
    #

    ## find the better way !!!!!!!!!!!!!!!!!!!!:(
