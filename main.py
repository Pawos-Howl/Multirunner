import os, subprocess, json, runErrors

# JSON parsing
def configAction(action, file, value):
    if action == "read":
        with open(file+".json", "r") as f:
            pass
    if action == "write":
            json.dump(value, file)

# Get the run files
def getRunFiles():
    pass

def reloadRunnable():
    # os.chdir(".")
    runningDirectoryFiles = os.listdir(".")
    #Remove the included stuff
    runningDirectoryFiles.remove("main.py")
    print(runningDirectoryFiles)

def modifySubproc(file, newState):
    # https://docs.python.org/3/library/subprocess.html
    # for bark in range(0, len(runFiles)):
    #     try:
    #         #start subproc
    #         pass
    #     except:
    #         #go to next item in list
    #         print(f'ERROR STARTING SUBPROCESS WITH: {bark}; EXCEPTION: {Exception}')
    #         continue
    # return "done"
    setState = "b"
    if newState == setState:
        print("No changes, same state :3")
    elif newState == "on":
        try:
            pass
        except:
            print("ERROR")
    elif newState == "off":
        pass

def startPY(paff):
    commandToStart = f'py {paff}'
    try:
        subprocess.run(args=commandToStart, capture_output=True)
    except:
        exit("SERIOUS FILE ERROR! FILE IS BROKEN.")

# Setup
# reloadRunnable()

# This just verifies that stuff works
runFilesPy = ["awoooooo\main.py","doggy\main.py"]
processes = []

for file_path in runFilesPy:
    print(f"Processing file: {file_path}")

    command = ['python', file_path]  # Assuming you are running Python scripts

    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, universal_newlines=True)
    processes.append(process)

import time
while True:
    for process in processes:
        output = process.stdout.readline()
        if output == '' and process.poll() is not None:
            break
        if output:
            print(output.strip())

    process.wait()
    print("\n")  # Add a newline to separate the output of each file
    time.sleep(0.025)