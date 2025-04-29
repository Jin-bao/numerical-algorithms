def primeQ(num):
  if num < 2:
    return False
  if num==2 or num==3:
    return True
  if num%6!=1 and num%6!=5:
    return False
  for i in range(5,int(num**0.5)+1,6):
    if num%i==0 or num%(i+2)==0:
      return False
  return True

if __name__ == '__main__':
  print(primeQ(23))