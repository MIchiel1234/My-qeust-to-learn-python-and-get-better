#
# Example file for working with functions
#

# define a basic function
def fun1():
    print("i am a function")

# function that takes arguments

def func2(agr1,arg2):
        print(agr1," ",arg2)


# function that returns a value
def cube(x):
    return x*x*x

# function with default value for an argument
def power(num , x=1):
    result = 1 
    for i in range(x):
        result = result * num
    return result

#function with variable number of arguments
def multi_add_args(*args):
    results = 0
    for x in args:
        results = results + x
    return results
        
    




#fun1()
#print(fun1())
#print(fun1)
#func2(10,20)
#print(cube(3))
#print(power(2,3))
#print(power(x=3,num=2))
#print(multi_add_args(4,5,10,7))