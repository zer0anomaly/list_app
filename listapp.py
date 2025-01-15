lists = []
while True:
	print("What do you want to do:")
	print("1.Show the list")
	print("2.Add to the list")
	print("3.Remove from the list")
	print("4.Exit")
	var1 = int(input("Give me the number:"))
	if var1 == 1:
		print(lists)
	elif var1 == 2:
		var2 = input("What do you want to add ?:")
		lists.append(var2)
	elif var1 == 3:
		var3 = input("What do you want to remove ?:")
		lists.remove(var3)
	elif var1 == 4:
		print("Exiting")
		break
	else:
		print("Error")
