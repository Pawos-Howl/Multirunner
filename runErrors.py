class UnableToRun(Exception):
    """Raised when the run command is invalid to run a particular item"""
    def __init__(self, runCommand, fileErrored, errorMessage):
        self.commandRun = runCommand
        self.file = fileErrored
        errorMessage = f'ERROR: COMMAND "{self.commandRun}" IS NOT VALID TO RUN FILE "{self.file}"'
        self.error = errorMessage
        super().__init__(self.error)

class NotValidState(Exception):
    """Raises an error when the state written to the program's run file is not valid"""
    def __init__(self, errorFile, errorState):
        self.errorFile = errorFile
        self.errorState = errorState
        self.errorMessage = f'ERROR: PROGRAM {self.errorFile} WAS NOT GIVEN STATE "enable" or "disable" (STATE "{self.errorState}" IS NOT VALID)'
        super().__init__(self.errorMessage)
