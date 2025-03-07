def add_book(book_name, book_text):
    
    with open("book.txt","a") as books_file:
        books_file.write(f"{book_name}\n")

    with open(f"{book_name}.txt", "w") as book_file:
        book_file.write(book_text)
        
        
    with open(f"{book_name}.txt", "r") as book_file:
        print(books_file.read())
book_title = input("Введите название книги:")
book_content = input("Введите текст книги:")
add_book(book_title, book_content)