class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        # https://leetcode.com/problems/unique-email-addresses/
        # Updated: 12/16/2020
        
        uniqueEmails = set()
        for email in emails:
            localName, domainName = email.split('@')
            uniqueEmails.add(localName.split('+')[0].replace('.', '')+'@'+domainName)
        return len(uniqueEmails)