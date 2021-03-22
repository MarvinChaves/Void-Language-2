# creation day = 13/03/2021
# last update = 19/03/2021
# version = 0.1.0
# goal = 700 lines
# lines = 581

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

       1 - userLog function added

    }

    18/03/2021 {

        1 - 1 new function

    }

    19/03/2021 {

        1 - bug fix
        2 - group function added
        3 - varsList added
        4 - if function added

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

            math log example { you can make the math more useful place with this:
                                (Test yourself!!)

                log 2 + 2

                console {
                    4
                } 
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
    cont = False
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
            cont = False

    except Exception as erro:
        if type(str(functionName[1])) == str:
            isMathing = False
            cont = True

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
        
    if cont:
        if functionName[2] == '+':
            sleep(1)
            print('==' * 50)
            sleep(1)
            print(str(functionName[1]) + str(functionName[3]))
            isMath = True
    
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
        
        elif type(int(functionName[3])) == int:
            intValue = True

        elif type(float(functionNam[3])) == float:
            floatValue = True
        
        elif type(bool(functionName[3])) == bool:
            boolValue = True

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
    o = 0
    for string in varList:
        print(f"\n{varList[o][0]} = {''.join(varList[o][1])}")
        o += 1



def group():
    got = False
    if functionName[1] == 'var':
        o = 0
        while True:
            if functionName[2] in varList[o]:
                got = True
            
            else:
                o += 1
                
            if got:
                sleep(1)
                print('==' * 50)
                sleep(1)
                groupList = []
                for string in varList[o][1]:
                    for value in string:
                        groupList.append(value)


                try:
                    value = value.split()
                    varList[o][1] = int(value)
                    if type(varList[o][1]) == int:
                        print(f'Type of {functionName[2]}: \n\n {cyan} <int>{white}')
                        break

                except:
                    try:
                        varList[o][1] = float(value)
                        if type(varList[o][1]) == float:
                            print(f'Type of {functionName[2]}: \n\n {cyan} <float>{white}')
                            break
                
                    
                    except:
                        try:
                            word = ''.join(groupList)
                            if word == 'True' or word == 'False':
                                print(f'Type of {functionName[2]}: \n\n {cyan} <bool>{white}')
                                break
            
                        
                        except:
                            try:
                                if type(varList[o][1]) == list:
                                    print(f'Type of {functionName[2]}: \n\n {cyan} <list>{white}')
                                    break
                        

                            except:
                                try:
                                    varList[o][1] = str(value)
                                    if type(varList[o][1]) == str:
                                        print(f'Type of {functionName[2]}: \n\n {cyan} <str>{white}')
                                        break
                                
                                except:
                                    pass

                                else:
                                    pass

                            else:
                                pass
                        else:
                            pass
                    
                    else:
                        pass
                
                else:
                    pass
                    

# ============================================== If def ==============================================

def If():

    def main():
        o = 0
        p = 0
        breaker = False
        
        for string in varList[o][0]:
            
            while True:
                if breaker:
                    break
                else:
                    pass

                if functionName[1] in varList[o][0]:
                    for item in varList[p][0]:
                        while True:
                            if breaker:
                                break
                            else:
                                pass

                            if functionName[3] in varList[p][0]:
                                if functionName[4] == 'log':
                                    if functionName[5] == 'var':
                                        o = 0
                                        for value in varList:
                                            if breaker:
                                                break
                                            else:
                                                pass

                                            while True:
                                                if breaker:
                                                    break
                                                else:
                                                    pass

                                                if functionName[6] in varList[o]:
                                                    if functionName[2] == '==':
                                                        if varList[o][1] == varList[p][1]:
                                                            sleep(1)
                                                            print('==' * 50)
                                                            sleep(1)
                                                            print(' '.join(varList[o][1]))
                                                            breaker = True
                                                            break
                                                    
                                                    elif functionName[2] == '!=':
                                                        if varList[o][1] != varList[p][1]:
                                                            sleep(1)
                                                            print('==' * 50)
                                                            sleep(1)
                                                            print(' '.join(varList[o][1]))
                                                            breaker = True
                                                            break
                                                    
                                                    elif functionName[2] == '>':
                                                        if varList[o][1] > varList[p][1]:
                                                            sleep(1)
                                                            print('==' * 50)
                                                            sleep(1)
                                                            print(' '.join(varList[o][1]))
                                                            breaker = True
                                                            break
                                                    
                                                    elif functionName[2] == '<':
                                                        if varList[o][1] < varList[p][1]:
                                                            sleep(1)
                                                            print('==' * 50)
                                                            sleep(1)
                                                            print(' '.join(varList[o][1]))
                                                            breaker = True
                                                            break
                                                    
                                                    elif functionName[2] == '>=':
                                                        if varList[o][1] >= varList[p][1]:
                                                            sleep(1)
                                                            print('==' * 50)
                                                            sleep(1)
                                                            print(' '.join(varList[o][1]))
                                                            breaker = True
                                                            break
                                                    
                                                    elif functionName[2] == '<=':
                                                        if varList[o][1] <= varList[p][1]:
                                                            sleep(1)
                                                            print('==' * 50)
                                                            sleep(1)
                                                            print(' '.join(varList[o][1]))
                                                            breaker = True
                                                            break
                                                    
                                                    else:
                                                        pass

                                                else:
                                                    o += 1

                                    elif functionName[5] != 'var':
                                        try:
                                            if type(int(functionName[5])) == int:
                                                if functionName[6] == '+':
                                                    sleep(1)
                                                    print('==' * 50)
                                                    sleep(1)
                                                    print(int(functionName[5]) + int(functionName[7]))
                                                    breaker = True
                                                    break

                                                elif functionName[6] == '-':
                                                    sleep(1)
                                                    print('==' * 50)
                                                    sleep(1)
                                                    print(int(functionName[5]) - int(functionName[7]))
                                                    breaker = True
                                                    break
                                                    
                                                elif functionName[6] == '*':
                                                    sleep(1)
                                                    print('==' * 50)
                                                    sleep(1)
                                                    print(int(functionName[5]) * int(functionName[7]))
                                                    breaker = True
                                                    break

                                                elif functionName[6] == '/':
                                                    sleep(1)
                                                    print('==' * 50)
                                                    sleep(1)
                                                    print(int(functionName[5]) / int(functionName[7]))
                                                    breaker = True
                                                    break
                                        except:
                                            if type(str(functionName[5])) == str:
                                                if len(functionName) == 6:
                                                    sleep(1)
                                                    print('==' * 50)
                                                    sleep(1)
                                                    print(str(functionName[5]))
                                                    breaker = True
                                                    break
                                                
                                                elif len(functionName) > 6 :
                                                    sleep(1)
                                                    print('==' * 50)
                                                    sleep(1)
                                                    leng = len(functionName)
                                                    m = 5
                                                    for value in range(leng - 5):
                                                        print(functionName[m], end=' ')
                                                        m += 1
                                                        if m == leng:
                                                            breaker = True
                                                            break
                                
                                elif functioName[4] == 'var':
                                    
                                    if functionName[6] == '=':
                                        varName = functionName[5]
                                        varValue = functionName[7]
                                                varList.append([varName, [varValue]])
                                                print(varList)
                             
                                                    
                                                    break
                                                        

                                        
                                        else:
                                            pass
                                    
                                    else:
                                        print('False')
                                    

                            else:
                                p += 1
                
                else:
                    o += 1

    condition = False
    breaker = False

    if functionName[2] == '==':
        main()


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
    
    elif functionName[0] == 'group':
        group()
    
    elif functionName[0] == 'if':
        If()
    
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



