CREATE TABLE IF NOT EXISTS accounts (
        id INTEGER PRIMARY KEY,
        uid TEXT NOT NULL UNIQUE,
        pwd TEXT NOT NULL,
        name TEXT NOT NULL,
        created TEXT NOT NULL,
        modified TEXT NOT NULL
    );

CREATE TABLE IF NOT EXISTS notes (
        id INTEGER PRIMARY KEY,
        accid INTEGER 
        note TEXT,
        attachment TEXT,
        created TEXT NOT NULL,
        modified TEXT NOT NULL,
        FOREIGN KEY(accid) REFERENCES accounts(id)
    );


INSERT INTO accounts (uid, pwd, name, created, modified) 
VALUES ('dummy', 'dummy', 'dummy', '2016-04-16 03:10:30', '2016-04-16 03:10:30');
