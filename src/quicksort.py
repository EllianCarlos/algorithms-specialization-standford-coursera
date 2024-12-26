def solve(a: list[int], pivotStrat):
  totalCmps = [0]

  def choosePivot(a, l, r, pivotStrat):
    if pivotStrat == 'f':
      return
    if pivotStrat == 'l':
      a[l], a[r-1] = a[r-1], a[l]
      return

    mid = ((r-1-l) // 2) + l
    tmp = [a[l],a[r-1],a[mid]]
    tmp.sort()

    if tmp[1] == a[l]:
      return
    elif tmp[1] == a[r-1]:
      a[l], a[r-1] = a[r-1], a[l]
      return
    else:
      a[l], a[mid] = a[mid], a[l]
      return
    return

  def partition(a: list[int], l: int, r: int) -> int:  
    pivot = a[l]
    j = l + 1
    for i in range(l+1, r):
      if a[i] < pivot:
        a[j], a[i] = a[i], a[j]
        j += 1
    a[j-1],a[l] = a[l],a[j-1]
    
    return j - 1

  def quicksort(a: list[int], l: int, r: int, totalCmps, pivotStrat) -> list[int]:
    totalCmps[0] += (r-l-1)
    if r-1 <= l:
      return a
    else:
      choosePivot(a, l, r, pivotStrat)
      p = partition(a,l,r)
      quicksort(a,l,p - 1,totalCmps,pivotStrat)
      quicksort(a,p + 1,r,totalCmps,pivotStrat)
    return a

  quicksort(a, 0, len(a),totalCmps, pivotStrat)
  
  return totalCmps

def choosePivot(alist,first,last,pivotID):
    if pivotID == 'first':
        pass

    if pivotID == 'last':
        (alist[first], alist[last]) = (alist[last], alist[first])

    elif pivotID == 'middle':
        mid = (last-first)//2 + first
        listTemp = [alist[first], alist[last], alist[mid]]
        listTemp.sort()
        if listTemp[1] == alist[first]:
            pivotIndex = first
        elif listTemp[1] == alist[last]:
            pivotIndex = last
        else:
            pivotIndex = mid
        (alist[first], alist[pivotIndex]) = (alist[pivotIndex], alist[first])

def partition(alist, first, last):
    pivotVal = alist[first] # initialise pivot as the first element
    leftmark = first+1
    for rightmark in range(first+1,last+1):
        if alist[rightmark] < pivotVal:
            (alist[leftmark],alist[rightmark]) = (alist[rightmark],alist[leftmark])
            leftmark = leftmark + 1
    (alist[leftmark-1],alist[first]) = (alist[first],alist[leftmark-1])

    return leftmark-1       # partition point := where pivot finally occupies

def quickSort(alist,first,last,pivotID):
    numComp = last -first
    if last <= first:
        return (alist, 0)
    else:
        choosePivot(alist,first,last,pivotID)
        splitpoint = partition(alist,first,last)
        (Lsorted,numCompL) = quickSort(alist, first, splitpoint-1, pivotID)
        (Rsorted,numCompR) = quickSort(alist, splitpoint+1, last, pivotID)
        numComp =  numComp + numCompL + numCompR
    return (alist, numComp)

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
      ### Correct Numbers:
      ### 162085 first as pivot
      ### 138382 middle (median as pivot)
      ### 164123 last as pivot