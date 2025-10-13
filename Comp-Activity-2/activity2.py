#Research and answer the following questions: 
#
#1. What is Python?
#2. What is Compiling and Interpreting?
#3. Python Types
#4. What is IDLE?
#

try:
    from tabulate import tabulate
except ImportError:
    import os
    os.system('pip install tabulate')
    from tabulate import tabulate

class QnA:
	def __init__(self, num, question, answer):
		self.number = num
		self.question = question
		self.answer = answer

# for Q3:
class PyDT:
	def __init__(self, category, type_n, examples, desc):
		self.categ = category
		self.type_n = type_n
		self.examples = examples
		self.desc = desc


qna_data_types = [
	PyDT("Text", "str", "\"hello\", 'world'", "Sequence of Unicode characters"),
	PyDT("Numeric", "int, float, complex", "123, 12.3, 12+3j", "Contains numbers, decimals and complex numbers with real and imaginary parts"),
	PyDT("Boolean", "bool", "True, False", "Logical values"),
]

def parse_data_types():
    return tabulate([[t.categ, t.type_n, t.examples, t.desc] for t in qna_data_types], headers=["Category", "Type", "Example", "Description"], tablefmt="grid")

qna_data = [
	QnA(1, "What is Python?", "Python is a high-level, general-purpose programming language known for its emphasis on code readability and simplicity. It was designed by Guido van Rossum and first released in 1991. Python supports multiple programming paradigms, including procedural, object-oriented, and functional programming."),
	QnA(2, "What is Compiling and Interpreting?", "Compiler is a translator that takes input i.e., High-Level Language, and produces an output of low-level language i.e. machine or assembly language.\nThe work of a Compiler is to transform the codes written in the programming language into machine code (format of 0s and 1s) so that computers can understand,\nwhile an interpreter is a program that translates a programming language into a comprehensible language.\nThe interpreter converts high-level language to an intermediate language. It contains pre-compiled code, source code, etc."),
	QnA(3, "Python Types", f"Here are the Python data types:\n{parse_data_types()}"),
	QnA(4, "What is IDLE?", "IDLE stands for Integrated Development and Learning Environment, and it's Python’s built-in editor and shell, perfect for beginners and quick scripting.")

]

global inp, outp
i = 0

print("Ask some questions, must be the same as the ones in the activity 2.\n")
while i < len(qna_data):
	q = qna_data[i]

	inp = input(f"{q.number}. ")
	if (inp.strip().upper() == q.question.upper()):
 		print(f"> {q.answer}\n")
 		i += 1
	elif (inp.strip().lower() == "exit"):
 		exit()
	else:
 		print("That response isn't even in the question, please try again.\n")
 		

