class Matrix:
    def __init__(self, lst):
        self.__elements = lst

    def __str__(self):
        matrix_str = ""

        for line in self.__elements:
            for elem in line:
                matrix_str += f"{elem} "

            matrix_str = matrix_str.strip() + "\n"

        return matrix_str

    def __add__(self, other):

        new_elements = []

        for i in range(len(self.elements)):
            line = []
            for j in range(len(self.elements[i])):
                line.append(self.elements[i][j] + other.elements[i][j])

            new_elements.append(line)

        return Matrix(new_elements)

    @property
    def elements(self):
        return self.__elements


m1 = Matrix([[31, 22], [37, 43], [51, 86]])
m2 = Matrix([[1, 2], [3, 4], [5, 6]])

print(m1)
print(m2)

print(m1 + m2)