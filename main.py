import wikipedia

def list_writer(ll: list):
    print("\n")
    for i in range(0, len(ll)):
        print(i+1, ll[i], "\n")



print("1. Summary.\n2. API_URL.\n3. Search (list).\n4. Page title.\n5. Page links (list).\n6. Page content.\n7. Page image (list).\n8. Page references (list).")

choice = int(input("\nEnter your choice: "))
"""
1. Summary.
2. API_URL.
3. Search (list).
4. Page title.
5. Page links (list).
6. Page content.
7. Page image (list).
8. Page references (list).
"""
if choice == 1:
    topic: str = input("Enter your Summary topic: ")
    print("\n", wikipedia.summary(topic), "\n")

elif choice == 2:
    print("\nAPI_URL is given below: ")
    print(wikipedia.API_URL, "\n")

elif choice == 3:
    topic: str = input("Enter your Search topic: ")
    tt: list = wikipedia.search(topic)
    list_writer(tt)



elif choice == 4:
    topic: str = input("Enter your Page's Title topic: ")
    print("\n", wikipedia.page(topic).title, "\n")

elif choice == 5:
    topic: str = input("Enter your Page's Links topic: ")
    tt: list = wikipedia.page(topic).links
    list_writer(tt)

elif choice == 6:
    topic: str = input("Enter your Page's content topic: ")
    print(wikipedia.page(topic).content)

elif choice == 7:
    topic: str = input("Enter your topic for page's image: ")
    tt: list = wikipedia.page(topic).images
    list_writer(tt)

elif choice == 8:
    topic: str = input("Enter your topic for page's References: ")
    tt: list = wikipedia.page(topic).references
    list_writer(tt)

jfcdjs = input("Hit enter to close...")
