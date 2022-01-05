def newEntry(n:int, phoneBook: dict):
    for i in range(n):
        entry = input().split()
        phoneBook.update({entry[0].lower():entry})


def queryEntry(name: str, phoneBook: dict):
    entry = phoneBook.get(name.lower(),phoneBook['DNE'])
    if entry != phoneBook['DNE']:
        return f"{entry[0]}={entry[1]}"
    return entry
    


def main():
    phoneBook = {"DNE":"Not found"}
    n = int(input())
    newEntry(n, phoneBook)

    _temp = "temp"
    while _temp != "":
        try:
            _name = input()
        except EOFError:
            _name = ""
        if _name == "":
            _temp =""
        else:
            print(queryEntry(_name,phoneBook))


if __name__ == "__main__":
    main()