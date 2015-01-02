
def count():
    lstlines = []
    linecount = 0
    textstring = ''
    char = 0
    numb_w=0
    inf = open('text.txt', 'r')
    lines = inf.readlines()

#lines count    
    for s in lines:
        nestedlist = s.split("'\n'") # cancel the empty line
        lstlines.append(nestedlist)
    for d in lstlines:
        if d != ['\n']: # count the line
            linecount += 1
    linecount -= 1

#words count
    inf = open('text.txt', 'r')
    for f in range(len(lstlines)):
        textstring += inf.readline()
    words = textstring.split()
    numb_w=(len(words)-1)
    

#characters count
    for g in words:
        char += len(g)

    print ('Number of line:', linecount,'Number of words:',numb_w,'Number of characters:', char)
       

count()
