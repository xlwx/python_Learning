#! /usr/bin/python
# Filename : contacts.py

import cPickle as p


print '1.Press n to create a new contacts Book'
print '2.Input the name to open an exixsting contacts book'
print '3.Press q to quit'

command = raw_input()

if command == 'q':
    pass
elif command == 'n':
    fileName = raw_input('File Name:-->')
    fileName += '.data'
    contactBook = {}
    while True:
        fileOperation = raw_input('Operations: showAll/delete name/add name number/other to quit-->')
        if fileOperation == 'showAll':
            print contactBook
        elif fileOperation.startswith('delete'):
            strlist = fileOperation.split()
            name = strlist[1]
            if name in contactBook:
                del contactBook[name]
                print '%s is deleted' % name
            else:
                print 'no such persion'
        elif fileOperation.startswith('add'):
            strlist = fileOperation.split()
            if len(strlist) < 3 :
                print 'invalid command'
                continue
            name = strlist[1]
            number = strlist[2]
            contactBook
            contactBook[name] = number
            print '%s is added/changed' %name
        else:
            break
    
    f = file(fileName, 'w')
    p.dump(contactBook,f)
    f.close()
else:
    fileName = command+'.data' 
    f = file(fileName)
    contactBook = p.load(f)
    print contactBook
    while True :
        fileOperation = raw_input('Operations: showAll/delete name/add name number/other to quit-->')
        if fileOperation == 'showAll':
            print contactBook
        elif fileOperation.startswith('delete'):
            strlist = fileOperation.split()
            name = strlist[1]
            if name in contactBook:
                del contactBook[name]
                print '%s is deleted' % name
            else:
                print 'no such persion'
        elif fileOperation.startswith('add'):
            strlist = fileOperation.split()
            name = strlist[1]
            number = strlist[2]
            contactBook
            contactBook[name] = number
            print '%s is added/changed' %name
        else:
            break
    f = file(fileName,'w')
    p.dump(contactBook,f)
    f.close()