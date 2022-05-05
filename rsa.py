#python 3.7.1
def isprime(num):
  f=1
  for i in range(2,int(num/2)+1):
    if(num%i==0):
      f=0
      break
  if(f==1):
    return 1
  else:
    return 0
  
def rsa(p,q,v):
  if(not(isprime(p) and isprime(q))):
    print("Sorry can't use rsa here as p and q aren't prime")
  else:
   n=p*q
   n1=(p-1)*(q-1)
   print("--- PUBLIC KEY ---")
   for i in range(2,n1):
     if(n1%i!=0):
       e=i
       break
   print("The value of public key is:",e)
   print("---Private Key---")
   k=0
   while(1):
    d=(1+(k*n1))/e
    #check=isinstance(d,int)
    if(abs(d-int(d))==0):
     print("Private key is:",int(d))
     break
    k=k+1
   print("-- ENCRYPTION --")
   c=(v**e)%n
   print("Encrypted text is:",c)
   print("-- DECRYPTION--")
   p=(c**int(d))%n
   print("Decrypted text is:",p)
p=int(input("Enter p:"))
q=int(input("Enter q:"))
v=int(input("Enter message symbol:"))
rsa(p,q,v)


  
