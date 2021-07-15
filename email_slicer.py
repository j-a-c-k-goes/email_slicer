"""
Take email id an input
Perform slicing operation on input
Input => someone@something.com
Output => username, domain
"""

# .......................................................................... Main Function
def user_email():

    fails = 0
    max_fails = 3
    at_symbol ='@'
    
    email = str(input('enter your email: ').strip()) # remove spacing on both sides of string

    while at_symbol not in email:

        fails += 1
        print("{} does not contain an {} symbol".format(email, at_symbol))
        print("please use a valid email (example: someone@something.domain)")
        print("you have {} attempts left".format(max_fails - fails))
        email = str(input("enter your email: ").strip())

        if fails >= max_fails:

            exit_message = "max fails reached.\nexiting program; goodbye."
            print(exit_message)
            exit()
            break

    user_name = email[:email.index(at_symbol)] # slice up to @ symbol
    domain = email[email.index(at_symbol) + 1:] # slice from @ symbol

    print('user_name: {}\tdomain: {}'.format(user_name, domain))
    return temp
# .......................................................................... Sub functions
# .......................................................................... On Run, Export
if __name__ == "__main__":
    user_email()
# .......................................................................... Bugs
# .......................................................................... Updates


