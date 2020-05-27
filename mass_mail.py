#!/usr/bin/python

#This code was written in Emacs <3

import yagmail

emails = ['john@doe.com',
'jane@doe.com',
'alice@ssl.com',
'bob@ssl.com',
'rms@gnu.org',
'torvalds@linuxfoundation.org']

name = ['John',
        'Jane',
        'Alice',
        'Bob',
        'Richard',
        'Linus']

passwords = ['1234',
             '4321'
             'sjaueAskalsa',
             'AlskaknAsddf',
             'I<3Microsoft',
             'fukUnvidia']


for i in range(0, len(emails)):
    

    template = """Hi [Student Name],

Welcome to the service, we look forward to working with you.

Here are your login details:    

Email: [EMAIL]
Password: [PASSWORD]

Many thanks,
github.com/SamBkamp"""

    template = template.replace("[Student Name]", name[i])
    template = template.replace("[EMAIL]", emails[i])
    template = template.replace("[PASSWORD]", passwords[i])

    yagmail.SMTP('sam@bonnekamp.net').send(emails[i], 'Some Subject Line', template)
    
    print(template)


