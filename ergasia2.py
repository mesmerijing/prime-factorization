x=int(input("Give an integer:"))
while x > 1000000:
    x=int(input("Give another number:"))
#checks if the number given is already prime    
if x%2==1:
    print ("The number is already prime!")    
if x%2==0:
    i=0
    j=0
    k=0
    z=0
    tot=0
    #does the modification with 2
    while x%2==0 :
        x=x//2
        i+=1
    #does the modification with 3    
    while x%3==0 :
        x=x//3
        j+=1
    #does the modification with 5    
    while x%5==0 :
        x=x//5
        k+=1
    #does the modification with 7    
    while x%7==0 :
         x=x//7
         z+=1
#prints the result-the analyzation of the number       
print("The number that you gave is analyzed as: (2**" + repr(i)
      + ")(3**" + repr(j) + ")(5**" + repr(k) + ")(7**"+ repr(z)+")(" + repr(x)+")")
