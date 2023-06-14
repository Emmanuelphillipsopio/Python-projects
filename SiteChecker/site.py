#Recieves a url and returns a respone 
import urllib.request as urllib

def main(url):
    print("")
    print("Checking connectivity")

    response = urllib.urlopen(url)
    print(f"Connected to {url} successfully")
    print(f"The response code was {response.getcode()}")
    print("")

print("")
print("This is a site connectivity checker program")
input_url = input("Input url: ")
main(input_url)