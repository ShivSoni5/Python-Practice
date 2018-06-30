#!/usr/bin/python3

import imaplib,email

mail = imaplib.IMAP4_SSL('imap.gmail.com')
mail.login('fakeshivsonic05@gmail.com','myfakeid05')

mail.select('inbox')

mail_ids = mail.search(None, 'ALL')[1][0]

id_list = mail_ids.split()

first_email_id = int(id_list[0].decode())

latest_email_id = int(id_list[-1].decode())

for i in range(latest_email_id,first_email_id,-1):
    typ, data = mail.fetch(str(i),'(RFC822)')
    for response_part in data:
        if isinstance(response_part,tuple):
            msg = email.message_from_string(response_part[1].decode())
            email_subject  = msg['subject']
            email_from = msg['from']
            print(f'From : {email_from}\n')
            print(f'Subject : {email_subject}\n')
