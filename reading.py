import string

count_s=0
count_w=0
count_sn=0
count_l=0
in_s=False
in_w=False
in_sn=False


def initialize():
    global count_s, count_w, count_sn,count_l, in_s, in_w, in_sn
    count_s=0
    count_w=0
    count_sn=0
    count_l=0
    in_s=False
    in_w=False
    in_sn=False


def process_file(name):
    fin=open(name, encoding='utf-8')
    global count_s, count_w, count_sn,count_l, in_s, in_w, in_sn
    initialize()
    count_line=0
    in_start=False
    for line in fin:
        if line[0:9]=='*** START':
            in_start=True
        if(in_start==True):
            count_line+=1
            for word in line:
                for letter in word:
                    if(letter in string.ascii_letters):
                        count_l+=1# character count g
                    
                    if letter in string.ascii_uppercase:
                        in_sn=True
                    if letter in '.!?':
                        if in_sn==True:
                            count_sn+=1
                            in_sn=False#sentence count 
                            
                    if letter in string.ascii_letters:
                        in_w=True
                    if letter not in string.ascii_letters:
                        if(in_w==True):
                            count_w+=1
                            in_w=False#word count g
                            
                    if letter in 'aeiou':
                        in_s=True
                    if letter not in 'aeiou':
                        if(in_s==True):
                            count_s+=1
                            in_s=False#syllable count g

                       
            if line[0:7]=='*** END':
                break
    print(name, count_line, 'lines')
    print("Sentence count",count_sn)
    print("Word count", count_w)
    print("Syllable count", count_s)
    print ("Character count", count_l)
    print("CLI",5.88*(count_l/count_w)-29.6*(count_sn/count_w)-15.8)
    print("FKG",11.8*(count_s/count_w)+0.39*(count_w/count_sn)-15.59)
    print("ARI",4.71*(count_l/count_w)+0.5*count_w/count_sn-21.43)
    print("FRE",206.835-84.6*(count_s/count_w)-1.015*(count_w/count_sn))
    print("===================================")
    return 
process_file('mobydick.txt')
process_file('greeneggsandham.txt')
process_file('lordjim.txt')
process_file('the problem of philosophy.txt')

        





