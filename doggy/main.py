print("doggy run :3")

f = open("bap.txt", "w+")
text = f.read()
text = text + "*boop*\n"
f.write(text)
f.close()
import time
while True:
    time.sleep(1)
    print("arf")