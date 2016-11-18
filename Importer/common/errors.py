import sys

from flask import Response

from common.enums import *
from common.constants import *
from common.errors import *


class NotFoundError(Exception):
    """NotFoundError"""

class DuplicatedError(Exception):
    """DuplicatedError"""


class CreateItemError(Exception):
    """CreateItemError"""
    
    
def returnSuccess(): 
    resp = Response(ErrorMsg.SUCCESS, status=HttpStatus.OK, mimetype='text/html')
    return resp;
    
def returnInternalError(className = '', methodName = ''):
    msg = sys.exc_info()[1];
    
    print("Method:", className, methodName)
    print("Message:", msg)
    resp = Response(msg, status=HttpStatus.InternalError, mimetype='text/html')
    return resp
