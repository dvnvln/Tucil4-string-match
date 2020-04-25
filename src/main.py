import re
from kmp import *
from bm import *
from regx import *
'''
method algoritma boyer moore mengembalikan dictionary hasil yaitu tanggal angka dan kalimat
'''
def readBm(naskah,pattern):
    allSen = splitArr(naskah)
    arrTot =[]
    dateTemp = findDate(allSen[0])
    for j in range (len(allSen)):
        arrtemp =[]
        dict={}
        date =findDate(allSen[j])
        valid = boym(pattern,allSen[j])
        if valid:
            sentClose = closestDig(allSen[j],pattern)
            digit = getDNumber(sentClose)
            dict["angka"] = digit
            dict["kalimat"] =allSen[j]
            if (date =="no date"):
                dict["tanggal"] = dateTemp
            else:
                dict["tanggal"] = date
            arrTot.append(dict)
    return (arrTot)

'''
method algoritma Knuth-Morris-Pratt mengembalikan dictionary hasil yaitu tanggal angka dan kalimat
'''
def readKMP(naskah,pattern):
    allSen = splitArr(naskah)
    arrTot =[]
    dateTemp = findDate(allSen[0])
    for j in range (len(allSen)):
        arrtemp = []
        dict={}
        date =findDate(allSen[j])
        valid = kmp(pattern,allSen[j])
        if valid:
            sentClose = closestDig(allSen[j],pattern)
            digit = getDNumber(sentClose)
            dict["angka"] = digit
            dict["kalimat"] =allSen[j]
            if (date =="no date"):
                dict["tanggal"] = dateTemp
            else:
                dict["tanggal"] = date
            arrTot.append(dict)
    return (arrTot)

'''
method algoritma regex mengembalikan dictionary hasil yaitu tanggal angka dan kalimat
'''
def readRegx(naskah,pattern):
    allSen = splitArr(naskah)
    arrTot =[]
    dateTemp = findDate(allSen[0])
    for j in range (len(allSen)):
        arrtemp=[]
        dict={}
        date =findDate(allSen[j])
        valid = searchRe(pattern,allSen[j])
        if valid:
            sentClose = closestDig(allSen[j],pattern)
            digit = getDNumber(sentClose)
            dict["angka"] = digit
            dict["kalimat"] =allSen[j]
            if (date =="no date"):
                dict["tanggal"] = dateTemp
            else:
                dict["tanggal"] = date
            arrTot.append(dict)
    return (arrTot)

