import sys

def main():
    sys.setrecursionlimit(10005) 
    n = int(sys.stdin.readline())
    b = [0] + list(map(int, sys.stdin.readline().split()))  
    a = [0] * (n + 2)  
    ans = 0  

    def pd(x):
        
        if a[x - 1] + a[x] + a[x + 1] == b[x]:
            return 1
        return 0

    def dfs(k):
        nonlocal ans
        if k == n + 1: 
            if pd(n):
                ans += 1
            return
        
        a[k] = 1
        if k == 1 or pd(k - 1):
            dfs(k + 1)
        
        a[k] = 0
        if k == 1 or pd(k - 1):
            dfs(k + 1)

    dfs(1)  
    print(ans)  

if __name__ == '__main__':
    main()
