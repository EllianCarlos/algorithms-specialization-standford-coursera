def solve(a: list[int], pivotStrat):
  totalCmps = [0]

  def choosePivot(a, l, r, pivotStrat):
    if pivotStrat == 'f':
      return
    if pivotStrat == 'l':
      a[l], a[r] = a[r], a[l]
      return

    mid = ((r-l) // 2) + l
    tmp = [a[l],a[r],a[mid]]
    tmp.sort()

    if tmp[1] == a[l]:
      return
    elif tmp[1] == a[r]:
      a[l], a[r] = a[r], a[l]
      return
    else:
      a[l], a[mid] = a[mid], a[l]
      return
    return

  def partition(a: list[int], l: int, r: int) -> int:  
    pivot = a[l]
    j = l + 1
    for i in range(l+1, r+1):
      if a[i] < pivot:
        a[j], a[i] = a[i], a[j]
        j += 1
    a[j-1],a[l] = a[l],a[j-1]
    
    return j - 1

  def quicksort(a: list[int], l: int, r: int, totalCmps, pivotStrat):
    if r <= l:
      return a

    totalCmps[0] += (r-l)
    choosePivot(a, l, r, pivotStrat)
    p = partition(a,l,r)
    quicksort(a,l,p - 1,totalCmps,pivotStrat)
    quicksort(a,p + 1,r,totalCmps,pivotStrat)

  quicksort(a, 0, len(a) - 1,totalCmps, pivotStrat)
  return totalCmps

if __name__ == "__main__":
  arr = [3,2,1]
  totalCmps = solve(arr, "m")
  print(totalCmps)
  
  import sys
  filename = sys.argv[1]
  with open(filename, "r") as f:
    arr = [ int(x) for x in f.read().split("\n")]
    pivotList =  ['first', 'middle', 'last']
    strats =  ['f', 'm', 'l']
    for strat in strats:
      totalCmps = solve(arr.copy(), strat)
      print(f"number of comparisons: {totalCmps}")