s = 'I love to write python'
split_s= s.split() #splits the string into words
print split_s 

for word in split_s:
    if word.find('i') > -1:
        print 'I found "i" in:', word
