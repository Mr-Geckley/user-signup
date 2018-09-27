from helpers import alphabet_position, rotate_character
    
def encrypt(msg, key):
  x = 0
  new_msg = ""
  new_char = ""
  for letter in msg:
    new_char = rotate_character(letter, alphabet_position(key[x]))
    if new_char.isalpha():
      x += 1
    if x > len(key) -1:
      x = 0
    new_msg = new_msg + new_char
  return new_msg

def main():
    msg = input("Tell me the secret you want to keep. ")
    key = input("What is the encoding key?")
    print(encrypt(msg, key))

if __name__ == '__main__':
    main()