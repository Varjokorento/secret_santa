import smtplib
import random
import copy
import yaml

SUBJECT_LINE = 'Your Secret Santa'
EMAIL_BODY = 'You will give a gift to'

def get_credentials():
    config = yaml.safe_load(open("config.yaml"))
    return config["username"], config["password"]

def get_name_lists():
    config = yaml.safe_load(open("config.yaml"))    
    to = []
    names = []
    for email in config["emails"]:
        names.append(email["name"])
        to.append((email['name'], email['email']))
    return to, names


def make_and_get_pairs():
    to = []
    names = []
    to, names = get_name_lists()
    names_copy = copy.copy(names)
    random.shuffle(names_copy)
    pairs = []
    for name, email in to:
        recipient_name = name
        iteration_copy = copy.copy(names_copy)
        if recipient_name in iteration_copy:
            iteration_copy.pop(iteration_copy.index(recipient_name))
        selected_name = random.choice(iteration_copy)
        names_copy.pop(names_copy.index(selected_name))
        pairs.append((email, selected_name))
    return pairs


def secret_santa(send_mail):
    gmail_user, gmail_password = get_credentials()
    sent_from = gmail_user
    pairs = make_and_get_pairs()
    for gift_giver_email, gift_recipient_name in pairs:
        subject = SUBJECT_LINE
        body = EMAIL_BODY 
        email_text = """\
        From: %s
        To: %s
        Subject: %s

        %s
        """ % (sent_from, gift_giver_email, subject, body)
        try:
            if send_mail == True:
                server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
                server.ehlo()
                #server.login(gmail_user, gmail_password)    
                #server.sendmail(sent_from, email, email_text)
                server.close()
        except Exception as e:
            print(e)
            print('Error occurred')
    return pairs

secret_santa(True)