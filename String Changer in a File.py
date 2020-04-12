mylines = []  
count=0
pattern='font-size'  
data =''
outputFile = open('gnomeOut.css','w')  #output file with  changes applied

def stringMinusOne(input):                                        #this method would decrease a number in a specific string pattern in text
    numbers = ['1','2','3','4','5','6','7','8','9','0']
    number = ''

    for ch in range(len(input)):
        if input[ch] in numbers:
            number+=input[ch]
            
        
    number = str(int(number)-1)
    output = '  font-size: '+number+'pt;\n' 
    return output


                           
with open ('gnome-shell.css') as myfile:   # Open the file that should be edited
    for myline in myfile:                                                     
        if pattern in myline:
            if('pt' in myline):
                count+=1
                data += myline.replace(myline,stringMinusOne(myline))
                mylines.append(myline)
            else:
                 data+=myline 
        else:
            data+=myline

outputFile.write(data)              #writing the final changed data
outputFile.close()                  #closing the file
print('number of edited lines : ' ,count)       #count of changed lines
#print(mylines)