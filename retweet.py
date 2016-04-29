#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ===================================================================
#     FileName: twitter.py
#       Author: brucvv
#        Email: brucvv@gmail.com
#   CreateTime: 2016-04-29 16:33
# ===================================================================
import twitter
api = twitter.Api(consumer_key='6Zv07gAH6FbFyafrOkWVek3jc',
                      consumer_secret='pr029JHcCue3Ymb9aSd2k5Kmm3aKT27R3yodwXMbqGpOGz8ETH',
                      access_token_key='2870829696-4jeT4KuzWPuixEhrBB7Zyl5stggIKB0OjFpVFRv',
                      access_token_secret='1LvhZd4FFDYk3rqMXS8jGGwHmQoOPcqYRJlk3PiEs867p')
print(api.VerifyCredentials())
statuses = api.GetUserTimeline(screen_name='rangxiangzi')
print([s.text for s in statuses])
status = api.PostUpdate('这是一个tweet，由python-twitter自动生成!')
print(status.text)
