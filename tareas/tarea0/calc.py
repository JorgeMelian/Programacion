from tkinter import N

n1 = int(input("Primer numero: "))
n2 = int(input("Segundo numero: "))

print (str(n1)+"+"+str(n2)+"="+str(n1+n2),
 str(n1)+"-"+str(n2)+"="+str(n1-n2),
  str(n1)+"*"+str(n2)+"="+str(n1*n2),
   str(n1)+"/"+str(n2)+"="+str(n1/n2),
   sep='\n')