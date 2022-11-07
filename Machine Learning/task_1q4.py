#doesnt work properly two conditions missing

def fun(emails):
    username ,url = emails.split('@')
    website_name ,extension = emails.split('.')

    if website_name.isalnum() == False:
        return False
    elif extension.isalpha() == False:
        return False
    elif len(extension>3):
        return False

    else:
        return True


def filter_mail(emails):
    return list(filter(fun, emails))

if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)