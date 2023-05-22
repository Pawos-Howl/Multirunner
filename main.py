import os

def removespaces(st):
    strippedstr = ""
    for v in st:
        if v != " ":
            strippedstr = strippedstr+v
    return strippedstr

def convertstringstopython(st):
    table = ["0","1","2","3","4","5","6","7","8","9"]
    isdig = True
    istable = False
    for v in st:
        if v not in table:
            isdig = False
            break

    if ("[" in st and "]" in st and "," in st) or ("[" in st and "]" in st):
        istable = True

    if st == "True":
        st = True
    elif st == "False":
        st = False
    elif isdig == True:
        st = int(st)
    elif istable == True:
        tab = []
        builtvalue = ""
        for v in st:
            if v != "[" and v != "]":
                if v == ",":
                    tab.append(convertstringstopython(removespaces(builtvalue)))
                    builtvalue = ""
                else:
                    builtvalue = builtvalue+v
            elif builtvalue != "" and v == "]":
                tab.append(convertstringstopython(removespaces(builtvalue)))
                builtvalue = ""
        st = tab
    return st

def first_chars(file):
    file.seek(0)
    return file.readlines()

def getbrshattrib(line):
        retline = ""
        constructstring = ""
        hitequalssign = False
        for c in removespaces(line):
            if hitequalssign == False:
                if c != "=" and c != " ":
                    constructstring = constructstring+c
                else:
                    if c == "=":
                        hitequalssign = True
            else:
                retline = retline+c
        return [removespaces(constructstring),removespaces(retline)]

def readconfig(readproperty,default,file):
    for v in first_chars(file):
        cfgproperty = v
        if getbrshattrib(cfgproperty)[0] == readproperty:
            file.seek(0)
            return removespaces(convertstringstopython(getbrshattrib(cfgproperty)[1]).split()[0])
    file.seek(0)
    return default

def setconfig(attribute,value,file):
    owoo = ""
    foundvalue = False
    lines = first_chars(file)
    for v in lines:
        if v != "":
            cfgproperty = v
            if getbrshattrib(cfgproperty)[0] == attribute:
                owoo = owoo+getbrshattrib(cfgproperty)[0]+" = "+str(value)+"\n"
                foundvalue = True
            else:
                owoo = owoo+v+"\n"
    if foundvalue == False:
        print("value not in file")
        owoo = owoo+attribute+" = "+str(value)
    owo = ""
    for v in owoo.splitlines():
        if removespaces(v) != "":
            owo = owo+v+"\n"
    file.seek(0)
    file.write("")
    file.flush()
    file.write(owo)
    file.flush()

# Config Setup


os.chdir(".")
# print(os.listdir("."))
runableFiles = os.listdir(".")
print(runableFiles)

# def getresourceexactpath(paff):
#     return os.path.dirname(os.path.abspath(__file__)) + paff

# # Setup for stuff
# paff = getresourceexactpath("/")
# runableFiles = os.listdir("/")
# print(getresourceexactpath("/"))
# print(runableFiles)