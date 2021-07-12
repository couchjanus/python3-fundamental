import os

def foo(sums):
   for root, dirs, files in os.walk(".", topdown = False):
      for name in files:
         file = os.path.join(root, name)
         sums[0] += os.path.getsize(file)
         sums[1] += 1
         # print(file)
      for name in dirs:
         dir = os.path.join(root, name)
         sums[2] += 1
         # print(dir)
   return sums
          
   
sums = [0,0,1] # 0 bytes, 0 files, 1 directory so far

print(foo(sums))
