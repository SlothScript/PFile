import os
import console
yeet = """
≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡
"""
def main():
	print("PFile")
	print(yeet)
	print("[A] Edit file\n[B] Create file\n[C] Create and open file")
	todo = input()
	if todo == "A":
		console.clear()
		todo = input("What file (include extentions like .txt or .py)\n")
		console.clear()
		f = open(todo,"r")
		oldcontents = f.read()
		contents = oldcontents
		while todo != "exit":
			console.clear()
			if contents == oldcontents:
				top = f"PFile - {todo}"
			else:
				top = f"PFile - {todo} - Edited"
			print(top)
			print(contents)
			lolo = input()
			if len(lolo) == 1:
				contents = contents + lolo
			else:
				if lolo == "del":
					contents = contents[:-1]
				elif lolo == "delword":
					words = contents.split(" ")
					words.pop(-1)
					contents = " ".join(words)
				elif lolo == "delall":
					contents = ""
				elif lolo == "enter":
					contents = contents + "\n"
				elif lolo == "exit":
					f.close()
					f = open(todo,"w")
					f.write(contents)
					break
				else:
					contents = contents + lolo
	elif todo == "B":
		console.clear()
		todo = input("What is the filename you are creating?\n")
		f = open(todo,"x")
		f.close()
	elif todo == "C":
		console.clear()
		todo = input("What is the filename your are creating and opening?\n")
		f = open(todo,"x")
		f.close()
		f = open(todo,"r")
		oldcontents = f.read()
		contents = oldcontents
		while todo != "exit":
			console.clear()
			if contents == oldcontents:
				top = f"PFile - {todo}"
			else:
				top = f"PFile - {todo} - Edited"
			print(top)
			print(contents)
			lolo = input()
			if len(lolo) == 1:
				contents = contents + lolo
			else:
				if lolo == "del":
					contents = contents[:-1]
				elif lolo == "delword":
					words = content.split(" ")
					words.pop(-1)
					content = " ".join(words)
				elif lolo == "delall":
					contents = ""
				elif lolo == "enter":
					contents = contents + "\n"
				elif lolo == "exit":
					f.close()
					f = open(todo,"w")
					f.write(contents)
					break
				else:
					contents = contents + lolo
if __name__ == "__main__":
	main()
