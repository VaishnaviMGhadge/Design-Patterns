def singlton(class1):
    instance={}
    def get_instance(*args,**kwargs):
        if class1 not in instance:
            instance[class1]=class1(*args,**kwargs)
        return instance[class1]
    return get_instance



@singlton
class Database:
    def __init__(self):
        print("loading....")

if __name__=='__main__':
    d1=Database()
    d2=Database()
    print(d1==d2)


