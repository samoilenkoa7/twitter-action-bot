loggings = []
passwords = []
phones = []
emails = []


def split_split_text(file):
    with open(file) as book:
        for line in book.readlines():
            string = line.split(':')
            loggings.append(string[0])
            passwords.append(string[1])
            phones.append(string[5].replace('\n', ''))
            emails.append(string[2])
