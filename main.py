#### Simple Morse Converter

#Created Dictionary
morse_dict = {
              "A": ".-",
              "B": "-...",
              "C": "-.-.",
              "D": "-..",
              "E": ".",
              "F": "..-.",
              "G": "--.",
              "H": "....",
              "I": "..",
              "J": ".---",
              "K": "-.-",
              "L": ".-..",
              "M": "--",
              "N": "-.",
              "O": "---",
              "P": ".--.",
              "Q": "--.-",
              "R": ".-.",
              "S": "...",
              "T": "-",
              "U": "..-",
              "V": "...-",
              "W": ".--",
              "X": "-..-",
              "Y": "-.--",
              "Z": "--..",
              "0": "-----",
              "1": ".----",
              "2": "..---",
              "3": "...--",
              "4": "....-",
              "5": ".....",
              "6": "-....",
              "7": "--...",
              "8": "---..",
              "9": "----.",
            " " : "/" ,
              }

#Created function which converts word or sentence into morse code
def morser():
    word = input('Please write your word/sentence to convert: ')
    morse_code = ''
    for letter in word:
        morse_code += morse_dict[letter.capitalize()]
        morse_code += ' '

    print(f'Here your morse code: \n{morse_code}')

#Create while loop to continues work with asking user to continue or not ))))))
end_morser = False
while not end_morser:
    morser()
    ask = input('Would you like to continue? Type ["Y" or "N"]:')
    if ask == 'N':
        print('Bye! Bye!')
        end_morser = True