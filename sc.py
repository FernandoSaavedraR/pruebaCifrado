import base64

def cifrar64(cadena):

    cadena_utf = cadena.encode('utf-8')
    cadena_codificada = base64.b64encode(cadena_utf)
    return cadena_codificada.decode()


def descifrar64(cadena):
    cadena_decodificada = base64.b64decode(cadena.encode('utf-8'))
    return cadena_decodificada


def cifrar64M(cadena,diccionario):
    caracteres = [cadena[i] for i in range(0,len(cadena))]
    caracteresASCII = [ord(x) for x in caracteres]
    caracteresbin = [bin(x) for x in caracteresASCII]
    caracteresbinfixed = [x[2:len(x)] for x in caracteresbin]
    caracteresbinsize = [x.rjust(8,'0') for x in caracteresbinfixed ]
    cadenabin = ''.join(caracteresbinsize)
    seises = [cadenabin[i:i+6] for i in range(0,len(cadenabin),6)]
    seisesFixed = [x.ljust(6,'0') for x in seises ]
    seisesInt = [int(x,2) for x in seisesFixed]
    seisesStr = [diccionario[x] for x in seisesInt]
    cadenaC = ''.join(seisesStr)
    calculo = len(seises[len(seises)-1])%3
    cadenaP = cadenaC+('='*calculo)
    return cadenaP


def descifrar64M(cadena,diccionario):
    diccionarioR = dict((val,key)for key,val in diccionario.items())
    caracteres = [cadena[i] for i in range(0,len(cadena))]
    padding = len([i for i,x in enumerate(caracteres) if x=='=' ])
    caracteresF = [x for x in caracteres if x !='=']
    caracteres64 = [diccionarioR[x] for x in caracteresF]
    caracteresbin = [bin(x) for x in caracteres64]
    caracteresbinfixed = [x[2:len(x)] for x in caracteresbin]
    caracteresbinsize = [x.rjust(8,'0') for x in caracteresbinfixed]
    caracteresbinresize = [x[2:len(x)] for x in caracteresbinsize]
    cadenabin = ''.join(caracteresbinresize)+('0'*2*padding)
    ochos = [cadenabin[i:i+8] for i in range(0,len(cadenabin),8)]
    ochosFilt = [x for x in ochos if len(x)==8]
    ochosInt = [int(x,2) for x in ochosFilt]
    caracteresFinal=[chr(x) for x in ochosInt]
    cadena = ''.join(caracteresFinal)
    return cadena

    
if __name__ == "__main__":
    diccionario={
        0:'A',
        1:'B',
        2:'C',
        3:'D',
        4:'E',
        5:'F',
        6:'G',
        7:'H',
        8:'I',
        9:'J',
        10:'K',
        11:'L',
        12:'M',
        13:'N',
        14:'O',
        15:'P',
        16:'Q',
        17:'R',
        18:'S',
        19:'T',
        20:'U',
        21:'V',
        22:'W',
        23:'X',
        24:'Y',
        25:'Z',
        26:'a',
        27:'b',
        28:'c',
        29:'d',
        30:'e',
        31:'f',
        32:'g',
        33:'h',
        34:'i',
        35:'j',
        36:'k',
        37:'l',
        38:'m',
        39:'n',
        40:'o',
        41:'p',
        42:'q',
        43:'r',
        44:'s',
        45:'t',
        46:'u',
        47:'v',
        48:'w',
        49:'x',
        50:'y',
        51:'z',
        52:'0',
        53:'1',
        54:'2',
        55:'3',
        56:'4',
        57:'5',
        58:'6',
        59:'7',
        60:'8',
        61:'9',
        62:'+',
        63:'/',
    }
    cadena = 'https://www.saes.upiicsa.ipn.mx/'
    #cadena = 'Man is distinguished, not only by his reason, but by this singular passion from other animals, which is a lust of the mind, that by a perseverance of delight in the continued and indefatigable generation of knowledge, exceeds the short vehemence of any carnal pleasure.'
    #cadena = '1234567890'
    cifradaL = cifrar64(cadena)
    descifradaL = descifrar64(cifradaL)
    cifradoM = cifrar64M(cadena,diccionario)
    descfiradaM = descifrar64M (cifradoM,diccionario)
    print(('liberia cif: '+cifradaL))
    print(('manual cif: '+cifradoM))
    print(('liberia desc: '+descifradaL.decode()))
    print(('manual desc: '+descfiradaM))