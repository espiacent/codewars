import time
def tribonacci(signature, n):
  start_time = time.time()
  res = signature[:n]
  for i in range(n - 3): res.append(sum(res[-3:]))
  # print(res)
  print(time.time() - start_time)
  return res

tribonacci([1,2,3], 250000)