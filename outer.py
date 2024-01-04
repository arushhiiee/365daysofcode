def outer_fun(who):
    def inner_fun():
        print('hello',who)
    inner_fun()
outer_fun('xyz')
inner_fun()
#hello xyz 
#when you call outer fun youre also creating a local scope
#the core feature of the inner function is their ability to access variables and objects
#from their enclosing functions.
#recurrsion when a function calls itself

def fact(num):
    if num==1:
        return 1
    else:
        return (num*fact(num-1))
print(fact(34))


 
