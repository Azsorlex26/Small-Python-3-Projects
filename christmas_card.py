import re

card = """+------------------------------------------------------------------------------+
21
+------------------------------------------------------------------------------+"""

text = """

				Merry Christmas"""

check = re.compile('[a-zA-Z]').search
for line in card.splitlines():
	try:
		last = int(line)
		for i in range(0, last):
			line = '|\t\t\t\t\t\t\t\t\t\t\t|'
			if i < len(text.splitlines()) and bool(check(text.splitlines()[i])):
				line = line.replace('\t', text.splitlines()[i], 1)
			elif i == last - 1:
				line = line.replace('\t', "Press Enter to continue", 1)
			print(line)
	except:
		print(line)

input()
