# -*- coding: utf-8 -*-
from datetime import datetime
from .object import Object
from random import randint

import json, shutil, time, os, base64, tempfile
    
class Models(Object):
        
    def __init__(self):
        Object.__init__(self)

    """Text"""

    def log(self, text):
        print("[%s] %s" % (str(datetime.now()), text))
