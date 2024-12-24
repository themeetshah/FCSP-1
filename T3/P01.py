#wap to use wordlist file to find all the words that can be made from a users string

def count_characters(s):
    char_count = {}
    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

user_inp = input("Enter string: ")
inplist = list(user_inp)
inpdict = count_characters(user_inp)

wordlist = open("D:\A1_MeetS\Python\T3\worked_exercises_text_files\wordlist.txt").readlines()

count=0

for j in wordlist:
    word_count=dict.fromkeys(inplist,0)
    for k in list(j):
        if k in inplist:
            word_count[k]+=1
    for k in word_count:
        if inpdict[k]>word_count[k]:
            break
    else:
        count+=1
        print(j)
else:
    print(count)