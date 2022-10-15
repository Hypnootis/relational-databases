
test_data = ["""INSERT INTO track (name, track_length)
VALUES ('Suhisee', 180),
('Kolisee', 175),
('Röhisee', 183),
('Hili hiis hops', 200),
('Hebsbuuga', 194),
('Hillomunkki', 2),
('Electro', 600),
('Disco', 420),
('Mushroom' 300)
""",
"""INSERT INTO tracklist(track_id)
VALUES (1),
(2),
(3)
""",
"""INSERT INTO cd (name, price, genre, tracklist_id)
VALUES ('Ruohikossa', 3.50, 'Iskelmä', 1),
('poppopppoppopmusiikkia', 8.30, 'Pop', 2),
('Lightning', 1.30, 'EDM', 3)
""",
"""INSERT INTO discography (cd_id, cd_name)
VALUES (1, 'Ruohikossa')
(2, 'poppopppoppopmusiikkia')
(3, 'Lightning')
""",
"""INSERT INTO artist (name, discography_id)
VALUES ('Muicemon', 1)
('Mesa-Matti Loiri', 2)
('Mopetion', 3)
"""]


