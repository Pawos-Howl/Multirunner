import os

madeFiles = ["beep.txt", "bap.txt"]
for item in madeFiles:
    try:
        os.remove(item)
    except FileNotFoundError:
        pass
    except Exception as err:
        print(f'ERROR: {err}')