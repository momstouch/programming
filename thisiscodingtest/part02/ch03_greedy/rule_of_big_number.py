# 5 8 3
# 2 4 6 4 6
# 46

n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort(reverse = True)
n_iter = m // (k + 1)
n_remain = m % (k + 1)
ans = (data[0] * k + data[1]) * n_iter + data[0] * n_remain

print(ans)
