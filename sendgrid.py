#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#! /usr/bin/python

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def sendmail(toEmail="jaguar7444@yahoo.com", url="http://www.tumblr.com", object = '<a href="http://stumblr.bamplify.com">Try Stumblr!</a>'):
	# Your From email address
	fromEmail = "stumblr@bamplify.com"
	# Recipient
	toEmail = "jaguar7444@yahoo.com"

	# Create message container - the correct MIME type is multipart/alternative.
	msg = MIMEMultipart('alternative')
	msg['Subject'] = "Stumblr site shared!"
	msg['From'] = fromEmail
	msg['To'] = toEmail

	# Create the body of the message (a plain-text and an HTML version).
	# text is your plain-text email
	# html is your html version of the email
	# if the reciever is able to view html emails then only the html
	# email will be displayed
	text = "Hi!\nA user wishes to share a site from Stumblr.\n"
	html = """\
	<html>
	  <head></head>
	  <body>
		<p>
		   %s
		</p>
	  </body>
	</html>
	"""% (object,)

	# Login credentials
	username = 'jaguar7444'
	password = "sendgrid"

	# Record the MIME types of both parts - text/plain and text/html.
	part1 = MIMEText(text, 'plain')
	part2 = MIMEText(html, 'html')

	# Attach parts into message container.
	msg.attach(part1)
	msg.attach(part2)

	# Open a connection to the SendGrid mail server
	s = smtplib.SMTP('smtp.sendgrid.net', 587)

	# Authenticate
	s.login(username, password)

	# sendmail function takes 3 arguments: sender's address, recipient's address
	# and message to send - here it is sent as one string.
	s.sendmail(fromEmail, toEmail, msg.as_string())

	s.quit()

def main():
	sendmail()
	return 0

if __name__ == '__main__':
	main()


