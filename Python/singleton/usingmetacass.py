class Singleton(type):
    _instance={}
    def __call__(cls,*args,**kwargs):
        if(cls not in cls._instance):
            cls._instance[cls]=super(Singleton,cls).__call__(*args,**kwargs)
        return cls._instance[cls]
    
    

class Logger(metaclass=Singleton):
    def log(self,msg):
        print(msg)


if __name__=="__main__":
    l=Logger()
    l.log('hello')
    l1=Logger()
    l1.log("bye")
    print(l==l1)




