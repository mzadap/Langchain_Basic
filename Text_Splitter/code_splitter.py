from langchain.text_splitter import RecursiveCharacterTextSplitter, Language

text = """
class Calculator:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b

    def subtract(self):
        return self.a - self.b

    def multiply(self):
        return self.a * self.b

    def divide(self):
        if self.b == 0:
            return "Error: Division by zero is not allowed."
        return self.a / self.b


# Using the class
calc = Calculator(10, 5)

print("Addition:", calc.add())
print("Subtraction:", calc.subtract())
print("Multiplication:", calc.multiply())
print("Division:", calc.divide())

"""


splitter = RecursiveCharacterTextSplitter.from_language(
    language=Language.PYTHON,
    chunk_size=400,
    chunk_overlap=0
)

result = splitter.split_text(text)
print(len(result))
print(result)
print(result[0])
print(result[1])