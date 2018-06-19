# -*- coding: utf-8 -*-
from datetime import datetime
from .channel import Channel

import json, time, base64

def loggedIn(func):
    def checkLogin(*args, **kwargs):
        if args[0].isLogin:
            return func(*args, **kwargs)
        else:
            args[0].callback.other('You want to call the function, you must login to LINE')
    return checkLogin
    
class Timeline(Channel):

    def __init__(self):
        Channel.__init__(self, self.channel, self.server.CHANNEL_ID['LINE_TIMELINE'], False)
        self.tl = self.getChannelResult()
        self.__loginTimeline()
        
    def __loginTimeline(self):
        self.server.setTimelineHeadersWithDict({
            'Content-Type': 'application/json',
            'User-Agent': self.server.USER_AGENT,
            'X-Line-Mid': self.profile.mid,
            'X-Line-Carrier': self.server.CARRIER,
            'X-Line-Application': self.server.APP_NAME,
            'X-Line-ChannelToken': self.tl.channelAccessToken
        })
        self.profileDetail = self.getProfileDetail()
