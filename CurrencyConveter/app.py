def main():
    print("")
    print("Currency conveter(USD to Pounds)")

    dollars = eval(input("Enter the amount in USD: "))
    pounds = convert_to_pounds(dollars)
    print(f"That is {pounds} ponuds")
    print("")

convert_to_pounds = lambda dollars: dollars * 0.82

main()