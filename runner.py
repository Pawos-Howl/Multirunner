import os

def getresourceexactpath(paff):
    return os.path.dirname(os.path.abspath(__file__)) + paff

# Setup for stuff
runableFiles = os.listdir("/")
print(getresourceexactpath("/"))
print(runableFiles)