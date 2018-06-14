#!/usr/bin/env python

import smtplib
import requests
from time import gmtime, strftime

 
def sendemail(message,
              from_addr='sergeypust@gmail.com', 
              to_addr_list=['sergeypust@gmail.com'], 
              subject='IES queue opened', 
              login='sergeypust', 
              password='Chupakabra123',
              smtpserver='smtp.gmail.com:587'):
    header  = 'From: %s\n' % from_addr
    header += 'To: %s\n' % ','.join(to_addr_list)
    header += 'Subject: %s\n\n' % subject
    message = header + message
 
    server = smtplib.SMTP(smtpserver)
    server.starttls()
    server.login(login,password)
    problems = server.sendmail(from_addr, to_addr_list, message)
    server.quit()
    return problems

def pagestatus(url):
  request = requests.get(url, allow_redirects=False)
  print(request.status_code)
  return request.status_code

def pagecontains(url, text):
  request = requests.get(url, allow_redirects=False)
  return request.text.find(text)


ss_iesva = "https://sms.schoolsoft.se/engelska/jsp/public/right_public_studentqueue.jsp?school=iesva"
ss_iesvar = "https://sms.schoolsoft.se/engelska/jsp/public/right_public_studentqueue.jsp?school=iesvar"
ss_iesvmd = "https://sms.schoolsoft.se/engelska/jsp/public/right_public_studentqueue.jsp?school=iesvmd"
ss_iesvarmdo = "https://sms.schoolsoft.se/engelska/jsp/public/right_public_studentqueue.jsp?school=iesvarmdo"

ss_iesgu = "https://sms.schoolsoft.se/engelska/jsp/public/right_public_studentqueue.jsp?school=iesgu"
ss_iesgus = "https://sms.schoolsoft.se/engelska/jsp/public/right_public_studentqueue.jsp?school=iesgus"
ss_iesgustavsberg = "https://sms.schoolsoft.se/engelska/jsp/public/right_public_studentqueue.jsp?school=iesgustavsberg"

school_list = "https://engelska.se/our-schools/join-queue"

print("Check started at " + strftime("%Y-%m-%d %H:%M:%S", gmtime()))

if pagestatus(ss_iesva) == 200:
  print("sending the email")
  sendemail(ss_iesva)
if pagestatus(ss_iesvar) == 200:
  print("sending the email")
  sendemail(ss_iesvar)
if pagestatus(ss_iesvmd) == 200:
  print("sending the email")
  sendemail(ss_iesvmd)
if pagestatus(ss_iesvarmdo) == 200:
  print("sending the email")
  sendemail(ss_iesvarmdo)

if pagestatus(ss_iesgu) == 200:
  print("sending the email")
  sendemail(ss_iesgu)
if pagestatus(ss_iesgus) == 200:
  print("sending the email")
  sendemail(ss_iesgus)
if pagestatus(ss_iesgustavsberg) == 200:
  print("sending the email")
  sendemail(ss_iesgustavsberg)

if pagecontains(school_list, "Värmdö") != -1:
  print("Värmdö - Found in list")
  sendemail(school_list)
if pagecontains(school_list, "Gustavsberg") != -1:
  print("Gustavsberg - Found in list")
  sendemail(school_list)