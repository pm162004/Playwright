
from oopsDemo import cal




class childcl(cal):
   num2 = 200


   def __init__(self):
       cal.__init__(self,8,9)
   def getComplete(self):
       return self.num2 + self.n + self.sum()


obj = childcl()
print(obj.getComplete())


