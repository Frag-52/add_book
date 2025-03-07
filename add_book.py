def add_book(book_name, book_text):


    with open(f"Книги/{book_name}.txt", "w") as book_file:
        book_file.write(book_text)
        
        
book_title = input("Введите название книги:")
book_content = input("Введите текст книги:")
add_book(book_title, book_content)