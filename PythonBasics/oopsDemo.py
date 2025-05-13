class cal:
   n = 100
   #default constructor
   def __init__(self,a,b):
       self.fname = a
       self.lname = b
       print("hii")
   def getData(self):
       print("This is the method")
   def sum(self):
       return self.fname + self.lname + cal.n
ob=cal(1,2)
ob.getData()
print(ob.n)
print(ob.sum())
print("**************************************************")
ob1=cal(7,8)
ob1.getData()
print(ob1.n)
print(ob.sum())
print("**************************************************")