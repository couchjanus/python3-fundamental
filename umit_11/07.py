
class Stack:
    
    def __init__(self, data = None):
        # create a list that store data
        if data == None:
            self.stack = list()
        elif isinstance(data, list):
            self.stack = data
        else:
            raise ValueError('input data should be list')

    def __iter__(self):
        return iter(self.stack)

# Now you can do this:

mystack = Stack([4,6,2,1,6,3])


for x in mystack:
  print(x)
