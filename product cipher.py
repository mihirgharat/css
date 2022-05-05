
def euclid_baba(x,y):
  r1,r2=x,y
  t1,t2=0,1
  r=r1%r2
  while(r!=0):
    q=r1//r2
    r=r1%r2
    t=t1-q*t2
    r1=r2
    r2=r
    t1=t2
    t2=t
  if(t1<0):
    return t1+t2
  else:
    return t1
def ceasercipher(s,k):
  D=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
  d=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
  en=""
  i=0
  for ch in s:
    if ch.isupper():
       i=D.index(ch)
       en=en+D[(i+k)%26] 
    else:
        i=d.index(ch)
        en=en+d[(i+k)%26]      
  print("encrypted word is:",en)
  de=""
  for c in en:
    if c.isupper():  
       j=D.index(c)
       de=de+D[(j-k)%26]  
    else:
       j=d.index(c)
       de=de+d[(j-k)%26]
  print("decrypted word is:",de)
  print(de)
def mulc(s,k):
  D=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
  d=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
  
  en=""
  i=0
  for ch in s:
    if ch.isupper():
       i=D.index(ch)
       en=en+D[(i*k)%26] 
    else:
        i=d.index(ch)
        en=en+d[(i*k)%26]   
  print("encrypted word is:",en)
  de=""
  j=0
  for c in en:
    if c.isupper():
       j=D.index(c)
       u=euclid_baba(26,k)
       de=de+D[(j*u)%26]  
    else:
       j=d.index(c)
       u=euclid_baba(26,k)
       de=de+d[(j*u)%26]               
  print("decrypted word is:",de)
def affine(s1,kk,k1):
  D=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
  d=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
  
  en=""
  i=0
  for ch in s1:
    if ch.isupper():
       i=D.index(ch)
       en=en+D[((i*kk)+k1)%26] 
    else:
        i=d.index(ch)
        en=en+d[((i*kk)+k1)%26]   
  print("encrypted word is:",en)
  de=""
  j=0
  for c in en:
    if c.isupper():
       j=D.index(c)
       u=euclid_baba(26,kk)
       de=de+D[((j-k1)*u)%26]  
    else:
       j=d.index(c)
       u=euclid_baba(26,kk)
       de=de+d[((j-k1)*u)%26]               
  print("decrypted word is:",de)
s=input("Enter a word:")
k=int(input("Enter key:"))
ceasercipher(s,k)
mulc(s,k)
s1=input("Enter a word(for affine):")
kk=int(input("Enter key(key 1 affine):"))
k1=int(input("Enter key(key 2 affine):"))
affine(s1,kk,k1)
    
    
    
    