s= 'I love to write python'
for i in s:
    print i, 

print '\n',s[4]
print '\n',s[-1]
print '\n',len(s)
split_s= s.split() #splits the string into words
print split_s 
 
for word in split_s:
    if word.find('i') > -1:
        print "I found 'i' in '{0}'".format(word)





