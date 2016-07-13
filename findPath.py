import os
def findStrInFilename(s,d):
    for f in os.listdir(d):
        curfile = os.path.join(d,f)
        if s in f:
            if os.path.isfile(curfile):
                print('Filename=%s,RelationPath=%s'%(f,curfile))
        if os.path.isdir(curfile):
            findStrInFilename(s,curfile)
    return 0

if __name__ == '__main__':
    file = input('Enter file name:-->')
    path = '.'
    findStrInFilename(file,path)