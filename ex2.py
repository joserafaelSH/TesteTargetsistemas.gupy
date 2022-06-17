memo = [-1 for i in range(10000)]
memo[0] = 0
memo[1] = 1

def fibonacci(n:int):
  if n == 0:
    return memo[0]
  if n ==  1:
    return memo[1]
  i = 2
  
  while(1):
    memo[i] = memo[i-1]+ memo[i-2]
    if(memo[i]== n ):
      return True
    if(memo[i]>n):
      return False
    i+=1

def main():
  assert(fibonacci(4) == False)
  assert(fibonacci(21) == True)
  assert(fibonacci(5) == True)

if __name__ == "__main__":
  main()