

class Foo:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def show(self):
        print "%s age is %s"%(self.name, self.age)

    def __call__(self):
        self.show()

    def __getitem__(self,test):
        test +=2017
        return test

    def __setitem__(self, key, value):
        # self[key] = value
        """
          File "cmofa.py", line 19, in __setitem__
    self[key] = value
RuntimeError: maximum recursion depth exceeded while calling a Python object
        """

        print (key,value)
    
f1 = Foo("tom",21)
f1()

print f1[1000]

f1["n"] =3



class DictDemo:
    def __init__(self, key,value):
        self.dict ={}
        self.dict[key] =  value

    def __getitem__(self,key):
        return self.dict[key]

    def __setitem__(self,key,value):
        self.dict[key] = value

d1 =DictDemo("tom",21)

print d1["tom"]

d1["jack"] = 31
print d1["jack"]

