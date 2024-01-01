def singlton(object):
    instance={}
    @staticmethod
    def get_instance(*args):
        if object not in instance:
            instance[object]=object(*args)
        return instance[object]
    return get_instance

@singlton
class database:
    def __init__(self):
        print("loading")

if __name__=="__main__":
    d=database()
    d1=database()
    print(d==d1)


