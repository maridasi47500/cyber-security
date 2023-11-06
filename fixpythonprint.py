import sys

bludescFilePath=sys.argv[1]
blu=open(bludescFilePath, 'r')
print("ok")
blu_file_in_lines = blu.readlines()
print(blu_file_in_lines)
mystr=[]

for line in blu_file_in_lines:
       print(line)
       if "print " in line and "import " not in line and "from " not in line:

            mystr.append(str(line.replace("print ","print(")).replace("\n",")\n"))
       elif "Error, " in line and "import " not in line and "from " not in line:
            mystr.append(str(line.replace("Error, ","Error(")).replace("\n",")\n"))
       elif "Exception, " in line and "import " not in line and "from " not in line:
            mystr.append(str(line.replace("Exception, ","Exception(")).replace("\n",")\n"))
       elif "lambda(" in line and "import " not in line and "from " not in line:
           mystr.append(str(line.replace("lambda(","lambda ").replace("):",":")).replace("\n",")\n"))
       else:
            mystr.append(str(line))
blu.close()
blu=open(bludescFilePath, 'w')
blu.write("".join(mystr))
blu.close()
