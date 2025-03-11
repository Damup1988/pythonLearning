def summ (a,b): return a + b
def mult (a,b): return a * b
def subs (a,b): return a - b

def operation (oper,x,y):
    if oper == "sum": return summ(x,y)
    if oper == "mul": return mult(x,y)
    if oper == "sub": return subs(x,y)

print(operation("sum",2,5))
print(operation("mul",2,5))
print(operation("sub",2,5))