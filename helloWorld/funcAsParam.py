def doOperation (a,b,operation): return operation(a,b)

def summ (a,b): return a + b
def mult (a,b): return a * b

x = 2
y = 3
print(doOperation(x,y,summ))
print(doOperation(x,y,mult))