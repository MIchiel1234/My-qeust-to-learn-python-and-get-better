#
# Example file for working with classes
#
class MyClass():
    def method1(self):
        print("this is my  method1")
    
    def method2(self , somestring):
        print("method 2 in my class " + somestring)
        
class NewClass(MyClass):
    def method1(self):
        MyClass.method1(self)
        print("this is my  method1 of a new class")
    
    def method2(self , somestring):
        print("method 2 in my class the new one " + somestring)

def main():
    c = MyClass()
    c.method1()
    c.method2("this is some string")
    
    
    c2 = NewClass()
    c2.method1()
    c2.method2("This is a new new new new class")


if __name__ == "__main__":
    main()
