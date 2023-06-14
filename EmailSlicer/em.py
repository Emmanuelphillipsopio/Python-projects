#this program takes in an email and slicies it into user name,domain and extension
#collect email from the user
#split the email using the @

def main():
    print("")
    print("Welcome to the Email slicer ")
    print("")
while True:
    main()
    email_input = input("Input your Email address: ")

    (username, domain) = email_input.split("@")
    (domain, extension) = domain.split(".")

    print("Username: ", username)
    print("Domain: ", domain)
    print("Extension: ", extension)
