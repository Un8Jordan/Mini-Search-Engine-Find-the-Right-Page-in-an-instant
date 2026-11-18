from articles import ARTICLES


print("=========================================")
print("          MINI SEARCH ENGINE             ")
print("=========================================")


# Breaking the text into words
def tokenize(text):
    words = text.lower().split()
    return words

index = {}
for x, (title , text) in enumerate(ARTICLES):
    words = tokenize(title + " " + text)

    for word in words:
        i = i.strip(".?/\|!@#$%^&*':;,.")

        if i not in index:
            index[i] = []

        if x not in index[i]:
            index[i].append(x)




# History of Pizza
def  search(query):
    words = tokenize(query)
    results = []

    for i in words:
        i = i.strip(".?/\|!@#$%^&*':;,.")

        if i in index:
            for x in index[i]:
                if x not in results:
                    results.append(x)

    return results

while True:
    query = input("\n Enter search words OR quit to stop): ")

    if query.lower() == "quit":
        print("Thank you for searching! Goodbye.")
        break

    results = search(query)

    if results:
        print("\n Search Results:")
        for i in results:
            title, text = ARTICLES[i]
            print("\n Title: ", title)
            print("Content: ", text)

    else:

        print("No matching articles found.")