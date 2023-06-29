class UnableToRun(Exception):
    """Raised when the run command is invalid to run a particular item"""
    def __init__(self, runCommand, fileExtension, errorMessage):
        self.commandRun = runCommand
        self.fileType = fileExtension
        errorMessage = ""
        self.error = errorMessage
        super().__init__()