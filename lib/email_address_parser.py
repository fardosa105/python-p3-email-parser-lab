# your code goes here!
import re


class EmailAddressParser:
    pass
    # your code goes here!

    def __init__(self, string):
        self.string = string
        self.valid_emails = []
        self.invalid_emails = []

    def parse(self):
        pass
        emails_joined = self.string
        emails_separated = re.split(r"[\s,]+", emails_joined)
        emails_separated = [email for email in emails_separated if email]
        email_pattern = re.compile(r"\D[A-z0-9._\s]+@[A-z0-9]+\.[A-z0-9]+")
        for email in emails_separated:
            if email_pattern.match(email):
                self.valid_emails.append(email)
            else:
                self.invalid_emails.append(email)
        self.valid_emails.sort()
        return self.valid_emails