
n1=0
n2=1
n3=0
opc = 0 

opc = int(input("Digite um número:"))

while(n1 < opc):
  print(n1,"," ,end=" ")
  n1 = n2+n3
  n3=n2
  n2=n1
  
  
else:
  print(opc,"....")
