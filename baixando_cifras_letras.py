
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import ssl

def modular(cifra, semitons=0):
    '''Altera a tonalidade da cifra.
    cifra: a cifra baixada
    semitons: o número de semitons de distância para a nova tonalidade (ascendentemente)'''    
    texto = str(cifra)
    for i in range(semitons):
        texto = re.sub('(<b>B)', '<b>_C', texto)
        texto = re.sub('(<b>_Cb)', '<b>B', texto)
        texto = re.sub('<b>A#', '<b>B', texto)
        texto = re.sub('(<b>A)', '<b>Bb', texto)
        texto = re.sub('(<b>Bbb)', '<b>A', texto)
        texto = re.sub('<b>G#', '<b>A', texto)
        texto = re.sub('(<b>G)', '<b>Ab', texto)
        texto = re.sub('(<b>Abb)', '<b>G', texto)
        texto = re.sub('<b>F#', '<b>G', texto)
        texto = re.sub('(<b>F)', '<b>F#', texto)
        texto = re.sub('(<b>E)', '<b>F', texto)
        texto = re.sub('(<b>Fb)', '<b>E', texto)
        texto = re.sub('<b>D#', '<b>E', texto)
        texto = re.sub('(<b>D)', '<b>Eb', texto)
        texto = re.sub('(<b>Ebb)', '<b>D', texto)
        texto = re.sub('<b>C#', '<b>D', texto)
        texto = re.sub('(<b>C)', '<b>C#', texto)
        texto = re.sub('(<b>_C)', '<b>C', texto)
        #Inversões
        texto = re.sub('(/B)', '/_C', texto)
        texto = re.sub('(/_Cb)', '/B', texto)
        texto = re.sub('/A#', '/B', texto)
        texto = re.sub('/A', '/Bb', texto)
        texto = re.sub('(/Bbb)', '/A', texto)
        texto = re.sub('/G#', '/A', texto)
        texto = re.sub('(/G)', '/Ab', texto)
        texto = re.sub('(/Abb)', '/G', texto)
        texto = re.sub('/F#', '/G', texto)
        texto = re.sub('(/F)', '/F#', texto)
        texto = re.sub('(/E)', '/F', texto)
        texto = re.sub('(/Fb)', '/E', texto)
        texto = re.sub('/D#', '/E', texto)
        texto = re.sub('(/D)', '/Eb', texto)
        texto = re.sub('(/Ebb)', '/D', texto)
        texto = re.sub('/C#', '/D', texto)
        texto = re.sub('(/C)', '/C#', texto)
        texto = re.sub('(/_C)', '/C', texto)            
    texto = re.sub('<.+?>', '', texto)
    return texto        

def baixar_cifra(musica,artista,semitons):
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    try:
        url = 'https://www.cifraclub.com.br/'+artista+'/'+musica+'/'
        html = urlopen(url, context=ctx).read()
        soup = BeautifulSoup(html, "html.parser")
        cifra = soup('pre')[0]
    except:
        return '<Cifra não encontrada. Tente alterar o nome do artista ou corrigir a grafia da música>'
    conteudo = modular(cifra,semitons=semitons)
    return conteudo

def baixar_letra(musica, artista):
    try:
        ctx = ssl.create_default_context()
        ctx.check_hostname = False
        ctx.verify_mode = ssl.CERT_NONE
        url = 'https://www.letras.com/'+artista+'/'+musica+'/'
        html = urlopen(url, context=ctx).read()
        soup = BeautifulSoup(html, "html.parser")
        letra = soup('div', {'class': "lyric-original font --lyrics --size18"})[0]
        letra=str(letra)
        letra=re.sub('<br/>', '\n', letra)
        letra=re.sub('<.+?>', '', letra)
        return letra
    except:
        return "<Letra não encontrada. Tente alterar o nome do artista ou corrigir a grafia da música>"

    
