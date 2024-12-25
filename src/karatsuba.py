def karatsuba(x: str, y: str) -> int:
  max_len = max(len(x), len(y))
  x = x.zfill(max_len)
  y = y.zfill(max_len)

  if len(x) == 1 or len(y) == 1:
    return int(x)*int(y)

  m = len(x) // 2
  x1, x0 = int(x[:-m]), int(x[-m:])
  y1, y0 = int(y[:-m]), int(y[-m:])
  
  a = x1*y1

  b = x0*y0

  d = (x1*y0) + (x0*y1)
  
  ## Assuming base 10
  B = 10
  return a*(B**(2*m)) + b + d*(B**m)
  
def karatsuba_rec(x: str, y: str) -> int:
  max_len = max(len(x), len(y))
  x = x.zfill(max_len)
  y = y.zfill(max_len)
              
  if len(x) == 1 or len(y) == 1:
    return int(x)*int(y)

  m = len(x) // 2
  x1, x0 = x[:-m], x[-m:]
  y1, y0 = y[:-m], y[-m:]
  
  # print(f"m={m} x={x1} {x0} y={y1} {y0}")

  a = karatsuba_rec(x1, y1)

  b = karatsuba_rec(x0, y0)

  c = karatsuba_rec(str(int(x1) + int(x0)), str(int(y1) + int(y0)))

  d = c - a - b

  ## Assuming base 10
  B = 10
  return (B**(2*m)) * a + (B**m) * d + b


if __name__ == "__main__":
  x = "3141592653589793238462643383279502884197169399375105820974944592"
  y = "2718281828459045235360287471352662497757247093699959574966967627"

  print(karatsuba(x, y))
  print(karatsuba_rec(x, y))

  assert(karatsuba_rec(x, y) == int(x)*int(y))