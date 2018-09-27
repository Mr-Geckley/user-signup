def get_initials(full_name):
    name_list = full_name.split()
    returned_initials = ""
    for name in name_list:
        returned_initials = returned_initials + name[0]
    returned_initials = returned_initials.upper()
    return returned_initials

def main():
    name = input("what is your name?")

    get_initials(name)

    print(get_initials(name))
  
if __name__ == '__main__':
    main()