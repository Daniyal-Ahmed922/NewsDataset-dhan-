import pandas as pd
import numpy as np
from os import path
import numpy as np
import sys
import os
os.system('color')
from termcolor import colored, cprint
#add bath browser later
path = "fixSentences.csv"
df = pd.read_csv(path)
#filepath = input()
filename='newstel'
def printsetn_options(x):
    text = colored(x, 'red', attrs=['reverse', 'blink'])
    print(text)
    #cprint(df['Sentence'][x], 'green', 'on_red')
    print('Aspect','1.O','2.B-ASP','3.I-ASP')
    print('Select the Aspects and the polarity \n1.none \n2.positive \n3.neutral \n4.negative')
    print(colored('----------------------------------------------------------------------------------------------', 'white', attrs=['underline', 'blink']))
def write_csv_df(path, filename, df):
    # Give the filename you wish to save the file to
    pathfile = os.path.normpath(os.path.join(path,filename))

    # Use this function to search for any files which match your filename
    files_present = os.path.isfile(pathfile) 
    # if no matching files, write to csv, if there are matching files, print statement
    if not files_present:
        df.to_csv(pathfile,index=False)
    else:
        overwrite = input("WARNING: " + pathfile + " already exists! Do you want to overwrite <y/n>? \n ")
        if overwrite == 'y':
            df.to_csv(pathfile,index=False)
        elif overwrite == 'n':
            new_filename = input("Type new filename: \n ")
            write_csv_df(path,new_filename,df)
        else:
            print ("Not a valid input. Data is NOT saved!\n")
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#            
polarity = {'1':'-999','2':'Positive','3':'Neutral','4':'Negative'}    #
Aspect = {'1':'O','2':'B-ASP','3':'I-ASP'}                             #
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#
with open(filename+'.counter', 'r') as the_file:
        co=int(the_file.read())+1
for x in range(co,len(df)):
    nnew=[]
    #print(df['Sentence'][x])
    #os.system('cls' if os.name == 'nt' else 'clear')
    printsetn_options(df['Sentence'][x])
    for words in df['Sentence'][x].split():
        os.system('cls' if os.name == 'nt' else 'clear')
        printsetn_options(df['Sentence'][x])
        print(words+' ')
        while True:
            try:
            # Note: Python 2.x users should use raw_input, the equivalent of 3.x's input
                asp=input('O,B or I  ')
                Aspect[asp]
            except KeyError:
                print("Sorry, I didn't understand that.")
                #better try again... Return to the start of the loop
                continue
            else:
                #age was successfully parsed!
                #we're ready to exit the loop.
                break
        if asp == '1':
          nnew.append(words+' '+'O'+' '+'-999')
          print(colored('----------------------------------------------------------------------------------------------', 'white', attrs=['underline', 'blink']))
        elif asp == '3':
            while True:
                try:
                    if (nnew[-1].split()[-2] == 'B-ASP' or nnew[-1].split()[-2] == 'I-ASP'):
                        nnew.append(words+' '+'I-ASP'+' '+nnew[-1].split()[-1])
                    else:
                        while True:
                            try:
                            # Note: Python 2.x users should use raw_input, the equivalent of 3.x's input
                                asp=input('O,B or I  ')
                                Aspect[asp]
                            except KeyError:
                                print("Sorry, I didn't understand that.")
                                #better try again... Return to the start of the loop
                                continue
                            if asp == '3':
                                print('there is no previous base aspect ')
                            else:
                                #age was successfully parsed!
                                #we're ready to exit the loop.
                                break
                            if asp == '2':
                                while True:
                                    try:
                                        # Note: Python 2.x users should use raw_input, the equivalent of 3.x's input
                                        pol=input('non pos neutral or neg  ')
                                        nnew.append((words+' '+Aspect[asp]+' '+polarity[pol]))
                                    except KeyError:
                                        print("Sorry, I didn't understand that.")
                                        #better try again... Return to the start of the loop
                                        continue
                                    else:
                                        #age was successfully parsed!
                                        #we're ready to exit the loop.
                                        break
                            else:
                                nnew.append(words+' '+'O'+' '+'-999')
                except IndexError:
                    print("start your annotaation first.")
                    asp=input('O,B or I  ')
                    pol=input('non pos neutral or neg  ')
                    nnew.append((words+' '+Aspect[asp]+' '+polarity[pol]))
                    #better try again... Return to the start of the loop
                    continue
                else:
                #age was successfully parsed!
                #we're ready to exit the loop.
                    break
        else :
            while True:
                try:
                    # Note: Python 2.x users should use raw_input, the equivalent of 3.x's input
                    pol=input('non pos neutral or neg  ')
                    nnew.append((words+' '+Aspect[asp]+' '+polarity[pol]))
                except KeyError:
                    print("Sorry, I didn't understand that.")
                    #better try again... Return to the start of the loop
                    continue
                else:
                    #age was successfully parsed!
                    #we're ready to exit the loop.
                    break
            print((words+' '+Aspect[asp]+' '+polarity[pol]))
            print(colored('----------------------------------------------------------------------------------------------', 'white', attrs=['underline', 'blink']))
    print(nnew)
    with open(filename+'.train.dat.atepc', 'a') as the_file:
        for all in nnew:
            the_file.write(all+'\n')
        the_file.write('\n') 
    with open(filename+'.counter', 'w') as the_file:
        the_file.write(str(x)+'\n')
    os.system('cls' if os.name == 'nt' else 'clear')
    with open('README.md', 'r') as f:
        text = f.readlines()
        text[-1]=str(x)+'\n'
    with open('README.md', 'w') as f:
        f.writelines(text)

print("Dataset annotated")
print("go ahead and split it into train and test")
        


#writes = input("enter")
#with open('g:somefile.xml.seg.aetpc', 'a') as the_file:
#    the_file.write(writes+'\n')
