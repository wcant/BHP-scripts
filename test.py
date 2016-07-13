class sumClass:

    def __init__(self, number_one, number_two):
        self.number_one = number_one
        self.number_two = number_two

    def convert_integer(self, number_string):
        converted_integer = int(number_string)

        return converted_integer


    def sum(self):
        number_one_int = convert_integer(self.number_one)
        number_two_int = convert_integer(self.number_two)
        self.result = number_one_int + number_two_int

sumtest = sumClass("1","2")

print sumtest.number_one
print sumtest.sum()




