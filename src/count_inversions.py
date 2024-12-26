def sort_and_count_inversions(a: list[int]) -> int:
  n = len(a)
  if n == 1:
    return (a.copy(), 0)

  m = n // 2

  b, x = sort_and_count_inversions(a[:-m])
  c, y = sort_and_count_inversions(a[-m:])
  d, z = merge_and_count_split_inv(b, c)

  return (d, x + y + z)

def merge_and_count_split_inv(b: list[int], c: list[int]) -> int: ## Inversion if i <= n/2 <= j
  d = [0]* (len(b)+len(c))
  i = 0
  j = 0

  split_inv = 0

  for k in range(len(d)):
    if j >= len(c) or (i < len(b) and b[i] < c[j]):
      d[k] = b[i]
      i += 1
    else:
      d[k] = c[j]
      j += 1
      if i < len(b):
        split_inv += len(b) - i
  return (d, split_inv)
  

if __name__ == "__main__":
  arr = [9,8,7,6,5,4,3,2,1]
  print(sort_and_count_inversions(arr)[0])
  print(sort_and_count_inversions(arr)[1])
  import sys
  filename = sys.argv[1]
  with open(filename, "r") as f:
    arr = [ int(x) for x in f.read().split("\n")]
    print(sort_and_count_inversions(arr)[1])