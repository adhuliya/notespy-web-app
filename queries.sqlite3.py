# this is a comment
# this file is a single dictionary object which can be
# read and evaluated using the eval() function in Python3
# suffix c=create, i=insert, s=select, u=update, a=administrative

{
    'initquery0000c':
    { 'query' : """
    CREATE TABLE IF NOT EXISTS accounts (
        id INTEGER PRIMARY KEY,
        uid TEXT NOT NULL,
        pwd TEXT NOT NULL,
        name TEXT NOT NULL,
        created TEXT NOT NULL,
        modified TEXT NOT NULL
    )
    """, 'tags': {'init': 1}},

    'initquery0001c':
    { 'query' : """
    CREATE TABLE IF NOT EXISTS notes (
        id INTEGER PRIMARY KEY,
        accid INTEGER,
        note TEXT,
        attachment TEXT,
        created TEXT NOT NULL,
        modified TEXT NOT NULL,
        FOREIGN KEY(accid) REFERENCES accounts(id)
    )
    """, 'tags': {'init': 2}},

    'initquery0002s':
    { 'query' : """
    INSERT INTO accounts (uid, pwd, name, created, modified) 
    values('anshu','anshu','anshuman', '2016-01-01', '2016-01-01')
    """, 'tags': {'init': 3}},

    'query0001i':
    { 'query' : """
    INSERT INTO notes (note, attachment, created, modified)
    VALUES (?, ?, ?, ?)
    """, 'tags': {'none':1}},

    'query0002s':
    { 'query' : """
    SELECT * FROM notes order by modified
    """, 'tags': {'none':1}},

    'query0003s':
    { 'query' : """
    SELECT id, name FROM accounts where uid = ? and pwd = ?
    """, 'tags': {'none':1}},

}


