n,m=map(int,input().split())

a=list(map(int,input().split()))
b=list(map(int,input().split()))
x=0
for i in range(m):
     v=list(map(str,input().split()))
     p=v[0]
     e=int(v[1])
     x=x+1
     
     if(p=='L'):
        
         for x in range(e):
                 k=a.pop(-1)
                 a.insert(0,k)
                 
                 if(a==b):
                   
                     break
    
     if(p=='R'):
        
        for x in range(e):
                 k=a.pop(0)
                 a.append(k)
                 
                 if(a==b):
                   
                     break

                 
                 
