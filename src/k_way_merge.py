def k_way_merge_sort(arr: list[any], k: int) -> list[any]:
  if len(arr) <= 1:
      return arr

  subarrays = []
  n = len(arr)
  step = (n + k - 1) // k

  for i in range(0, n, step):
    subarrays.append(arr[i:i + step])

  sorted_subarrays = [k_way_merge_sort(subarray, k) for subarray in subarrays]

  return k_way_merge(sorted_subarrays)

def k_way_merge(sorted_subarrays: list[list[any]]) -> list[list[any]]:
  result = []

  pointers = [0] * len(sorted_subarrays) # Pointers keep track of where we visited in every single array

  while True:
    smallest = None
    smallest_index = -1

    for i in range(len(sorted_subarrays)):
        if pointers[i] < len(sorted_subarrays[i]): # Using pointers to guarantee I put smallest numbers in order.
            current_value = sorted_subarrays[i][pointers[i]]
            if smallest is None or current_value < smallest:
                smallest = current_value
                smallest_index = i

    if smallest is None:
        break

    result.append(smallest)
    pointers[smallest_index] += 1
    
  return result

if __name__ == "__main__":
  import random
  arr = [int(random.random()*100) for _ in range(12349)]
  k = 12
  sorted_arr = k_way_merge_sort(arr, k)
  assert(sorted_arr == sorted(arr))
  
  