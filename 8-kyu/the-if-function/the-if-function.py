from collections.abc import Callable
def _if(arg,f1: Callable ,f2: Callable):    
  return f1() if arg else f2()        
print(_if(False, lambda: 4 * 4, lambda: 4 + 4))