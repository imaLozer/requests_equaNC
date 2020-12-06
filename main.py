'''
Equation à effectuer : [0]*[1]^2 + [3][4][5]
'''
import sqrt
import requests, re, math

def requestConnect():

    global resultat
    global session

    session = requests.Session()

    jar = requests.cookies.RequestsCookieJar()
    jar.set('SMFCookie89', '[cookie]') #Attribuer le cookie à SMFCookie89
    session.cookies = jar

    r = session.get('https://www.newbiecontest.org/epreuves/prog/prog4.php') #récupérer le premier nombre

    resultat = r.text

    return resultat

def patternRX():

    list=[] #[0] * [1] del [2] ^2 + [3][4][5]

    #Output du resultat avec du REGEX, retire tous les char et les symboles pour n'avoir que des :digit:
    result = re.sub(r"[a-z]", "", resultat, flags=re.I)
    result2 = re.sub(r"\W","", result, flags = re.I)

    for i in result2:
        convertedResult = str(i) #résultat converti en int -> exemple :  "832152"
        list.append(convertedResult)

    list.pop(2) #retirer le troisième élément du tableau -> 2

    index0 = int(list[0])
    index01 = int(list[1])
    index1 = index01**2

    completeStr = list[2] + list[3] + list[4]

    toSquare = sqrt.toSqrt(index0, index1);

    result = toSquare + int(completeStr)
    j = str(result)

    flag = session.get("https://www.newbiecontest.org/epreuves/prog/verifpr4.php?solution=" + j) #flag

    print(flag.text)










requestConnect()
patternRX()
