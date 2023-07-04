import os, subprocess, json, runErrors, time

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
    systemFiles = ['main.py', 'runErrors.py', 'config/']
    for item in systemFiles:
        # runningDirectoryFiles.remove(item)
        print(item)
    # runningDirectoryFiles.remove("main.py")
    print(runningDirectoryFiles)
    # return runningDirectoryFiles

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
    if file in runningProcesses:setState = "enable"
    # elif file not in runningProcesses: setState = "disable"
    else: setState = "disable"
    # setState = "b"
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
        raise runErrors.NotValidState(file, newState)

# Setup
reloadRunnable()

# This just verifies that stuff works
runFilesPy = ["awoooooo\main.py","doggy\main.py"]
# runFiles = runFilesPy
processes = []

for file_path in runFilesPy:
    print(f"Processing file: {file_path}")

    command = ['python', file_path]  # Assuming you are running Python scripts

    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, universal_newlines=True)
    processes.append(process)

while True:
    # Read output from each process and display it
    for process in processes:
        output = process.stdout.readline()
        if output:
            # Print the output along with the corresponding process's arguments
            print(f"Output from {process.args}: {output.strip()}")

    # Example: Sleep for a short period before checking for output again
    time.sleep(0.025)

# while processes:
#     for process in processes:
#         output = process.stdout.readline()
#         if output == '':
#             # Process has terminated
#             # processes.remove(process)
#             pass
#         else:
#             # Print the output along with the corresponding process's arguments
#             print(f"Output from {process.args}: {output.strip()}")