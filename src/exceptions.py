class ExceptionHandler(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.message = message

# TODO: custom exception options