import random          
import string

def encoding(word):
        word_list=word.split()
        nwords=[]                                # creating an empty list
        for word in word_list:                            # accessing the items of the list
            if(len(word)>3):
                random_1="".join(random.choices(string.ascii_lowercase,k=3))             # adding 3 random alpahabets in starting
                random_2="".join(random.choices(string.ascii_lowercase,k=3))             # adding 3 random alpahabets in end
                _coded=random_1+word[1:]+word[0]+random_2                         # adding random alphabets and words with given index
                nwords.append(_coded)               # putting the received word in the list
            else:
                nwords.append(word[::-1])                   # reversing index of the word and putting it in the list
        return " ".join(nwords)                 # breaking the list and simply joining the words

def decoding(word):
    word_list=word.split()
    nwords=[]
    for word in word_list:
        if(len(word)<=3):
            nwords.append(word[::-1])
        else:
            nwords.append(word[-4]+word[3:-4])         # taking only those words which don't have random alphabets
    return " ".join(nwords)