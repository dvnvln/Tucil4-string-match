import re
from nltk.tokenize import sent_tokenize
from kmp import *
from bm import *



def splitArr(teks):#memecah 1teks(paragraf) menjadi beberapa kalimat dengan memanfaatkan nltk
    splt = sent_tokenize(teks)
    return splt

def closestDig(kalimat,p):#method mencari potongan kalimat yang terdapat angka dan pattern dari user
    pattern = p.lower()
    sentence = kalimat.lower()
    pat = '[0-9]'
    result = re.search(genPattern(True,pat, pattern),sentence)
    if result is None:
            return ("no result")
    return result.group()

def getDNumber(matchClosest):#method mencari angka dari potongan kalimat
    pat =r' [0-9]*\.[0-9]+| [0-9]+'
    space = " "
    matchClosest = space + matchClosest 
    result = re.search(pat,matchClosest)
    if result is None:
            return ("no result")
    return result.group()

def findDate(sentence):#method mencari waktu dengan format hari tanggal waktu waktubagian
    regex = r"((Senin|Monday|Selasa|Tuesday|Rabu|Wednesday|Kamis|Thursday|Jumat|Friday|Sabtu|Saturday|Minggu|Sunday)(?:.)*?((\d{1,2}(\/|\-|\.)\d{1,2}(\/|\-|\.)\d{4})|(\d{1,2}( )(Jan|Januari|January|Feb|Februari|February|Mar|Maret|March|Apr|April|Mei|May|Jun|Juni|June|Jul|July|Juli|Aug|Agustus|August|Sep|September|Oct|Oktober|October|November|Nov|Dec|December|Desember)( )\d{4}))(?:.)*?(([0-1]\d|[2][0-3])((\:|\.)[0-5]\d){1,2})((?:.)*?WIB(?:.)*?|(?:.)*?WITA(?:.)*?| (?:.)*?WIT(?:.)*?|))"
    result = re.search(regex, sentence)
    if result is None:
        date = r"((\d{1,2}(\/|\-|\.)\d{1,2}(\/|\-|\.)\d{4})|(\d{1,2}( )(Jan|Januari|January|Feb|Februari|February|Mar|Maret|March|Apr|April|Mei|May|Jun|Juni|June|Jul|July|Juli|Aug|Agustus|August|Sep|September|Oct|Oktober|October|November|Nov|Dec|December|Desember)( )\d{4}))"
        result = re.search (date,sentence)
        if result is None:
            return ("no date")
    return result.group()

def searchRe(pattern,text):#mencari pattern dalam teks dengan regex
    pat = pattern.lower()
    txt = text.lower()
    reg = re.findall("{}".format(pat),txt)
    return (len(reg)>0)

def genPattern(isMultiple, pattern, lookup):
    sym = ""
    if isMultiple:
        sym = "+"
    return r"({pattern}{sym}(?:(?!( {pattern})).)*?{lookup}|{lookup}(?:(?! ({pattern}) ).)*?( {pattern}*\.{pattern}+| {pattern}{sym}))".format(pattern = pattern, sym = sym, lookup = lookup)
