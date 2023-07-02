print("doggy run :3")

import time, os
f = os.open("bap.txt", "w+")
# f.read()
print(f)
f.append("*boop*\n")
f.close()
while True:
    time.sleep(1)
    print("arf")