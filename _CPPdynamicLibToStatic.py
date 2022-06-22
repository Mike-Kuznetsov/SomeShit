import os
for filename in os.listdir(os.getcwd()):
    with open(os.path.join(os.getcwd(), filename), 'r+') as f: # Read every file in folder
        if (filename!="_CPPdynamicLibToStatic.py"): # If we read file which is not this program file
            data=f.read();
            result="";
            for line in data.splitlines(): # Go through every line
                if "<openssl/" in line: # If library initialization in line 
                    line=line.replace("<openssl/",'"'); # Replace path to lib to current folder
                    line=line.replace(">",'"');
                    #print(line);
                result = result+"\n"+line;
            f.seek(0); # Write from the first bite of the file not from the last.
            #print(result);
            f.write(result); # Write new data to file
        f.close();
