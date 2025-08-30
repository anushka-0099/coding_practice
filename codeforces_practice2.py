# class Node:
#     # making a constructor
#     def __init__(self,data):
#         self.data=data
#         self.left=None
#         self.right=None
# def buildbst(root,data):
#     if root==None:
#         root=Node(data)
#         return root
#     if root.data>data:
#         root.left=buildbst(root.left,data)
#     if root.data<data:
#         root.right=buildbst(root.right,data)
#     return root
# # arr=[]
# def inorder(root):
#     # nonlocal arr
#     arr=[]
#     if not root:
#         return 
#     if root:
#         # if root.left:
#         inorder(root.left)
#         # if root.right:   
#         print(root.data) 
#         inorder(root.right)
#     return arr
# n=int(input())
# root=None
# for i in range(n):
#     d=int(input())
#     root=buildbst(root,d)

# print(inorder(root))
    


#leetcode Q-95
# creating bst from scratch

# this was the only main structure
# class Node:
#     def __init__(self,data,left,right):
#         self.data=data
#         self.left=left
#         self.right=right
# def trav(start,end):
#     res=[]
    
#     if start>end:
#         res.append(None)
#         return res
#     for i in range(start,end+1):
#         ltree=trav(start,i-1)
#         rtree=trav(i+1,end)
#         for l in ltree:
#             for r in rtree:
#                 root=Node(i,l,r)
#                 res.append(root)
                
#     return res
# n=int(input())
# ans=trav(1,n)
# for i in ans:
#     print(i)
    
# def fn(arr):
#     n=len(arr)
#     dp=[[[-1 for _ in range(n)]for _ in range(n)]for _ in range(n)]
#     def f(idx,p1,p2):
#         if idx>=n:
#             return 0
#         if dp[idx][p1][p2]!=-1:
#             return dp[idx][p1][p2]
#         if p1==-1:
#             pick1=f(idx+1,idx,p2)

#         else:
#             if arr[idx]>arr[p1]:
#                 pick1=1+f(idx+1,idx,p2)
#             else:
#                 pick1=f(idx+1,idx,p2)
#         if p2==-1:
#             pick2=f(idx+1,p1,idx)
#         else:
#             if arr[idx]>arr[p2]:
#                 pick2=1+f(idx+1,p1,idx)
#             else:
#                 pick2=f(idx+1,p1,idx)
        
#         dp[idx][p1][p2]= min(pick1,pick2)
#         return dp[idx][p1][p2]
#     return f(0,-1,-1)
# t=int(input())
# final=[]
# for i in range(t):
#     n=int(input())
#     arr=list(map(int,input().split()))
#     final.append((fn(arr)))
# for i in final:
#     print(i)


# def fk(arr):
#     s=1e9
#     t=1e9
#     # try to keep s[-1]<=t[-1]
#     count=0
#     for i in arr:
#         if s>t:
#             s,t=t,s
#         if i<=s:
#             s=i
#         elif i<=t:
#             t=i
#         else:
#             s=i 
#             count+=1
#     return count
# t=int(input())
# final=[]
# for i in range(t):
#     n=int(input())
#     arr=list(map(int,input().split()))
#     final.append((fk(arr)))
# for i in final:
#     print(i)

# import math
# def f(a,n):
#     count=0
#     for i in range(1,n+1):
#         if n%i==0:
#             k=n//i
#             m=0
#             for j in range(k):
#                 m_k=0
#                 for l in range(j,n,k):
#                     m_k=math.gcd(m_k,abs(a[j]-a[l]))
#                 m=math.gcd(m,m_k) 
#             if m!=1:
#                 count+=1
#     return count
# t=int(input())
# final=[]
# for i in range(t):
#     n=int(input())
#     a=list(map(int,input().split()))
#     final.append(f(a,n))
# for i in final:
#     print(i)

# def f(n):
#     count=0
#     def get_s(k):
#         su_n=0
#         while k>0:
#             su_n+=k%10
#             k=k//10
#         return su_n
#     pres=[0]*(n+1)
#     for i in range(n+1):
#         pres[i]=get_s(i)

#     arr=set()
#     for i in range(n+1):
#         for j in range(n+1):
#             k=n-i-j
#             if k>=0:
#                 if i+j+k==n:
#                     k_o=[i,j,k]
#                     k_o=tuple(k_o)
#                     # k_o=sorted(k_o)
#                     if pres[i]+pres[j]+pres[k]==pres[n] and k_o not in arr:
#                         arr.add(k_o)
#                         count+=1
#     return count
# t=int(input())
# fin=[]
# for i in range(t):
#     n=int(input())
#     fin.append(f(n))
# for i in fin:
#     print(i)
# Time complexity of this is high (above code) so we can optimize this. Try to think the approach of carry over.
# def f(n):
#     count=1
#     while n>0:
#         r=n%10
#         n=n//10
#         k=0
#         for i in range(r+1):
#             for j in range(r+1):
#                 if r-i-j>=0:
#                     k+=1
#         count=count*k
#     return count
# t=int(input())
# fin=[]
# for i in range(t):
#     n=int(input())
#     fin.append(f(n))
# for i in fin:
#     print(i)

# from itertools import combinations
# ans=combinations([2,3,4],2)
# res=[]
# for j in ans:
#     res.append(list(j))
# # res=[list(k) for k in ans]
# print(res)
# from itertools import combinations

# comb = combinations([1, 2, 3], 2)

# # Convert each tuple to a list using list comprehension
# result = [list(pair) for pair in comb]

# print(result)


# https://neetcode.io/problems/islands-and-treasure?list=neetcode250
'''
Input: [
  [2147483647,-1,0,2147483647],
  [2147483647,2147483647,2147483647,-1],
  [2147483647,-1,2147483647,-1],
  [0,-1,2147483647,2147483647]
]
'''
# from collections import deque
# class Solution:
#     def islandsAndTreasure(self,grid):
#         def isValid(r,c):
#             if r>=0 and r<len(grid) and c>=0 and c<len(grid[0]):
#                 if grid[r][c]!=-1 and grid[r][c]!=0:
#                     return True
#             return False
#         def bfs(x,y):
#             q.append((x,y))
#             while len(q)>0:
#                 k=q.popleft()
#                 row=k[0]
#                 col=k[1]
#                 dirs=[(0,1),(1,0),(-1,0),(0,-1)]
#                 for dx,dy in dirs:
#                     r=row+dx
#                     c=col+dy
#                     if isValid(r,c):
#                         if grid[r][c]>grid[row][col]+1:
#                             q.append((r,c))
#                             grid[r][c]=grid[row][col]+1


#         q=deque()
#         for i in range(len(grid)):
#             for j in range(len(grid[0])):
#                 if grid[i][j]==0:
#                     bfs(i,j)
#         return grid

# sol=Solution()
# grid=[
#   [0,-1],
#   [2147483647,2147483647]
# ]
# print(sol.islandsAndTreasure(grid))
# class soln: 
#     def f(grid): 
#         def fn(idx,mask): 
#             if idx>=len(grid): 
#                 return 