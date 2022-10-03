def letter_value(c):
    return ord(c)-ord('a')

def word_value(w):
    count=0
    for letter in w:
        count+=letter_value(letter)
    return count

def is_dollar_word(w):
    if(word_value(w)==100):
        return True
    else:
        return False

fin=open('words.txt')
total=0
count=0
for word in fin:
    word=word.lower()
    total+=1
    if(is_dollar_word(word)):
        count+=1
print("Total numer of words:",total)
print("Total numer worth 100 cents:",count)
print("Percentage of total:" ,count/total)
