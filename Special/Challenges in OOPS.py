class skibidi:
    def __init__(self,skabidi):
        self.skabidi = skabidi
    def __lt__(self,other):
        if(self.skabidi<other.skabidi):
            return "ob1 is less than ob2"
        else:
            return"ob2 is less than ob1"
    def __eq__(self, other):
        if(self.skabidi == other.skabidi):
            return "Both are equal"
        else:
            return "Not equal"
        

ob1 = skibidi(2)
ob2 = skibidi(3)
print("Passed Values :", ob1.skabidi, ob2.skabidi)
print(ob1<ob2)

ob3 = skibidi(4)
ob4 = skibidi(4)
print("Passed Values :", ob3.skabidi, ob4.skabidi)
print(ob3 == ob4)