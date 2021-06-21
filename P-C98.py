def Swapper() :
    print('swap the data in your files')
    file1=input('file name 1? ')
    file2=input('file name 2? ')
    o1=open(file1,'r')
    o2=open(file2,'r')
    d1=o1.read()    
    d2=o2.read()
    w1=open(file1,'w')
    w1.write(d2) 
    w2=open(file2,'w')  
    w2.write(d1)

Swapper()