# -*- coding: utf-8 -*-
from akad.ttypes import MediaType

def loggedIn(func):
    def checkLogin(*args, **kwargs):
        if args[0].isLogin:
            return func(*args, **kwargs)
        else:
            args[0].callback.other('You want to call the function, you must login to LINE')
    return checkLogin
    
class Call(object):
    isLogin = False

    def __init__(self):
        self.isLogin = True
