#Task 1
data = [4,0,5,0,3,0,0,5]

def change_list(data):
	non_zero_position = 0
	for i in range (len(data)):
		if data[i] != 0:
			storage = data[i]
			data[i] = data[non_zero_position]
			data[non_zero_position] = storage
			non_zero_position = non_zero_position + 1
	print(data)

change_list(data)

#Task2

def check_poem():

	vowels = 'aeiouy'
	n_vowels = 0
	n_consonants = 0
	line_number = int(input("How many lines will there be? "))
	for i in range(line_number):
		line = input("Enter line: ").lower()
		for x in line:
			if x.isalpha():
				if x in vowels:
					n_vowels = n_vowels + 1
				else:
					n_consonants = n_consonants + 1
	print("Total vowels: ", n_vowels)
	print("Total consonants: ", n_consonants)


check_poem()

#Task3
ef check_coordinates():

	print("First square- coordinates: ")
	x_1 = int(input("Column: "))
	y_1 = int(input("Row: "))
	print("Second square - coordinates: ")
	x_2 = int(input("Column: "))
	y_2 = int(input("Row: "))
	print(x_2)
	print(y_2)
	diff_x = x_2 - x_1
	diff_y = y_2 - y_1

	if x_1 == x_2:
		if y_1 != y_2 and y_2 > 0 and y_2 <= 8:
			print("Yes")
		else:
			print("No")

	if y_1 == y_2: 
		if x_1 != x_2 and x_2 > 0 and x_2 <= 8:
			print("Yes")
		else:
			print("No")

	if x_1 != x_2 and y_1 != y_2:
		if diff_x == diff_y:
			if x_2 > 0 and x_1 != x_2 and x_2 <=8 and y_2 > 0 and y_2 <=8 and y_2 != y_1:
				print("Yes")
			else:
				print("No")
		else:
			print("No")


check_coordinates()
