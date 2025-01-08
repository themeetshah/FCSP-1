#wap that add and subtract 2 given matrix obj
class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __add__(self,other):
        mx=[]
        for i in range(len(self.matrix)):
            my=[]
            for j in range(len(self.matrix[i])):
                my.append(f"{self.matrix[i][j]+other.matrix[i][j]}")
            mx.append(my)
        return mx
    
    def __sub__(self, other):
        mx=[]
        for i in range(len(self.matrix)):
            my=[]
            for j in range(len(self.matrix[i])):
                my.append(f"{self.matrix[i][j]-other.matrix[i][j]}")
            mx.append(my)
        return mx
    
m1=Matrix([[1,2],[3,4]])
m2=Matrix([[5,6],[7,8]])
print("ADD:", (m1+m2))
print("SUB:", (m2-m1))