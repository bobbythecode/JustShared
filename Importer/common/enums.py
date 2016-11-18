from enum import Enum

class HttpStatus(Enum):        
    OK = 200
    InternalError = 503
    
    def __str__(self):
        return '%s' % self._value_
    