import random
import string
from Words import words


def  get_valid_word(words):
    word = random.choice(words) # Nesse não preciso colocar [] porque a lista ja existe em outro arquivo
    while '-' in words or ' ' in words: # loop pra impedir - traços e espaços em branco
        word = random.choice(words)

    return word.upper() # vai retornar como letras maiusculas

def Forca():
    word = get_valid_word(words)
    word_letters = set(word) # letters in the word
    alphabet = set(string.ascii_uppercase) # Lista pré determinada de letras maiusculas no alfabeto ingles
    used_letters = set() # O que o usuario chutou

    vida = 6

        # pegando o input do usuario
    while len(word_letters) > 0 and vida > 0:

        # Letras usadas
        # ' '.join(['a', 'b', 'cd']) --> 'a b cd'
        print('Você tem', vida,' vidas restantes, você ja usou essas letras: ', ' '.join(used_letters)) # O que esse .join() faz é transformar essa lista em uma string iteravel, separada seja o que for antes do .join()

        # Qual letra que é (is W - R D) letras que foram chutadas aparecem e as que não foram fiquem no formato
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Palavra atual: ',' '.join(word_list))

        user_letter = input('Chute a letra:  \n').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)

            if user_letter in word_letters:
                word_letters.remove(user_letter)

            else:
                vida = vida - 1 # tira uma vida se chutar arrado


        elif user_letter in used_letters:
            print('Você ja tentou essas letras. Tente novamente.')

        else:
            print('Letras invalidas tente novamente')
    # esse while gets here when len(word_letters) == 0

    if vida == 0: # aqui para o loop
        print('Você morreu, a palavra era:',word)
    else:
        print('Você chutou:', word, '!!')
    
user_input = input('Digite algo para iniciar: ')
Forca()