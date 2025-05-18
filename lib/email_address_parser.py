import re

class EmailAddressParser:
    def __init__(self, emails):
        self.emails = emails

    def parse(self):
        if not self.emails:
            return []
            
        # Split on commas or whitespace and filter out empty strings
        email_list = re.split(r'[,\s]+', self.emails.strip())
        email_list = [email for email in email_list if email]
        
        # Validate email format using regex
        valid_emails = []
        email_regex = re.compile(r'^[a-zA-Z][\w\.-]*@[a-zA-Z0-9]+\.[a-zA-Z]{2,}$')
        
        for email in email_list:
            if email_regex.fullmatch(email):
                valid_emails.append(email)
                
        # Remove duplicates and sort alphabetically
        unique_emails = sorted(list(set(valid_emails)))
        
        return unique_emails