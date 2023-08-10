# Definir um dicionário com as letras e seus equivalentes em Código Morse
MORSE_CODE_DICT = { 'A':'.-', 'B':'-...', 'C':'-.-.', 'D':'-..',
 'E':'.', 'F':'..-.', 'G':'--.', 'H':'....', 'I':'..', 'J':'.---',
  'K':'-.-', 'L':'.-..', 'M':'--', 'N':'-.', 'O':'---', 'P':'.--.',
   'Q':'--.-', 'R':'.-.', 'S':'...', 'T':'-', 'U':'..-', 'V':'...-',
    'W':'.--', 'X':'-..-', 'Y':'-.--', 'Z':'--..', '1':'.----',
     '2':'..---', '3':'...--', '4':'....-', '5':'.....', '6':'-....',
      '7':'--...', '8':'---..', '9':'----.', '0':'-----'}

def encrypt(message):
    """Função que converte um texto em código Morse"""
    cipher = ''
    for letter in message:
        if letter != ' ':
            # procura a letra no dicionário e adiciona o equivalente em Morse à mensagem codificada
            cipher += MORSE_CODE_DICT[letter] + ' '
        else:
            # Adiciona um espaço se a letra for um espaço em branco
            cipher += ' '

    return cipher


mensagem = str(input("""
               _ _                                             
              | (_)                                            
  ___ ___   __| |_  __ _  ___  
 / __/ _ \ / _` | |/ _` |/ _ \ 
| (_| (_) | (_| | | (_| | (_) |
 \___\___/ \__,_|_|\__, |\___/ 
                    __/ |      
                   |___/       


  _ __ ___   ___  ___  ___  ____
 | '_ ` _ \ / _ \|  _\/ __|/ ___/
 | | | | | | (_) | |  \__ \  _/
 |_| |_| |_|\___/|_|  |___/\___/
                        
																					
Texto a ser Codificado: """)).upper()

# Exemplo de uso

mensagem_codificada = encrypt(mensagem)

print(f"\n\nMensagem Codificada:{mensagem_codificada}\n\n")
