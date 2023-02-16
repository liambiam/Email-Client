class Email:
    def __init__(self, from_address, subject_line, email_contents):
        self.from_address = from_address
        self.subject_line = subject_line
        self.email_contents = email_contents
        self.has_been_read = False
        self.is_spam = False
        
    def mark_as_read(self):
        self.has_been_read = True
        
    def mark_as_spam(self):
        self.is_spam = True
        
class Inbox:
    def __init__(self):
        self.emails = []                # Empty list
        
    def add_email(self, from_address, subject_line, email_contents):
        email = Email(from_address, subject_line, email_contents)
        self.emails.append(email)       # Append new email objects to list
        
    def list_messages_from_sender(self, sender_address):
        # Build list of email objects if email.from = email.sender
        messages = [email for email in self.emails if email.from_address == sender_address] 
        output = ""
        # Return output string of the subject line for those objects, with an index number
        for i, message in enumerate(messages):
            output += f"{i} {message.subject_line}\n"
        return output
    
    def get_email(self, sender_address, index):
        #As above
        messages = [email for email in self.emails if email.from_address == sender_address]
        # Get email based on input index, return and mark as read
        email = messages[index]
        email.mark_as_read()
        return email
    
    def mark_as_spam(self, sender_address, index):
        # As above, but mark as spam
        messages = [email for email in self.emails if email.from_address == sender_address]
        email = messages[index]
        email.mark_as_spam()
        
    def get_unread_emails(self):
        # As above, but only get the subject line of unread emails
        unread_emails = [email.subject_line for email in self.emails if not email.has_been_read]
        # Return string of subject_line arguments separated by a \n
        output = "" 
        for email in unread_emails:
            output += f"{email}\n"
        return output
    
    def get_spam_emails(self):
        # As above, but for spam only
        spam_emails = [email.subject_line for email in self.emails if email.is_spam]
        output = ""
        for email in spam_emails:
            output += f"{email}\n"
        return output
    
    def delete(self, sender_address, index):
        # Delete email given address and index
        messages = [email for email in self.emails if email.from_address == sender_address]
        self.emails.remove(messages[index])

usage_message = '''
Welcome to the email system! What would you like to do?

s - send email.
l - list emails from a sender.
r - read email.
m - mark email as spam.
gu - get unread emails.
gs - get spam emails.
d - delete email.
e - exit this program.
'''

inbox = Inbox()
user_choice = ""

while True:
    
    # Lowercase and remove spaces
    user_choice = input(usage_message).strip().lower() 

#=====#

    if user_choice == "s":
        # Send an email (Create a new Email object)
        sender_address = input("Enter the address of the sender:\n")
        subject_line = input("Enter the subject line of the email:\n")
        email_contents = input("Enter the contents of the email:\n")
        
        # Now add the email to the Inbox
        inbox.add_email(sender_address, subject_line, email_contents)
        
        # Print a success message
        print("Congratulations, your email has been sent!\n")
        print(f"Subject: {subject_line}\nFrom: {sender_address}\nContents: {email_contents}")

#=====#
   
    elif user_choice == "l":

        # List all emails from a sender_address
        sender_address = input("Please enter the sender address:\n")
        
        # Now list all emails from this sender
        print(inbox.list_messages_from_sender(sender_address))

#=====#

    elif user_choice == "r":
        
        # Step 1: show emails from the sender
        sender_address = input("Please enter the sender address:\n")
        
        # Step 2: show all emails from this sender (with indexes)
        messages = inbox.list_messages_from_sender(sender_address)
        print(messages)
        
        # Step 3: ask the user for the index of the email
        email_index = int(input("Please enter the index of the email that you would like to read:\n"))
        
        # Step 4: display the email
        email = inbox.get_email(sender_address, email_index)
        print(f"Subject Line: {email.subject_line}\nFrom Address: {email.from_address}\nEmail Contents: {email.email_contents}")

#=====#
    
    elif user_choice == "m":

        # Step 1: show emails from the sender
        sender_address = input("Please enter the sender address:\n")
        
        # Step 2: show all emails from this sender (with indexes)
        messages = inbox.list_messages_from_sender(sender_address)
        print(messages)
        
        # Step 3: ask the user for the index of the email
        email_index = int(input("Please enter the index of the spam email:\n"))
        
        # Step 4: mark the email as spam
        inbox.mark_as_spam(sender_address, email_index)

        # Step 5: print a success message
        print("Email has been marked as spam")

#=====#
   
    elif user_choice == "gu":
        
        # Get unread emails
        print(inbox.get_unread_emails())

#=====#
    
    elif user_choice == "gs":
        
        # Get spam emails
        print(inbox.get_spam_emails())

#=====#

    elif user_choice == "d":

        # Step 1: show emails from the sender
        sender_address = input("Please enter the sender address:\n")

        # Step 2: show all emails from this sender (with indexes)
        messages = inbox.list_messages_from_sender(sender_address)
        print(messages)

        # Step 3: ask the user for the index of the email
        email_index = int(input("Please enter the index of the spam email:\n"))

        # Step 4: delete the email
        inbox.delete(sender_address, email_index)

        # Step 5: print a success message
        print("Email has been deleted")

        pass
    else:
        print("Oops - incorrect input")