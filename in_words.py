Nm = ['','один','два','три','чотири',"п'ять",'шість','сім','вісім',"дев'ять",'десять']
Nf = ['','одна','дві','три','чотири',"п'ять",'шість','сім','вісім',"дев'ять",'десять']
Nt = ['десять','одинадцять','двонадцять','тринадцять','чотирнадцять',"п'ятнадацять",'шістнадцять','сімнадцять','вісімнадацять',"дев'ятнадацять",'двадцять']
NN = ['','десять','двадцять','тридцять','сорок',"п'ятьдесят",'шістьдесят','сімдесят','вісімдесят',"дев'яносто",'сто']
NNN = ['','сто','двісті','триста','чотириста',"п'ятьсот",'шістьсот','сімсот','вісімсот',"дев'ятьсот",'тисяча']

UAH = ['гривень','гривня','гривні','гривні','гривні','гривень','гривень','гривень','гривень','гривень',]
THO = ['тисяч','тисяча','тисячі','тисячі','тисячі','тисяч','тисяч','тисяч','тисяч','тисяч','тисяч',]
MLN = ['мільонів','мільон','мільона','мільона','мільона','мільонів','мільонів','мільонів','мільонів','мільонів','мільонів',]
MRD = ['мільярдів','мільярд','мільярда','мільярда','мільярда','мільярдів','мільярдів','мільярдів','мільярдів','мільярдів','мільярдів',]
t = " " # just space

import sys
import math

# num_1 = int(number) % (10**3)           # UAH
# num_2 = (int(number) // 10**3) % 10**3  # thousands
# num_3 = (int(number) // 10**6) % 10**3  # millions
# num_4 = (int(number) // 10**9) % 10**3  # billions

# digit = 1 - UAH
# digit = 2 - thousands
# digit = 3 - millions
# digit = 4 - billions

# making word string 
def num_in_words_UAH (num_e):
    word = ""
    if num_e < 10:
        word = Nf[num_e] + t + UAH[num_e]
    elif num_e < 20:
        word = Nt[num_e-10] + t + UAH[9]     
    elif num_e < 101:    
        word = NN[num_e//10] + t + Nf[num_e % 10] + t + UAH[num_e % 10]
    elif num_e < 1001:
        word = NNN[num_e//100] + t + NN[(num_e % 100) // 10] + t + Nf[num_e %10] + t + UAH[num_e %10]
    return (word)
    
def num_in_words_THO (num_e):
    word = ""
    if num_e < 10:
        word = Nf[num_e] + t + THO[num_e]
    elif num_e < 20:
        word = Nt[num_e-10] + t + THO[9]     
    elif num_e < 101:    
        word = NN[num_e//10] + t + Nf[num_e % 10] + t + THO[num_e % 10]
    elif num_e < 1001:
        word = NNN[num_e//100] + t + NN[(num_e % 100) // 10] + t + Nf[num_e %10] + t + THO[num_e %10]
    return (word)

def num_in_words_MLN (num_e):
    word = ""
    if num_e < 10:
        word = Nm[num_e] + t + MLN[num_e]
    elif num_e < 20:
        word = Nt[num_e-10] + t + MLN[9]     
    elif num_e < 101:    
        word = NN[num_e//10] + t + Nm[num_e % 10] + t + MLN[num_e % 10]
    elif num_e < 1001:
        word = NNN[num_e//100] + t + NN[(num_e % 100) // 10] + t + Nm[num_e %10] + t + MLN[num_e %10]
    return (word)

def num_in_words_MRD (num_e):
    word = ""
    if num_e < 10:
        word = Nm[num_e] + t + MRD[num_e]
    elif num_e < 20:
        word = Nt[num_e-10] + t + MRD[9]     
    elif num_e < 101:    
        word = NN[num_e//10] + t + Nm[num_e % 10] + t + MRD[num_e % 10]
    elif num_e < 1001:
        word = NNN[num_e//100] + t + NN[(num_e % 100) // 10] + t + Nm[num_e %10] + t + MRD[num_e %10]
    return (word)

    word = ""
    print ('num_e= ',num_e)
    if num_e < 10:
        word = Nf[num_e] + t + MLN[num_e]
    elif num_e < 20:
        word = Nt[num_e-10] + t + MLN[9]     
    elif num_e < 101:    
        word = NN[num_e//10] + t + Nf[num_e % 10] + t + MLN[num_e % 10]
    elif num_e < 1001:
        word = NNN[num_e//100] + t + NN[(num_e % 100) // 10] + t + Nf[num_e %10] + t + MLN[num_e %10]
    return (word)

    word = ""
    print ('num_e= ',num_e)
    if num_e < 10:
        word = Nf[num_e] + t + THO[num_e]
    elif num_e < 20:
        word = Nt[num_e-10] + t + THO[9]     
    elif num_e < 101:    
        word = NN[num_e//10] + t + Nf[num_e % 10] + t + THO[num_e % 10]
    elif num_e < 1001:
        word = NNN[num_e//100] + t + NN[(num_e % 100) // 10] + t + Nf[num_e %10] + t + THO[num_e %10]
    return (word)

def num_in_words (sum):
    number = sum
    num_i = int(number)
    
    if number >= 10**12 or number < 0:
        result =  'Число за пределами допустимого диапазона'

    NUM =[int(number) % (10**3),(int(number) // 10**3) % 10**3,(int(number) // 10**6) % 10**3,(int(number) // 10**9) % 10**3]
    DIG = ['UAH','THO','MLN','MRD']
    RES = []
  
    # separating fraction part
    if (round (number - num_i,2)*100) ==0: 
        num_f = '00'
    else:
        num_f = str(int((round ((number - num_i)*100,0))))
    num_kop = ' '+str(num_f) + ' коп.'

    if NUM[0] == 0:
        RES.append("")
    else:
        RES.append(num_in_words_UAH(NUM[0]))

    if NUM[1] == 0:
        RES.append("")
    else:
        RES.append(num_in_words_THO(NUM[1]))

    if NUM[2] == 0:
        RES.append("")
    else:
        RES.append(num_in_words_MLN(NUM[2]))

    if NUM[3] == 0:
        RES.append("")
    else:
        RES.append(num_in_words_MRD(NUM[3]))


    result = RES[3] + " " + RES[2] + " " + RES[1] + " " + RES[0] + " " + num_kop
    result =  result.replace("  "," ")
    return result