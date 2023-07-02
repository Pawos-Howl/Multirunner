print("awooo run :3")
f = open("beep.txt", "w+")
text = f.read()
text = text + "*boop*\n"
f.write(text)
f.close()