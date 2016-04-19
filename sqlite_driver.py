import sqlite3 

#classes are Sqlite3Driver and Sqlite3 

class Sqlite3():
    """
    This is a convenience class built to wrap Sqlite3Driver class.
    """
    def __init__(self, dbfile=':memory:', maxfetchlen=0, 
            queriesfile='queries.sqlite3.py'): 
        self.sqlite = Sqlite3Driver(dbfile=dbfile, maxfetchlen=maxfetchlen)

        # queries file should be in the same directory or
        # its path could be passed
        self.queriesfile = queriesfile
        self.queries = Sqlite3.read_queries(queriesfile)

        self.dbfile = dbfile 
        # max number of rows returnded from select statement
        # zero means all
        self.maxfetchlen = maxfetchlen
        self.initialize_db()

    def read_queries(queriesfile='queries.sqlite3.py'):
        with open(queriesfile) as q:
            return eval(q.read())

    def initialize_db(self):
        if self.sqlite == None: return False

        initquerykeys = [x for x in self.queries.keys()
                if 'init' in self.queries[x]['tags']]
        initquerykeys.sort(key=lambda x : self.queries[x]['tags']['init'])

        for querykey in initquerykeys:
            self.execute(querykey)

        return True

    def execute (self, querykey, data=None, maxfetchlen=None):
        """
        Here the paramenter 'data' is a tuple of values. Which
        will be inserted into the 'query' paramenter at appropriate 
        places.
        """
        if querykey.endswith("s"):
            return self.sqlite.select(self.queries[querykey]['query'],
                    data=data, maxfetchlen=maxfetchlen)
        else:
            return self.sqlite.modify(self.queries[querykey]['query'],
                    data=data)

    def close (self):
        if self.sqlite != None:
            self.sqlite.close()



class Sqlite3Driver(): 
    def __init__(self, dbfile=':memory:', maxfetchlen=0): 

        # queries file should be in the same directory or
        # its path could be passed

        self.dbfile = dbfile 
        # max number of rows returnded from select statement
        # zero means all
        self.maxfetchlen = maxfetchlen
        self.cur = self.conn = None
        try:
            self.conn = sqlite3.connect(dbfile) 
            print ("Database {} opened.".format(self.dbfile))
            self.cur = self.conn.cursor() 
        except sqlite3.Error as e:
            print (e)
            raise e

    def select (self, query, data=None, maxfetchlen=None): 
        """
        Here the paramenter 'data' is a tuple of values. Which
        will be inserted into the 'query' paramenter at appropriate 
        places.
        """
        if data == None: 
            self.cur.execute (query) 
        else: 
            self.cur.execute (query, data)

        if maxfetchlen == None:
            maxfetchlen = self.maxfetchlen

        if maxfetchlen == 0:
            return self.cur.fetchall()
        else:
            return self.cur.fetchmany(size=maxfetchlen)

    def modify (self, query, data=None):
        """
        Here the paramenter 'data' is a tuple of values. Which
        will be inserted into the 'query' paramenter at appropriate 
        places.
        """
        if data == None: 
            self.cur.execute (query) 
        else: 
            self.cur.execute (query, data)

        self.conn.commit()

        return self.cur.rowcount;

    def close (self):
        if self.conn != None:
            self.conn.close()
            print ("Database {} closed.".format(self.dbfile))

