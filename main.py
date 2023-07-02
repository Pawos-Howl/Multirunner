import os, subprocess, json, runErrors, select

# JSON parsing
def configAction(action, file, value):
    if action == "read":
        f = open(file+".json", "r")
        pass
    if action == "write":
            json.dump(value, file)

def reloadRunnable():
    # os.chdir(".")
    runningDirectoryFiles = os.listdir(".")
    #Remove the included stuff
    runningDirectoryFiles.remove("main.py")
    print(runningDirectoryFiles)

def modifySubproc(file, newState, runningProcesses):
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
    if file in runningProcesses:
        setState = "enable"
    elif file not in runningProcesses: setState = "disable"
    setState = "b"
    if newState == setState:
        print(f'No changes to process "{file}", same state :3')
    elif newState == "enable":
        try:
            pass
        except:
            print("ERROR")
    elif newState == "disable":
        pass
    else:
        raise runErrors.notValidState(file, newState)

# Setup
# reloadRunnable()

# This just verifies that stuff works
runFilesPy = ["awoooooo\main.py","doggy\main.py"]
processes = []

for file_path in runFilesPy:
    print(f"Processing file: {file_path}")

    command = ['python', file_path]  # Assuming you are running Python scripts

    try:
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, universal_newlines=True)
        processes.append(process)
    except FileNotFoundError:
        ## Assumes (its bad to assume) 
        raise runErrors.UnableToRun()

# Read output from subprocesses in a non-blocking manner
while processes:
    readable, _, _ = select.select(processes, [], [])

    for process in readable:
        output = process.stdout.readline()
        if output == '':
            processes.remove(process)
        else:
            print(f"Output from {process.args}: {output.strip()}")
            # You can modify or process the output as needed

# Wait for all subprocesses to finish
for process in processes:
    process.wait()