class Riyastack:
    def __init__(self):
        self.arr = []  # Corrected to use self.arr to make it an instance variable
    
    def add(self, n):
        self.arr.append(n)  # Corrected to use self.arr
    
    def remove(self):
        if len(self.arr) > 0:
            last = self.arr.pop()  # Using pop() to remove the last element
            print("Your element removed:", last)
        else:
            print("Stack is empty.")
    
    def len(self):
        return len(self.arr)  # Corrected to use self.arr

a = Riyastack()
a.add(2)
a.add(3)
a.add(4)
a.add(7)
print(a.len())  # Prints the length of the stack
a.remove()  # Removes the last element
print(a.len())  # Prints the new length after removal
a.remove()
print(a.len()) 