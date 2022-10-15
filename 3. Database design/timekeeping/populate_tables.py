
test_data = ["""INSERT INTO employee (name, email)
VALUES ('Kaisla Kultahammas', 'kkultahammas@traijing.com'),
('Pirkko Pyppy', 'ppyppy@traijing.com'),
('Teijo Tuhnu', 'ttuhnu@traijing.com'),
('Pierre France', 'pfrance@traijing.com'),
('Maija Mehiläinen', 'mmehilainen@traijing.com')
""",
"""INSERT INTO project (name)
VALUES ('Tipsy website'),
('Pipsu pepsait'),
('Hipsu hepsait')
""",
"""INSERT INTO timetable (entry_date, project_id, employee_id, hours_worked)
VALUES ('2022-08-10', 1, 4, 3),
('2022-08-10', 3, 4, 4),
('2022-08-10', 2, 2, 8),
('2022-08-10', 1, 3, 9),
('2022-08-11', 2, 1, 6),
('2022-08-11', 1, 3, 9)
"""]


