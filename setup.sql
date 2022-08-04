CREAT TABLE user (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name VARCHAR(45),
    last_name VARCHAR(45),
    hobbies TEXT, 
    ACTIVE boolean default 1

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


