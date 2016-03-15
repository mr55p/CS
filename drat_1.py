import os, sys, random
import operator as op
from time import sleep
sys.path.append('./modules')
# import core if i ever make core...
try:
	import core
except ImportError:
	print("Core Cannot be loaded... Breakin")
	raise
else:
	core.cls()
	print("Core is available, good luck")


# Vars
operations = (op.add, op.sub, op.mul)
str_operations = ('+','-','*')
answers = []
user = ''
score = 0

def main():
	global user, answers, score
	print("Welcome to the Maths Quiz; Win big or die hard")
	print("What's your name faggot?")
	user = input()
	# I can think of no more effective way than this
	while not validate(user):
		print("Wrong Answer. What's your name faggot?")
		user = input()

	i = 0
	while i < 10:
		core.cls()
		print("Question ",i+1)
		operator_source = random.randint(0,2) #inclusive thank fuck
		operator = operations[operator_source]
		if operator == op.add:
			operand1 = random.randint(1,999)
			operand2 = random.randint(1,99)
		elif operator == op.sub:
			operand1 = random.randint(1,999)
			operand2 = random.randint(1,99)
			if operand1 < operand2:
				operand1,operand2 = operand2,operand1

		else:
			operand1 = random.randint(1,12)
			operand2 = random.randint(1,12)

		ans = operator(operand1, operand2)
		if ans in answers:
			continue
		else:
			i+=1
		answers.append(ans)
		print('{0}{1}{2}'.format(operand1,str_operations[operator_source], operand2))
		user_ans = input()	
		while not answer_validate(user_ans):
			print("Thats an invalid answer; try again please")
			user_ans = input()
			
		if int(user_ans) == ans:
			score +=1
			print("Correct!")
			sleep(2)
		else:
			print("Incorrect")
			sleep(2)
	
	print("Your Score was {0}/10".format(score))


def validate(user):
	from re import match
	if match('.[0-9]', user):
		return False
	else:
		return True

def answer_validate(ans):
	try:
		ans = int(ans)
	except ValueError:
		return False
	else:
		return True



if __name__ == '__main__':
	main()






		########################
		# Code Appenxix for me #
		########################

""" This is a good bit of code for a generator
Cant be used on this project cause i need to validate
the questions generated rather than just going
bam bam bam all at once unless i did it the sanal
way which i probably won't.
#######################################################################
#######################################################################
#######################################################################
		#	Call with this		#
		#################################

generated = generate()
for i in range(0,10):
	print(next(generated))

def generate():
	while True:
		operate = random.choice(operations)
		operand1 = random.randint(1,12)
		operand2 = random.randint(1,12)
		answer = operate(operand1,operand2)
		if operate == op.add:
			question = "{0}+{1}".format(operand1,operand2)
		elif operate == op.sub:
			question = "{0}-{1}".format(operand1,operand2)
		else:
			question = "{0}-{1}".format(operand1,operand2)

		yield (question,answer)

"""


