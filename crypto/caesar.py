from helpers import alphabet_position, rotate_character

def encrypt(text, rot):
  new_msg = ""
  new_char = ""
  for letter in text:
    new_char = rotate_character(letter, rot)
    new_msg = new_msg + new_char
  return new_msg

def main():
  text = input("What message would you like to encode? ")
  rot = int(input("How much would you like to move the letters? "))
  print(encrypt(text, rot))

if __name__ == '__main__':
  main()