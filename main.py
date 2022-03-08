import os

# ascii value of a 
num = 97;
allDiseases = open("all_diseases.txt", "a")

while num<=122:

    # reading input
    f = open("{}_diseases.txt".format(chr(num)), "r")
    data = f.readlines()

    # Keeping only disease name
    newData = open("{}_diseases_output.txt".format(chr(num)), "a")
    for line in data:
        name = ""
        x = line.split("see")
        newData.write('\n')
        if "see" in line:
            newData.write(x[0])
        else:
            newData.write(line)

    newData.close()



    oldData = open("{}_diseases_output.txt".format(chr(num)), "r")

    # removing empty lines
    finalData = open("{}.txt".format(chr(num)), "a")
    for line in oldData:
        if(line != '\n'):
            finalData.write(line)
            allDiseases.write(line)

    allDiseases.write('\n')
    oldData.close()
    finalData.close()
    

    os.remove("{}_diseases_output.txt".format(chr(num)))
    #os.remove("{}.txt".format(chr(num)))
    
    print(chr(num))
    num += 1
        
allDiseases.close()



        


