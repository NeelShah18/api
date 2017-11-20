import smtplib
import logging
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText

#Reason to use passowrd and mail is: it will not count as spam never.
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

def send_mail(reciver, message_text):
    '''send_mail(email_id, your_message_here) --> None
    >>>send_mail("xyz@xyz.abc","Your message here")
    '''
    #Change email address we use for mailing
    fromaddr = "---Email--address--of--company---"
    #Mail id Password.
    sender_password = "---passowrd--of--emailid---"
    toaddr = reciver
    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = "Erro: Your bot is not working properly"

    body = "This message is system generated, please don't reply. Contant at about@datalog.ai \n Your bot is not replying for this message {message}. \nRegards, \nDatalog Team".format(message=message_text)
    msg.attach(MIMEText(body, 'plain'))

    try:
        server = smtplib.SMTP('smtp.gmail.com')
        server.starttls()
        server.login(fromaddr, sender_password)
        text = msg.as_string()
        server.sendmail(fromaddr, toaddr, text)
        server.quit()
        #logging statment to check message send succefully
        logger.info('succeful: email is send to: {add} with message: {mess}'.format(add = toaddr,mess = message_text))
    except:
        #logging statment to trace error
        logger.info('Error: email is not send to %s.'%toaddr)

    return None

def main():
    send_mail("neel@datalog.ai","Hey AI, what is meaning of wisdom?")
    return None

if __name__=="__main__":
    main()
