CREATE TABLE user (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name VARCHAR(45),
    last_name VARCHAR(45),
    hobbies TEXT, 
    active BOOLEAN DEFAULT 1

);


INSERT INTO user (
    first_name,
    last_name,
    hobbies
) VALUES (
    "jane",
    "doe",
    "tennis"
);

INSERT INTO user (
    first_name,
    last_name,
    hobbies
) VALUES (
    "john",
    "doe",
    "football"
);

INSERT INTO user (
    first_name,
    last_name,
    hobbies
) VALUES (
    "james",
    "doe",
    "reading"
);



