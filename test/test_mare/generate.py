def make_tests():
    file = open('dickens')
    text = file.read()

    paragraphs = [i for i in text.split('\n\n')]

    input_file = open('input.in', 'w')
    input_file.write(str(len(paragraphs)) + '\r\n')
    input_file.write('date.in\r\n')
    for i in range(2, len(paragraphs) + 1):
        input_file.write('date' + str(i) + '.in\r\n')
    input_file.close()


    i = 1
    for p in paragraphs:
        name = ''
        if i == 1:
            name = 'date.in'
        else:
            name = 'date' + str(i) + '.in'
        print i
        f = open(name, 'w')
        f.write(p)
        f.write('\r\n')
        f.close()
        i += 1

queryes = [
    'gigi',
    'doctor & having',
    'I & hero | life',
    'innocently | that | know & will & it & I & yet',
    'shall & turn & out & to & be',
    'happy & Copperfield',
    'restanta & PL',
    'infants & of & either & gender',
    'looking | fire | called & another',
    'be & I',
    'Miss & Betsey',
]

make_tests()

input_file = open('input.in', 'a')
input_file.write(str(len(queryes)) + '\r\n')
for query in queryes:
    input_file.write(query + '\r\n')

input_file.close()

print queryes
    
print 'done'
