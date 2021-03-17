# creation day = 13/03/2021
# last update = 17/03/2021
# version = 0.0.3
# goal = 500 lines
# lines = 428

'''

this laguage is a better version of Void Laguage

update log {

    13/03/2021 {

        1 - project started

    }

    14/03/2021 {
        
        Nothing
        
    }

    15/03/2021 {

        1 - Log function added

    }

    16/03/2021 {

        1 - var function added

    }

    17/03/2021 {

        pass

    }

}

list of commands {

    log { write something in cmd

        examples{

            normal log example {

                log hello, world -> write in cmd "hello, world"

            }

            var log example {
                
                WARNING {

                    you needs to have a variable

                }

                log var varName -> write your var name
                     |
                     |
                     V
                you need to write var

            }
        }
    }

    var { creates a variable with type -> str, int, float and bool

        var VarName = value -> write the value here (str, int, float or bool)
               |
               |
               V
        write your varName here

    }

    userLog {works with variables

        var varName = userLog string -> string inputed
                         |
                         |
                         V
                    write 'userLog'

    }

}

WARNING {

    1 - this laguage is a better version of Void Language
    2 - this laguage is a little simple
    3 - this laguage is in tests

}

'''
from time import sleep

# ============================================== log def ==============================================

def log():

    isBig = False
    varLog = False
    isMath = False
    isMathing = False
    isVarMath = False
    listLen = len(functionName)
    if listLen > 2:
        isBig = True
    
    else:
        isBig = False

    if functionName[1] == 'var':
        varLog = True
        isBig = False
    
    else:
        varLog = False
    
    try:
        if type(int(functionName[1])) == int:
            isMathing = True

    except Exception as erro:
        if type(str(functionName[1])) == str:
            isMathing = False

    else:
        if isMathing and len(functionName) >= 3:
            if functionName[2] == '+':
                if type(int(functionName[3])) == int:
                    sleep(1)
                    print('==' * 50)
                    sleep(1)
                    print(int(functionName[1]) + int(functionName[3]))
                    isMath = True

            elif functionName[2] == '-':
                if type(int(functionName[3])) == int:
                    sleep(1)
                    print('==' * 50)
                    sleep(1)
                    print(int(functionName[1]) - int(functionName[3]))
                    isMath = True
            
            elif functionName[2] == '*':
                if type(int(functionName[3])) == int:
                    sleep(1)
                    print('==' * 50)
                    sleep(1)
                    print(int(functionName[1]) * int(functionName[3]))
                    isMath = True
            
            elif functionName[2] == '/':
                if type(int(functionName[3])) == int:
                    sleep(1)
                    print('==' * 50)
                    sleep(1)
                    print(int(functionName[1]) / int(functionName[3]))
                    isMath = True
    
    t = 0
    l = 0
    ready = False
                
   
    if isBig and not isVarMath and not isMath:
        length = len(functionName)
        i = 0
        sleep(1)
        print('==' * 50)
        for c in range(length - 1):
            
            print(functionName[1 + i], end=' ')
            i += 1

    if not isBig and not isMath and not isVarMath:
        if varLog:
            o = 0
            value = 1
            while True:
                if functionName[2] in varList[o]:
                    if not isBigVar:
                        for item in range(1):
                            sleep(1)
                            print('==' * 50)
                            sleep(1)
                            varList[o][value] = varList[o][value]
                            print(''.join(varList[o][value]))

                    elif isBigVar:
                        length = len(functionName)
                        for c in range(1):
                            sleep(1)
                            print('==' * 50)
                            sleep(1)
                            print(' '.join(varList[o][1]))

                    break
                    
                else:
                    o += 1

        elif not varLog and not isBig and not isMath and not isVarMath:
            sleep(1)
            print('==' * 50)
            sleep(1)
            print(functionName[1])


# ============================================== var def ==============================================
varList = []
def var():
    global isBigVar, varName, varValue
    
    equals = False
    strValue = False
    intValue = False
    isBigVar = False
    floatValue = False
    boolValue = False
    inputType = False

    varName = functionName[1]
    if functionName[2] == '=':
        equals = True
    
    else:
        equals = False
    
    if equals:
        if functionName[3] == 'userLog':
            userLog()
            if isBigInput:
                string = ' '.join(inputedString)
            
            else:
                string = inputedString

            varValue = input(f'{string}')
            inputType = True

        elif type(str(functionName[3])) == str:
            strValue = True
        
        elif type(int(functionName[3].capitalize())) == int:
            print('é')

        elif type(float(functionNam[3])) == float:
            floatValue = True
        
        elif type(bool(functionName[3])) == bool:
            boolValue = True

        print(intValue, strValue, floatValue, boolValue)

        if strValue:
            varValue = str(functionName[3])
        
        elif intValue:
            varValue = int(functionName[3])
        
        elif floatValue:
            varValue = float(functionName[3])
        
        elif boolValue:
            varValue = bool(functionName[3])
    
    if len(functionName) > 4:

        isBigVar = True
        length = len(functionName)
        p = 3
        b = 0
        n = 4
        for c in range(length - 3):
            if b == 0:
                varList.append([varName, [varValue]])
                b += 1
            
            else:
                if not inputType:
                    varValue = functionName[n]
                    m = len(varList) - 1
                    varList[m][1].append(varValue)
                    n += 1

                else:
                    pass

    else:
        varList.append([varName, [varValue]])
        isBigVar = False

    print(varList)


# ============================================== userLog def =======================================

def userLog():
    global inputedString, isBigInput

    inputList = []
    isBigInput = False

    if len(functionName) > 3:
        inputedString = functionName[4]
        if len(functionName) > 4:
            length = len(functionName)
            value = 4
            isBigInput = True

            for c in range(length - 4):
                inputList.append(functionName[value])
                value += 1
            
            inputedString = inputList
        
        else:
            isBigInput = False

        sleep(1)
        print('==' * 50)
        sleep(1)
            
    else:
        pass


# ============================================== varsList def ==============================================

def varsList():
    sleep(1)
    print('==' * 50)
    sleep(1)
    print(varList)


# ============================================== Main ==============================================

red = '\033[1;31m'
green = '\033[1;32m'
yellow = '\033[1;33m'
blue = '\033[1;34m'
purple = '\033[1;35m'
cyan = '\033[1;36m'
white = '\033[0m'

while True:
    print('')

    functionName = input().split()
    functionList = functionName

    'try:'
    if functionName[0] == 'log':
        log()

    elif functionName[0] == 'var':
        var()
    
    elif functionName[0] == 'userLog':
        userLog()
    
    elif functionName[0] == 'varsList':
        varsList()
    
    elif functionName[0] == 'exit':
        break

    else:
        sleep(1)
        print('==' * 50)
        sleep(0.5)
        print(f'function {red}"{functionName[0]}"\033[0m does not exist') 
    
    '''except Exception as erro:
        sleep(1)
        print('==' * 50)
        sleep(0.5)
        print(f'a unknow erro has been occurred:\n      {red}{erro.__class__}{white}')
        continue

    else:
        pass'''
