from sys import stdin,stdout
from collections import Counter,defaultdict 

def I(): return int(stdin.readline())
def II(): return map(int, stdin.readline().split())
def IL(): return list(map(int, stdin.readline().split()))
def SIL(): return sorted(map(int, stdin.readline().split()))

def valid(arr):
    i = 1 
    for j in arr:
        if i == j:
            i += 1 
        else:
            return False 
    return True 


def solve():
    # write your code here 
    n = I()
    arr = IL()
    count = 0 
    
    def merge(left,right):
        nonlocal count 
        if left == right:
            return [arr[left]]
        
        mid = (left+right)//2 
        left_arr = merge(left,mid)
        right_arr = merge(mid+1,right)
        if left_arr[0] > right_arr[0]:
            count += 1 
            right_arr.extend(left_arr)
            return right_arr 
        left_arr.extend(right_arr)
        return left_arr  
    
    arr = merge(0,n-1)
    if valid(arr):
        return count 
    
    return -1 

    
    
   
    
    
    
    
    


for _ in range(I()):
    print(solve())
