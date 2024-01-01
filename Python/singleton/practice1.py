"""class database:
    _instance=None
    def __new__(cls,*args,**kwargs):

        if(cls._instance==None):
            cls._instance=super(database,cls).__new__(cls,*args,**kwargs)

        return cls._instance
    

    def __init__(self):
        print("hello this is loading the databse")
    

if __name__=="__main__":
    d=database()
    d1=database()
    print(d==d1)
"""

def singlton(object):
    instance={}
    def get_instance(*args,**kwargs):
        if object not in instance:
            instance[object]=super(type).get_instance(object)
        return instance[object]
    return get_instance

    
@singlton
class Database:
    def __init__(self):
        print("loading....")

if __name__=="__main__":
    d=Database()
    d1=Database()
    print(d==d1)

