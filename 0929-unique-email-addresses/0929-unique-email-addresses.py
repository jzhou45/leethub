class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        uniq = set()
        
        for email in emails:
            email = email.split("@")
            local, domain = email[0], email[1]
            
            new_loc = ""
            for char in local:
                if char == "+":
                    break
                elif char == ".":
                    continue
                else:
                    new_loc += char
            
            email = new_loc + "@" + domain
            uniq.add(email)
        
        return len(uniq)