class Library:
    def __init__(self,list,name):
        self.bookslist=list
        self.name =name
        self.lendDict={}

    def displayBooks(self):
        print(f"In {self.name} we have the following books")
        for book in self.bookslist:
            print(book)
    def lendBooks(self,user,book):
        if book not in self.lendDict.keys():
            self.lendDict.update({book:user})
            print("you can lend this book :)")
        else:
            print(f"Book is already taken by {self.lendDict[book]}")
    def addBooks(self,book):
        self.bookslist.append(book)
        print("The book has been added to the list")
    def returnBooks(self,book):
        self.lendDict.pop(book)
        print("your book has been returned")


if __name__=='__main__':
    saima= Library(['python','C++','Java','DSA','problem solving'],"saima's library")
    while(True):
        print(f"Welcome to {saima.name} . Enter your choice to continue")
        print("1.Display Books")
        print("2.Lend Books")
        print("3.Add Books")
        print("4.Return Books")
        user_choice=input()
        if user_choice not in ['1','2','3','4']:
            print("Please enter a valid option")
            continue

        else:
            user_choice=int(user_choice)

        if user_choice==1:
            saima.displayBooks()
        elif user_choice==2:
            book=input("Enter the name of the book:")
            user=input("Enter your name:")
            saima.lendBooks(user,book)
        elif user_choice==3:
            book=input("Enter the name of the book you want to add:")
            saima.addBooks(book)
        elif user_choice==4:
            book=input("Enter the name of the book you want to return:")
            saima.returnBooks(book)

        else:
            print("Not a valid option")
        print("press q to exit and c to continue")
        user_choice2=""
        while (user_choice2!="q" and user_choice2!="c"):
            user_choice2=input()
            if user_choice2=="q":
                exit()
            elif user_choice2=="c":
                continue
