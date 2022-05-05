#python 3.7.1
def encr(s,k):
  s1=[]
  for i in s:
    s1.append(i)
  s2=[]
  while(len(s1)!=0):
    l=[]
    while(len(l)!=len(k)):
      if(len(s1)==0):
        l.append("*")
      else: 
        l.append(s1.pop(0))
    s2.append(l)
 # print(s2)
  en=[]
  for li in s2:
    t=[]
    for j in k:
      if(li[j-1]=="*"):
        continue
      t.append(li[j-1])
    en.append("".join(t))
  print("".join(en))
def decr(e,k):
  s1=[]
  for i in e:
    s1.append(i)
  s2=[]
  while(len(s1)!=0):
    l=[]
    while(len(l)!=len(k)):
      if(len(s1)==0):
        l.append("*")
      else: 
        l.append(s1.pop(0))
    s2.append(l)
  de=[]
  for li in s2:
    t=[]
    if("*" in li):
      ind=li.index("*")
      m=min(k[ind:])
      while(li.count("*")!=0):
        li.remove("*")
      k[len(li)-1]=m
      k=k[:len(li)]
    z=zip(k,li)
    z=sorted(z)
    for x,y in z:
      t.append(y)
    de.append("".join(t))
  print("".join(de))   
s=input("Enter a string to encrypt:")
k=input("Enter comma separated key list:").split(",")
k=list(map(int,k))
encr(s,k)
e=input("Enter a string to decrypt:")
decr(e,k)


    
    