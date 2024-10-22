answer = input("What is the answer to the Great Question of Life, the Universe and Everything? \n").lower().strip()
right = ["42", "forty two", "forty-two", " 42 "]
if answer in right :
    print("Yes")
else:
    print("No")
