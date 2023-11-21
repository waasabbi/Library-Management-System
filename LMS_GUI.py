from tkinter import *
import sqlite3
from dateutil.relativedelta import relativedelta
from datetime import date, timedelta, datetime

# cancel button to close the window


def cancel(Window):
    Window.destroy()


# create a font
ourFont = ("Helvetica", 14)

# function to check out a book


def checkout_book():

    # create variables to hold the dates
    branch_id = StringVar()
    book_id = StringVar()
    card_no = StringVar()
    date_out = StringVar()
    due_date = StringVar()

    print("Checking out a book")

    # create a window
    w1 = Tk()
    w1.title("Check out a book")
    w1.geometry("600x500")

    # create a label
    text = Label(w1, text="Check out a book", font=ourFont)
    text.grid(row=0, column=1, padx=10, pady=10, sticky='we')

    # create a label for the branch id
    branch_id_label = Label(w1, text="Branch Id", font=ourFont)
    branch_id_label.grid(row=1, column=0, padx=10, pady=10, sticky='we')

    # create a text field for the branch id and assign it to branch_id
    branch_id_entry = Entry(w1, textvariable=branch_id, font=ourFont)
    branch_id_entry.grid(row=1, column=1, padx=10, pady=10, sticky='we')

    # create a label for the book id
    book_id_label = Label(w1, text="Book Id", font=ourFont)
    book_id_label.grid(row=2, column=0, padx=10, pady=10, sticky='we')

    # create a text field for the book id and assign it to book_id
    book_id_entry = Entry(w1, textvariable=book_id, font=ourFont)
    book_id_entry.grid(row=2, column=1, padx=10, pady=10, sticky='we')

    # create a label for the card number
    card_no_label = Label(w1, text="Card No", font=ourFont)
    card_no_label.grid(row=3, column=0, padx=10, pady=10, sticky='we')

    # create a text field for the card number and assign it to card_no
    card_no_entry = Entry(w1, textvariable=card_no, font=ourFont)
    card_no_entry.grid(row=3, column=1, padx=10, pady=10, sticky='we')

    # create a label for the date out
    date_out_label = Label(w1, text="Date Out", font=ourFont)
    date_out_label.grid(row=4, column=0, padx=10, pady=10, sticky='we')

    # display today's date using the datetime function, put it as a label ,assign it to date_out
    today = date.today()
    date_out = today.strftime("%Y-%m-%d")
    Date_out_label = Label(w1, text=date_out, font=ourFont)
    Date_out_label.grid(row=4, column=1, padx=10, pady=10, sticky='we')

    # create a label for the due date
    due_date_label = Label(w1, text="Due Date", font=ourFont)
    due_date_label.grid(row=5, column=0, padx=10, pady=10, sticky='we')

    # check if the month is december, if it is, add 1 to the year and set the month to january
    due_date = today + relativedelta(months=+1)
    if due_date.month == 12:
        due_date = due_date.replace(year=due_date.year+1, month=1)
    else:
        Due_date_label = Label(w1, text=due_date, font=ourFont)
    Due_date_label.grid(row=5, column=1, padx=10, pady=10, sticky='we')

    # keep submit button disabled until all fields are filled
    submit_button = Button(w1, text="Submit", command=lambda: CB_results(
        book_id_entry.get(), branch_id_entry.get(), card_no_entry.get(), date_out, due_date))
    submit_button.grid(row=6, column=1, padx=10, pady=10, sticky='we')
    submit_button.config(state="disabled")

    # checks if all fields are filled
    def check_fields():
        if book_id_entry.get() != "" and branch_id_entry.get() != "" and card_no_entry.get() != "":
            submit_button.config(state="normal")
        else:
            submit_button.config(state="disabled")

    # check if all fields are filled every time a field is filled
    branch_id_entry.bind("<KeyRelease>", lambda e: check_fields())
    card_no_entry.bind("<KeyRelease>", lambda e: check_fields())
    book_id_entry.bind("<KeyRelease>", lambda e: check_fields())

    # create a button to cancel the window
    cancel_button = Button(w1, text="Cancel", command=lambda: cancel(w1))
    cancel_button.grid(row=7, column=1, padx=10, pady=10, sticky='we')

    # execute my window
    w1.mainloop()

    return


# function to add a new borrower
def add_borrower():

    print("Adding a new borrower")

    # create a window
    w3 = Tk()
    w3.title("Add a new borrower")

    # create a label
    text = Label(w3, text="Add a new borrower", font=ourFont)
    text.grid(row=0, column=1, padx=10, pady=10, sticky='we')

    # create a label for the name
    name_label = Label(w3, text="Name", font=ourFont)
    name_label.grid(row=1, column=0, padx=10, pady=10, sticky='we')

    # create a text field for the name and assign it to name
    name = StringVar()
    name_entry = Entry(w3, textvariable=name, font=ourFont)
    name_entry.grid(row=1, column=1, padx=10, pady=10, sticky='we')

    # create a label for the address
    address_label = Label(w3, text="Address", font=ourFont)
    address_label.grid(row=2, column=0, padx=10, pady=10, sticky='we')

    # create a text field for the address and assign it to address
    address = StringVar()
    address_entry = Entry(w3, textvariable=address, font=ourFont)
    address_entry.grid(row=2, column=1, padx=10, pady=10, sticky='we')

    # create a label for the phone
    phone_label = Label(w3, text="Phone", font=ourFont)
    phone_label.grid(row=3, column=0, padx=10, pady=10, sticky='we')

    # create a text field for the phone and assign it to phone
    phone = StringVar()
    phone_entry = Entry(w3, textvariable=phone, font=ourFont)
    phone_entry.grid(row=3, column=1, padx=10, pady=10, sticky='we')

    # create a button to submit the information
    submit_button = Button(w3, text="Submit", command=lambda: AB_results(
        name_entry.get(), address_entry.get(), phone_entry.get()))
    submit_button.grid(row=4, column=1, padx=10, pady=10, sticky='we')

    # execute my window
    w3.mainloop()

    return


# function to add a new book
def add_book():
    print("Adding a new book")

    # create a window
    w5 = Tk()
    w5.title("Add a new book")

    # create a label
    text = Label(w5, text="Add a new book", font=ourFont)
    text.grid(row=0, column=1, padx=10, pady=10, sticky='we')

    # create a label for the title
    title_label = Label(w5, text="Title", font=ourFont)
    title_label.grid(row=1, column=0, padx=10, pady=10, sticky='we')

    # create a text field for the title and assign it to title
    title = StringVar()
    title_entry = Entry(w5, textvariable=title, font=ourFont)
    title_entry.grid(row=1, column=1, padx=10, pady=10, sticky='we')

    # create a label for the author
    author_label = Label(w5, text="Author", font=ourFont)
    author_label.grid(row=2, column=0, padx=10, pady=10, sticky='we')

    # create a text field for the author and assign it to author
    author = StringVar()
    author_entry = Entry(w5, textvariable=author, font=ourFont)
    author_entry.grid(row=2, column=1, padx=10, pady=10, sticky='we')

    # create a label for the publisher
    publisher_label = Label(w5, text="Publisher", font=ourFont)
    publisher_label.grid(row=3, column=0, padx=10, pady=10, sticky='we')

    # create a text field for the publisher and assign it to publisher
    publisher = StringVar()
    publisher_entry = Entry(w5, textvariable=publisher, font=ourFont)
    publisher_entry.grid(row=3, column=1, padx=10, pady=10, sticky='we')

    # submit button
    submit_button = Button(w5, text="Submit", command=lambda: ABOOK_results(
        title_entry.get(), author_entry.get(), publisher_entry.get()))
    submit_button.grid(row=4, column=1, padx=10, pady=10, sticky='we')

    # execute my window
    w5.mainloop()


# function to list the number of copies loaned out per branch
def list_copies():
    print("Listing the number of copies loaned out per branch")

    # create a window
    w6 = Tk()
    w6.title("Listing the number of copies loaned out per branch")
    w6.geometry("600x500")

    # create a label
    text = Label(
        w6, text="Listing the number of copies loaned out per branch", font=ourFont)
    text.grid(row=0, column=1, padx=10, pady=10, sticky='we')

    # create a label for the book title
    book_title_label = Label(w6, text="Book Title", font=ourFont)
    book_title_label.grid(row=1, column=0, padx=10, pady=10, sticky='we')

    # create a text field for the book title and assign it to book_title
    book_title = StringVar()
    book_title_entry = Entry(w6, textvariable=book_title, font=ourFont)
    book_title_entry.grid(row=1, column=1, padx=10, pady=10, sticky='we')

    # create a submit button
    submit_button = Button(
        w6, text="Submit", command=lambda: LC_results(book_title_entry.get()))
    submit_button.grid(row=2, column=1, padx=10, pady=10, sticky='we')


# function to list the Book_Loans that were returned late and how many days they were late
# Given any due date range list the Book_Loans that were returned late and how many days they were
# late.
def list_late():
    print("Listing the Book_Loans that were returned late and how many days they were late")

    # create a window
    w7 = Tk()
    w7.title(
        "Listing the Book_Loans that were returned late and how many days they were late")
    w7.geometry("600x500")

    # create a label
    text = Label(
        w7, text="Listing the Book_Loans that were returned late and how many days they were late", font=ourFont)
    text.grid(row=0, column=1, padx=10, pady=10, sticky='we')

    # create a label for the due date
    due_date_label1 = Label(w7, text="from", font=ourFont)
    due_date_label1.grid(row=1, column=0, padx=10, pady=10, sticky='we')

    # create a text field for the due date and assign it to due_date
    due_date1 = StringVar()
    due_date_entry1 = Entry(w7, textvariable=due_date1, font=ourFont)
    due_date_entry1.grid(row=1, column=1, padx=10, pady=10, sticky='we')

    # create a label for the due date
    due_date_label2 = Label(w7, text="to", font=ourFont)
    due_date_label2.grid(row=2, column=0, padx=10, pady=10, sticky='we')

    # create a text field for the due date and assign it to due_date
    due_date2 = StringVar()
    due_date_entry2 = Entry(w7, textvariable=due_date2, font=ourFont)
    due_date_entry2.grid(row=2, column=1, padx=10, pady=10, sticky='we')

    # create a submit button
    submit_button = Button(w7, text="Submit", command=lambda: LL_results(
        due_date_entry1.get(), due_date_entry2.get()))
    submit_button.grid(row=3, column=1, padx=10, pady=10, sticky='we')


# function to check the late fees by providing Card_no or Name or part of the name
def late_fees():
    print("Checking the late fees")

    # create a window
    w8 = Tk()
    w8.title("Checking the late fees")
    w8.geometry("600x500")

    # create a label
    text = Label(w8, text="Check your late fees", font=ourFont)
    text.grid(row=0, column=1, padx=10, pady=10, sticky='we')

    # create a label (card_no, or name, or part of the name)
    card_no_label = Label(
        w8, text="Card_no, or Name, or part of your name", font=ourFont)
    card_no_label.grid(row=1, column=0, padx=10, pady=10, sticky='we')

    # create a text field for the card_no, or name, or part of the name and assign it to card_no
    card_no = StringVar()
    card_no_entry = Entry(w8, textvariable=card_no, font=ourFont)
    card_no_entry.grid(row=1, column=1, padx=10, pady=10, sticky='we')

    # create a submit button
    submit_button = Button(
        w8, text="Submit", command=lambda: LF_results(card_no_entry.get()))
    submit_button.grid(row=2, column=1, padx=10, pady=10, sticky='we')

    # execute my window
    w8.mainloop()

    return


# function to give book info
def book_info():
    print("Getting book info")

    # create a window
    w10 = Tk()
    w10.title("Getting book info")
    w10.geometry("600x500")

    # create a label
    text = Label(w10, text="Get book info", font=ourFont)
    text.grid(row=0, column=1, padx=10, pady=10, sticky='we')

    # create a label to give a input format (book_id, or title, or part of the title)
    book_id_label = Label(
        w10, text="Book_id, or Title, or part of the title", font=ourFont)
    book_id_label.grid(row=1, column=0, padx=10, pady=10, sticky='we')

    # create a text field for the book_id, or title, or part of the title and assign it to book_id
    book_info = StringVar()
    book_info_entry = Entry(w10, textvariable=book_info, font=ourFont)
    book_info_entry.grid(row=1, column=1, padx=10, pady=10, sticky='we')

    # create a submit button
    submit_button = Button(
        w10, text="Submit", command=lambda: BI_results(book_info_entry.get()))
    submit_button.grid(row=2, column=1, padx=10, pady=10, sticky='we')

    # execute my window
    w10.mainloop()

    return


# Show the output of the updated Book_Copies.
def CB_results(book_id, branch_id, card_no, date_out, due_date):
    print("Checking out a book")

    # create a window
    w2 = Tk()

    # create a label
    text = Label(w2, text="Check out a book", font=ourFont)
    text.grid(row=0, column=1, padx=10, pady=10, sticky='we')

    submit_conn = sqlite3.connect('LMS.sqlite3')
    submit_cur = submit_conn.cursor()

    # add it to Book_Loan
    submit_cur.execute("INSERT INTO BOOK_LOANS(Book_Id, Branch_Id, Card_no, Date_Out, Due_Date) VALUES (:book_id, :branch_id, :card_no, :date_out, :due_date)",
                       {
                           'book_id': book_id,
                           'branch_id': branch_id,
                           'card_no': card_no,
                           'date_out': date_out,
                           'due_date': due_date,
                       })
    print("Book_Loan updated")

    # the number of copies needs to be updated in the Book_Copies table.
    submit_cur.execute("UPDATE BOOK_COPIES SET No_Of_Copies = No_Of_Copies - 1 WHERE Book_Id = :book_id AND Branch_Id = :branch_id",
                       {
                           'book_id': book_id,
                           'branch_id': branch_id,
                       })
    print("Book_Copies updated")

    # Show the output of the updated Book_Copies.
    submit_cur.execute("SELECT * FROM BOOK_COPIES")
    print("Book_Copies output")
    records = submit_cur.fetchall()
    print_records = ''

    for record in records:
        print_records += str(record) + "\n"

    # create lebels for headers
    book_id_label = Label(
        w2, text="(Book_Id, Branch_Id, # of copies)", font=ourFont)
    book_id_label.grid(row=1, column=1, padx=10, pady=10, sticky='we')

    query_label = Label(w2, text=print_records, font=ourFont)
    query_label.grid(row=2, column=1, padx=10, pady=10, sticky='we')

    # create a button to cancel the window
    cancel_button = Button(w2, text="Close", command=lambda: cancel(w2))
    cancel_button.grid(row=3, column=1, padx=10, pady=10, sticky='we')

    # closing the connection
    submit_conn.commit()
    submit_conn.close()
    return


# function to add a new borrower
def AB_results(name, address, phone):

    # create a window
    w4 = Tk()
    w4.title("Add a new borrower")
    w4.geometry("400x200")

    # connect to the database
    submit_conn = sqlite3.connect('LMS.sqlite3')
    submit_cur = submit_conn.cursor()

    # add the new borrower to the database
    submit_cur.execute("INSERT INTO BORROWER(Name, Address, Phone) VALUES (:name, :address, :phone)",
                       {
                           'name': name,
                           'address': address,
                           'phone': phone,
                       })

    # get the card number of the new borrower
    submit_cur.execute("SELECT Card_no FROM BORROWER WHERE Name = :name AND Address = :address AND Phone = :phone",
                       {
                           'name': name,
                           'address': address,
                           'phone': phone,
                       })

    # display the card number
    records = submit_cur.fetchall()
    print_records = ''

    for record in records:
        print_records += str(record) + "\n"

    # create a label for the card number
    card_no_label = Label(w4, text="Card Number", font=ourFont)
    card_no_label.grid(row=0, column=1, padx=10, pady=10, sticky='we')

    # create a label for the card number
    query_label = Label(w4, text=print_records, font=ourFont)
    query_label.grid(row=1, column=1, padx=10, pady=10, sticky='we')

    # create a button to cancel the window
    cancel_button = Button(w4, text="Close", command=lambda: cancel(w4))

    # closing the connection
    submit_conn.commit()
    submit_conn.close()

    # execute my window
    w4.mainloop()

    return


# function to add a new book
def ABOOK_results(title, author, publisher):

    # create a window
    w9 = Tk()
    w9.title("Add a new book")
    w9.geometry("700x700")

    # connect to the database
    submit_conn = sqlite3.connect('LMS.sqlite3')
    submit_cur = submit_conn.cursor()

    # add the new book to the database Book(Book_Id, Title, Book_Author)
    submit_cur.execute("INSERT into BOOK(Title, Book_Author) values (:title, :author)",
                       {
                           'title': title,
                           'author': author
                       })
    print("Book added to BOOK")

    # display the Book table
    submit_cur.execute("SELECT * FROM BOOK")

    # display the Book table
    records = submit_cur.fetchall()
    print_records = ''

    for record in records:
        print_records += str(record) + "\n"

    # create a label for the card number
    book_label = Label(w9, text="(Book_Id, Title, Book_Author)", font=ourFont)
    book_label.grid(row=0, column=1, padx=10, pady=10, sticky='we')

    # create a label for the card number
    query_label = Label(w9, text=print_records, font=ourFont)
    query_label.grid(row=1, column=1, padx=10, pady=10, sticky='we')

    # create a button to cancel the window
    cancel_button = Button(w9, text="Close", command=lambda: cancel(w9))
    cancel_button.grid(row=2, column=1, padx=10, pady=10, sticky='we')

    # closing the connection
    submit_conn.commit()
    submit_conn.close()

    # execute my window
    w9.mainloop()

    return


# function to list the number of copies loaned out per branch
def LC_results(book_title):
    # create a window
    w7 = Tk()
    w7.title("Listing the number of copies loaned out per branch")
    w7.geometry("600x500")

    # connect to the database
    submit_conn = sqlite3.connect('LMS.sqlite3')
    submit_cur = submit_conn.cursor()

    # get the book id from the book title
    submit_cur.execute("SELECT Book_Id FROM BOOK WHERE Title = :book_title",
                       {
                           'book_title': book_title,
                       })

    # assign the book id to book_id
    records = submit_cur.fetchall()

    # convert records to int
    records = [int(i[0]) for i in records]

    info_label = Label(
        w7, text="If no entries displayed, no books are loaned out(all returned)", font=ourFont)
    info_label.grid(row=0, column=1, padx=10, pady=10, sticky='we')

    # create a label for the book title
    book_title_label = Label(
        w7, text="(Book Title,Branch Name, num of copies loaned)", font=ourFont)
    book_title_label.grid(row=1, column=1, padx=10, pady=10, sticky='we')

    # find the number of copies loaned out per branch using the book id from BOOK_LOANS
    # if the BOOK_LOAN.returned_date is null, then the book is still loaned out. else, it will be counted as loaned out in the query
    # have a row for all branches
    # have a column for the book title, branch name, and number loaned out copies
    submit_cur.execute("SELECT BOOK.Title, LIBRARY_BRANCH.Branch_Name, COUNT(BOOK_LOANS.Book_Id) FROM LIBRARY_BRANCH LEFT JOIN BOOK_LOANS ON LIBRARY_BRANCH.Branch_Id = BOOK_LOANS.Branch_Id NATURAL JOIN BOOK WHERE BOOK.Book_Id = :book_id AND BOOK_LOANS.Returned_date IS NULL GROUP BY LIBRARY_BRANCH.Branch_Name",
                       {
                           'book_id': records[0],
                       })

    # display the results
    records = submit_cur.fetchall()
    print_records = ''

    for record in records:
        print_records += str(record) + "\n"

    # create a label for the results
    query_label = Label(w7, text=print_records, font=ourFont)
    query_label.grid(row=2, column=1, padx=10, pady=10, sticky='we')

    # create a button to cancel the window
    cancel_button = Button(w7, text="Close", command=lambda: cancel(w7))
    cancel_button.grid(row=3, column=1, padx=10, pady=10, sticky='we')

    # closing the connection
    submit_conn.commit()
    submit_conn.close()

    # execute my window
    w7.mainloop()

    return


# function to list the Book_Loans that were returned late and how many days they were late
def LL_results(due_date1, due_date2):
    print("Listing the Book_Loans that were returned late and how many days they were late")

    # create a window
    w8 = Tk()
    w8.title(
        "Listing the Book_Loans that were returned late and how many days they were late")
    w8.geometry("600x500")

    # connect to the database
    submit_conn = sqlite3.connect('LMS.sqlite3')
    submit_cur = submit_conn.cursor()

    # create a label
    text = Label(
        w8, text="Listing the Book_Loans that were returned late and how many days they were late", font=ourFont)
    text.grid(row=0, column=1, padx=10, pady=10, sticky='we')

    #create a label with the output format
    info_label = Label(w8, text="(Book_Id, Card_No, Date_Out, Due_Date, Returned_date, Late, Days_Late)", font=ourFont)
    info_label.grid(row=1, column=1, padx=10, pady=10, sticky='we')

    # CASE WHEN BOOK_LOANS.Late is 1
    querry = query = """
    SELECT 
        BOOK_LOANS.Book_Id,
        BOOK_LOANS.Card_No,
        BOOK_LOANS.Date_Out,
        BOOK_LOANS.Due_Date,
        BOOK_LOANS.Returned_date,
        BOOK_LOANS.Late,
        (julianday(BOOK_LOANS.Returned_date) - julianday(BOOK_LOANS.Due_Date)) AS Days_Late
    FROM 
        BOOK_LOANS
        JOIN BORROWER ON BOOK_LOANS.Card_No = BORROWER.Card_No
    WHERE 
        BOOK_LOANS.Due_Date BETWEEN :start_date AND :end_date
        AND BOOK_LOANS.Returned_date > BOOK_LOANS.Due_Date
    ORDER BY 
        Days_Late DESC;
    """
    submit_cur.execute(query, {'start_date': due_date1, 'end_date': due_date2})

    # display the results
    records = submit_cur.fetchall()
    print_records = ''

    for record in records:
        print_records += str(record) + "\n"

    # create a label for the results
    query_label = Label(w8, text=print_records, font=ourFont)
    query_label.grid(row=2, column=1, padx=10, pady=10, sticky='we')

    # create a button to cancel the window
    cancel_button = Button(w8, text="Close", command=lambda: cancel(w8))
    cancel_button.grid(row=3, column=1, padx=10, pady=10, sticky='we')

    # closing the connection
    submit_conn.commit()
    submit_conn.close()

    # execute my window
    w8.mainloop()

    return

# check for late fee


def LF_results(borrower_info):
    print("Checking for late fee")

    # create a window
    w10 = Tk()
    w10.title("Checking for late fee")
    w10.geometry("600x500")

    # connect to the database
    submit_conn = sqlite3.connect('LMS.sqlite3')
    submit_cur = submit_conn.cursor()

    # create a label to display the table format
    info_label = Label(
        w10, text="(Card_No, BorrowerName, LateFeeBalance($))", font=ourFont)
    info_label.grid(row=0, column=1, padx=10, pady=10, sticky='we')

    # create a label
    text = Label(w10, text="Checking for late fee", font=ourFont)
    text.grid(row=1, column=1, padx=10, pady=10, sticky='we')

    # query to find the late fee
    query = """
    SELECT 
        Card_No, 
        BorrowerName, 
        CASE
            WHEN LateFeeBalance IS NULL OR LateFeeBalance = 0 THEN '$0.00'
            ELSE '$' || printf("%.2f", LateFeeBalance)
        END AS LateFeeBalance
    FROM 
        vBookLoanInfo
    WHERE 
        (:search_string IS NULL 
        OR :search_string = '' 
        OR 
        Card_No LIKE '%' || :search_string || '%' OR 
        BorrowerName LIKE '%' || :search_string || '%')
    ORDER BY 
        LateFeeBalance DESC;
    """
    submit_cur.execute(query, {'search_string': borrower_info})

    # display the results
    records = submit_cur.fetchall()
    print_records = ''

    for record in records:
        print_records += str(record) + "\n"

    # create a label for the results
    query_label = Label(w10, text=print_records, font=ourFont)
    query_label.grid(row=1, column=1, padx=10, pady=10, sticky='we')

    # create a button to cancel the window
    cancel_button = Button(w10, text="Close", command=lambda: cancel(w10))
    cancel_button.grid(row=2, column=1, padx=10, pady=10, sticky='we')

    # closing the connection
    submit_conn.commit()
    submit_conn.close()

    # execute my window
    w10.mainloop()

    return

# function to give book info result


def BI_results(book_info):
    # create a window
    w11 = Tk()
    w11.title("Book Info")
    w11.geometry("600x500")

    # connect to the database
    submit_conn = sqlite3.connect('LMS.sqlite3')
    submit_cur = submit_conn.cursor()

    # create a label to display the table format
    info_label = Label(
        w11, text="(Book_Id, Title, Total Days borrowed ,BorrowerName, Late Fee Balance)", font=ourFont)
    info_label.grid(row=0, column=1, padx=10, pady=10, sticky='we')

    # query to find the book info
    query = """
    SELECT 
    b.Book_Id, 
    b.Title, 
    v.TotalDays,
    v.BorrowerName,  
    CASE 
        WHEN v.LateFeeBalance IS NULL THEN 'Non-Applicable'
        ELSE '$' || printf("%.2f", v.LateFeeBalance)
    END AS LateFeeAmount
    FROM 
        vBookLoanInfo v 
        JOIN BOOK b ON v.BookTitle = b.Title
    WHERE 
        b.Title LIKE '%' || :search_input || '%' 
        OR b.Book_Id = :search_input
    ORDER BY 
        v.LateFeeBalance DESC NULLS LAST
    """

    submit_cur.execute(query, {'search_input': book_info})

    # display the results
    records = submit_cur.fetchall()
    print_records = ''

    for record in records:
        print_records += str(record) + "\n"

    # create a label for the results
    query_label = Label(w11, text=print_records, font=ourFont)
    query_label.grid(row=1, column=1, padx=10, pady=10, sticky='we')

    # create a button to cancel the window
    cancel_button = Button(w11, text="Close", command=lambda: cancel(w11))
    cancel_button.grid(row=2, column=1, padx=10, pady=10, sticky='we')

    # closing the connection
    submit_conn.commit()
    submit_conn.close()

    # execute my window
    w11.mainloop()

    return


# add tkinter window
root = Tk()
root.title("Library Management System")
root.geometry("600x500")

# create a database or connect to one
conn = sqlite3.connect('LMS.sqlite3')

# create cursor
cur = conn.cursor()

# add some text and horizontally center it
text = Label(root, text="GUI CSE3330", font=ourFont)
text.grid(row=0, column=1, padx=190, pady=10, sticky='we')

# create a button to check out a book
checkout_button = Button(root, text="Check out a book", command=checkout_book)
checkout_button.grid(row=1, column=1, padx=190, pady=10, sticky='we')

# create a button to add a new borrower
add_borrower_button = Button(
    root, text="Add a new borrower", command=add_borrower)
add_borrower_button.grid(row=2, column=1, padx=190, pady=10, sticky='we')

# create a button to add a new book
add_book_button = Button(root, text="Add a new book", command=add_book)
add_book_button.grid(row=3, column=1, padx=190, pady=10, sticky='we')

# create a button to list the number of copies loaned out per branch
list_copies_button = Button(
    root, text="List number of copies loaned out per branch", command=list_copies)
list_copies_button.grid(row=4, column=1, padx=190, pady=10, sticky='we')

# create a button to list the Book_Loans that were returned late and how many days they were late
list_late_button = Button(
    root, text="List late Book_Loans and days overdue", command=list_late)
list_late_button.grid(row=5, column=1, padx=190, pady=10, sticky='we')

# create a button to check for the late fee
late_fee_button = Button(root, text="Check for late fee", command=late_fees)
late_fee_button.grid(row=6, column=1, padx=190, pady=10, sticky='we')

# create a button to check book info
book_info_button = Button(root, text="Check book info", command=book_info)
book_info_button.grid(row=7, column=1, padx=190, pady=10, sticky='we')


# execute my window
root.mainloop()



