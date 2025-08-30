from collections import defaultdict
def game(arr,m):
    def anna(arr):
        new_arr=[]
        lenn=0
        for i in arr:
            count=0
            while i%10==0:
                count+=1
                lenn+=1
                i=i//10
            while i>0:
                lenn+=1
                i=i//10
            if count!=0:
                new_arr.append(count)

        return new_arr,lenn
    new_arr,count=anna(arr) 
    # return len(k)-temp
    # return anna(arr)
    
    new_arr.sort()
    new_arr=new_arr[::-1]
    for i in range(len(new_arr)):
        if i%2==0:
            count-=new_arr[i]
    # return new_arr
    if count>m:
        return 'Sasha'
    return 'Anna'
 
t=int(input())
final=[]
for i in range(t):
    n,m=map(int,input().split())
    arr=list(map(int,input().split()))
    
    final.append(game(arr,m))
    # print(game(arr,m))
for i in final:
    print(i)
        
        


        
