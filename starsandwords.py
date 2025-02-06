string = "hello world in a frame"

def starsIntoWords(string):
    x = string.split()
    print(x)
    print('*********')
    for words in x:
        print('* ' + words + ' *')
    print('*********')
starsIntoWords(string)