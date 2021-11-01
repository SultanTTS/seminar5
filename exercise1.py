try:
    fhand = open("mailbox.txt")
except:
    print('File cannot be opened')
    exit()


lines=fhand.readlines()
file=open('output.txt', 'w')
for line in lines:
       if 'ESMTP' in line:
           ind=line.find('ESMTP id ')
           en_ind=line.find(';')
           word=line[ind+9:en_ind]
           print(word)
           file.write(word)
           file.write('\n')
fhand.close()
