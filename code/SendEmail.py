"""
Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

 http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""
import smtplib
import os

def sendEmail(receiver, itemName, url):
    """
    Sending the notification email to the giving user.
    Takes in the user's email, product name, and product url as input.
    In order to send the email, please prepare an email account and
    fill in the gmail_user for email address and gmail_password for password
    :param receiver: The email address of the receiver(User)
    :param itemName: The name of the the product
    :param url: URL of the product
    :return: 1 if the email sent successfully, 0 if not
    @author: Fishish
    """

    # The email address of sender
    gmail_user = os.environ['GMAIL_ID']
    # The password of sender's email
    gmail_password = os.environ['GMAIL_PASSWORD']

    # The subject of email content
    subject = "The item " + itemName + " is restocked!!!!!"

    # The body of email body
    body = "The item " + itemName + " at " + url + " has been restocked."

    # The whole email text
    email_text = """From: Your ItemStockTracker 
To: %s
Subject: %s
%s
    """ % (
        receiver,
        subject,
        body,
    )

    # Login to the sender email and send the email
    # Print "You've Got Mail!"
    try:
        smtp_server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
        smtp_server.ehlo()
        smtp_server.login(gmail_user, gmail_password)
        smtp_server.sendmail(gmail_user, receiver, email_text)
        smtp_server.close()
        print("You've Got Mail!")

    # Handle the exception and print "Whoops…."
    except Exception as ex:
        print("Whoops….", ex)
