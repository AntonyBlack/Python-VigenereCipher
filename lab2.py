from collections import Counter
from re import sub

def getFile(fileName):
    File = open(fileName)
    return File

def getText(File, alph):
    text = File.read()
    text = text.lower()
    text = sub("[^а-я]", "", text)
    File.close()
    return text

def textEncryptionVigenere(text, key, alph):
    encryptedText = ""
    step=0
    for i in range(0, len(text)):
        if i % len(key) == 0:
            step += len(key)
        encryptedText += alph[(alph.index(text[i])+alph.index(key[i-step]))%len(alph)]
    return encryptedText    


def affinityIndex(text):
    affinityIndex = 0
    Dict = dict(Counter(text))
    for i in Dict:
        affinityIndex += (Dict[i]*(Dict[i]-1))
    affinityIndex /= (len(text)*(len(text)-1))
    return affinityIndex

def guessTheKey(text, alph):
    posibleKeys = []
    mcl = 'оаени'
    for keySize in range(2,30):
        affinityIndexForBlock = affinityIndex(text[::keySize])
        print(str(affinityIndexForBlock) + ': ' +  str(keySize))
        if (0.0553-affinityIndexForBlock) < 0.0015:      #0.0553 - индекс соответствия для русского языка
            print("Key size: " + str(keySize))
            for i in range(0,len(mcl)):             #самые частые буквы, согласно лабе №1
                posibleKeys.append('')                  # 'о': 0.114843 , 'а': 0.0886082, 'е': 0.0791515, 'н': 0.0632887, 'и': 0.0626786
                for j in range(0, keySize):
                    posibleKeys[i] += alph[(alph.index(Counter(text[j::keySize]).most_common()[0][0])-alph.index(mcl[i]))%len(alph)]
            for key in posibleKeys:        
                print(str(posibleKeys.index(key)+1)+ '. ' + key)
            while(True):
                print('Which key is correct: ')
                try:
                    key = int(input())
                    return posibleKeys[key-1]
                except IndexError:
                    print("Enter number 1-5: ")
                except ValueError:
                    print("Enter number 1-5: ")           
                            
def textDecryptionVigenere(text, key, alph):
    decryptedText = ""
    step=0
    for i in range(0, len(text)):
        if i % len(key) == 0:
            step += len(key)
        decryptedText += alph[(alph.index(text[i])-alph.index(key[i-step]))%len(alph)]
    print(decryptedText)    
                 
def main():
    alph='абвгдежзийклмнопрстуфхцчшщъыьэюя'
    key1 = 'шв'
    key2 = 'ыпф'
    key3 = 'пукр'
    key4 = 'ырнсы'
    key5 = 'рагцлвщкиыгптплв'
    text = open('text.txt', encoding = 'utf-8')
    text = getText(text, alph)
    print('key[2]',affinityIndex(textEncryptionVigenere(text, key1, alph)))
    print('key[3]',affinityIndex(textEncryptionVigenere(text, key2, alph)))
    print('key[4]',affinityIndex(textEncryptionVigenere(text, key3, alph)))
    print('key[5]',affinityIndex(textEncryptionVigenere(text, key4, alph)))
    print('key[16]',affinityIndex(textEncryptionVigenere(text, key5, alph)))
    decrypt = getText(getFile("variant15.txt"), alph)
    textDecryptionVigenere(decrypt, guessTheKey(decrypt, alph), alph)

    
main()
