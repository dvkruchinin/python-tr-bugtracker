#!/usr/bin/env python
# coding:utf-8
"""
Name    : mail.py
Author  : Dmitry Kruchinin
Date    : 7/9/2021
Desc:   
"""

import poplib
import email
import time
import quopri


class MailHelper:

    def __init__(self, app):
        self.app = app

    def get_mail(self, username, password, subject):
        for i in range(5):
            pop = poplib.POP3(self.app.config["james"]["host"])
            pop.user(username)
            pop.pass_(password)
            num = pop.stat()[0]
            if num > 0:
                for n in range(num):
                    msglines = pop.retr(n+1)[1]
                    msgtext = "\n".join(map(lambda x: x.decode("utf-8"), msglines))
                    body = quopri.decodestring(msgtext).decode('utf-8')
                    msg = email.message_from_string(body)
                    if msg.get("Subject") == subject:
                        pop.dele(n+1)
                        pop.quit()
                        msg.get_payload()
                        return msg.get_payload()
            pop.quit()
            time.sleep(15)
        return None
