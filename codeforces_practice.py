# from collections import defaultdict
# def game(arr,m):
#     def anna(arr):
#         new_arr=[]
#         lenn=0
#         for i in arr:
#             count=0
#             while i%10==0:
#                 count+=1
#                 lenn+=1
#                 i=i//10
#             while i>0:
#                 lenn+=1
#                 i=i//10
#             if count!=0:
#                 new_arr.append(count)

#         return new_arr,lenn
#     new_arr,count=anna(arr) 
#     # return len(k)-temp
#     # return anna(arr)
    
#     new_arr.sort()
#     new_arr=new_arr[::-1]
#     for i in range(len(new_arr)):
#         if i%2==0:
#             count-=new_arr[i]
#     # return new_arr
#     if count>m:
#         return 'Sasha'
#     return 'Anna'
 
# t=int(input())
# final=[]
# for i in range(t):
#     n,m=map(int,input().split())
#     arr=list(map(int,input().split()))
    
#     final.append(game(arr,m))
#     # print(game(arr,m))
# for i in final:
#     print(i)
# CDC TCS_DIGITAL TEST1 CODE
# THIS IS NOT CORRECT NUT READ THE QS PROPERLY
# def f(matt,quer):
#     dis,mn,mx=quer[0],quer[1],quer[2]
#     count=0
#     ans=[]
#     ans2=[]
#     for i,minm in matt:
#         if i<=dis and minm>=mn and minm<=mx:
#             count+=1
#             ans.append((i,minm))
#             ans2.append((minm,i))

#     # return count
#     ans.sort()
#     ans2.sort()
#     v1=ans[0]
#     v2=ans2[0][::-1]
#     if v1==v2:
#         return 1
#     return 2
# n=int(input())
# matt=[]
# for i in range(n):
#     t=list(map(int,input().split()))
#     matt.append(t)
# ans=[]
# q=int(input())
# for i in range(q):
#     quer=list(map(int,input().split()))
#     ans.append(f(matt,quer))
# for i in ans:
#     print(i)
        
'''
quesstion in companys hiring challenge 
'''
def f(arr,k):
    eve=[]
    odd=[]
    for i in arr:
        if i%2==0:
            eve.append(i%k)
        else:
            odd.append(i%k)
    # we have 2 cases here
    # both the arrs are always in the range of k ie 0-k-1
    # case 1 if sum is <k
    # c2 sum is >=k in this case we have to take the mod again so we want to deviate it most from k so that the remainder is always the greatest so in this case we take the 2nd arrs maxm val
    # in case 1 we have x+y<k so we have x,k and find y<k-x ie max val can be k-x-1 so use bs over 2nd arr to find the closest val to it
    # and directly add it
    # in case 2 again take the mod
    eve.sort()
    odd.sort()
    maxm=odd[-1]
    ans=0
    for i in eve:
        y=k-i-1
        low=0
        high=len(odd)-1
        t=-1
        while low<=high:
            mid=(low+high)//2
            if odd[mid]<=y:
                t=mid
                low=mid+1
            else:
                high=mid-1
        if t!=-1:
            ans=max(ans,odd[t]+i)
        if maxm+i>=k:
            ans=max(ans,(i+maxm)%k)
    return ans
arr=list(map(int,input().split()))
k=int(input())
print(f(arr,k))

        
