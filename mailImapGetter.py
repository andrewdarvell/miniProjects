# coding: utf8
import imaplib, email, quopri

#fefdваываав

server = "imap.googlemail.com"
port = "993"
login = "darvelldark@gmail.com"
password = ""

#box = poplib.IMAP4(server, port)
M = imaplib.IMAP4_SSL(server, port)
M.login(login, password)
 
M.select("INBOX")

rv, mailboxes = M.list()
if rv == 'OK':
    print "Mailboxes:"
    for box in mailboxes:
	    pass

#rv,data = M.search(None,"UNSEEN")
typ, data = M.search(None,"(UNSEEN)")

for num in data[0].split():
	data = M.fetch(num, '(RFC822)')
	raw_mail = data[1][0][1]
	mail = email.message_from_string(raw_mail)
	subject = mail.get('Subject')
	
	for part in mail.walk():
		if part.get_content_maintype() == 'multipart':
			continue
		if part.get('Content-Disposition') is None:
			continue
		filename = part.get_filename()
		print filename
#	print raw_mail
	
	print quopri.decodestring(subject)
M.close()
M.logout()