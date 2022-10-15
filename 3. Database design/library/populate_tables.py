# All the phone numbers are generated with a random number generator, and the addresses are of public businesses / not individual addresses
test_data = ["""INSERT INTO publisher (address, name, phone_number)
    VALUES ('Kuntotie 5 96400 Rovaniemi Finland', 'Reindeer Publishing', '9648987385'),
    ('McFarlane St Cummins SA 5631 Australia', 'Kangaroo & co', '8227270461'),
    ('Kenraalintie 9 42300 Jämsänkoski Finland', 'Mikan K-Market ja kirjapaino', '4784923775')
    """,    
    """INSERT INTO book (book_name, publisher_id, copy_count)
    VALUES ('Silmarillion', 1, 5),
    ('test_book', 1, 2000),
    ('The joy of SQL programming', 2, 1),
    ('Muicen muistelmat', 2, 4),
    ('Muhveli muhveli muhveli - näin muhvellat', 2, 2)
    """,
    """INSERT INTO customer (customer_name, address, email, phone_number)
    VALUES ('Mirva Kirva', 'Karhupolku 16 Kaipola', 'mirvakirva@gmail.lol', '1231231'),
    ('Keijo Kurahousu', 'Kankkulankaivo Kankkula', 'kankkulankuninkas@kuumaposti.fi', '1323661'),
    ('Hesha Muu', 'Fiilin dis meis Mifoo', 'hanomenashii@hishimoo.com', '5555555')
    """,
    """ INSERT INTO catalog (book_id, book_name, publisher_id)
    VALUES (1, 'Silmarillion', 1),
    (1, 'test_book', 1),
    (2, 'The joy of SQL programming', 2),
    (4, 'Muhveli muhveli muhveli - näin muhvellat', 2),
    (3, 'Muicen muistelmat', 2)
    """,
    """INSERT INTO loan (book_id, customer_id, loan_date, due_date)
    VALUES (1, 1, '2022-06-07', '2022-06-14'),
    (1, 2, '2022-06-06', '2022-06-30'),
    (1, 1, '2001-01-01', '2022-10-14')
    """]


