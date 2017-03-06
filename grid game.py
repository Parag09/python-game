import random
def check (ori_list,t):
    count=0
    l=ori_list
    for i in range(len(l)):
        if l[i]==' ':
            continue
        for j in range (i,16):
            if l[j]==' ':
                continue
            if l[j]>l[j+1]:
                count+=1
    parity=(-1)**count
    
    taxicab_distance=0
    for i in range (len(t)):
        for j in range (len(t)):
            if t[i][j]==' ':
                taxicab_distance=8-i-j
                return (parity+taxicab_distance,i,j)
def list_array(ori_list):
    x=[]
    for i in range (0,len(ori_list),4):
        x+=[ori_list[i:i+4]]
    return x
def up (l,i,j):
    if i!=3:
        l[i][j],l[i+1][j]=l[i+1][j],l[i][j]
    
def down (l,i,j):
    if i!=0:
        l[i][j],l[i-1][j]=l[i-1][j],l[i][j]
        
def right (l,i,j):
    if j!=0:
        l[i][j],l[i][j-1]=l[i][j-1],l[i][j]
def right (l,i,j):
    if j!=3:
        l[i][j],l[i][j+1]=l[i][j+1],l[i][j]


def display(l):
    for row in l:
        for tile in row:
            print(tile, end='\t')
        print()

ori_list =[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,' ']
random.shuffle(ori_list)
l = list_array(ori_list)
z,i,j=check (ori_list,l)
while z!=1:
    random.shuffle(ori_list)
    l = list_array(ori_list)
    z=check (ori_list,l)
display(l)
while l!=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,' ']]:
    character=input()
    if character == 'w':
        up(l,i,j)
    if character == 'd':
        right(l,i,j)
    if character == 'a':
        left(l,i,j)
    if character == 's':
        down(l,i,j)    
    display(l)
    
    
