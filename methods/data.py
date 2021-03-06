#!python3
import tokenz

class MethodInputError(Exception): pass
class VariableError(Exception): pass

data = {}

def var(args):
    if args[0].type == "ident" and (args[1].type != "call"):
        data[args[0].val] = args[1]
    else:
        raise MethodInputError("Incorrect type of arguments for function: %s & %s" % (str(args[0].type), str(args[1].type)) )
    
    return tokenz.Token("None", None)

def get(args):
    if hasattr(args[0], 'id'):
        try:
            return data[args[0].id] # Token obj
        except KeyError:
            raise VariableError("Attempt to get value of undefined variable %s" % args[0].id)
    else:
        raise MethodInputError("Incorrect type of arguments for function: %s" % str(args[0].type))
        return tokenz.Token("None", None)

class Data:
    def __init__(self):
        self.methods = ["var", "get"]
        self.banned = ["get"] # Do not allow through the prompt
        self.funcs = [var, get]
