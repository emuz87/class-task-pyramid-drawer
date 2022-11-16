from math import floor 
def takeOddNum(str):
    inp = int(input(str))
    return inp if inp%2!=0 else takeOddNum(str)
def takeSym(str):
    inp = input(str)
    return inp if len(inp) < 2 else takeSym(str) 
def draw(sym, n):
    return (n+1)*" "+sym+"\n"+"\n".join([(n-v)*" "+sym+((2*v)+1)*" "+sym for v in range(floor(n/2)-1)])+"\n"+(floor(n/2)+2)*" "+n*sym
print(draw(takeSym("Enter symbol: "), takeOddNum("Enter odd number: ")))