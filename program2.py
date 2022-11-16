from math import floor

class Validator():
    def __init__(self, msg, err, cast_fn, cond_fn):
        self.msg = msg
        self.err = err
        self.cast_fn = cast_fn
        self.cond_fn = cond_fn
    
    def try_input(self):
        raw_input = input(self.msg)
        try: casted = self.cast_fn(raw_input)
        except: raise TypeError("That is the wrong type.")
        if self.cond_fn(casted):
            return casted
        raise Exception(self.err)
    
    def yield_until_valid(self):
        value = None
        while not value:
            try:
                value = self.try_input()
            except Exception as e:
                print(e)
        return value
        
class OddNumberValidator(Validator):
    def __init__(self):
        super().__init__(
            "Please enter an odd number: ",
            "That was not an odd number.",
            int, lambda x: x%2!=0
        )

class SymbolValidator(Validator):
    def __init__(self):
        super().__init__(
            "Please enter one symbol: ",
            "That was not one symbol.",
            str, lambda x: len(x) == 1
        )

class Drawer():
    def __init__(self, sym, n):
        self.sym = sym
        self.n = n
    
    def draw(self):
       return (self.n+1)*" "+self.sym+"\n"+\
            "\n".join([(self.n-v)*" "+self.sym+((2*v)+1)*" "+self.sym for v in range(floor(self.n/2)-1)])+\
                "\n"+(floor(self.n/2)+2)*" "+self.n*self.sym 

drawer = Drawer(
    SymbolValidator().yield_until_valid(),
    OddNumberValidator().yield_until_valid()
)
print(drawer.draw())