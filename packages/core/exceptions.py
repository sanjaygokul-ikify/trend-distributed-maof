class InvalidTaskException(Exception):
    pass

class AgentAlreadyRegisteredException(InvalidTaskException):
    pass

class NoAgentsAvailableException(InvalidTaskException):
    pass

class TaskNotFoundException(InvalidTaskException):
    pass