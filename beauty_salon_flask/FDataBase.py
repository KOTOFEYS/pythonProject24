


class FDataBase:
    def __init__(self,db):
        self.__db = db
        self.__cur = db.cursor()

    def online_reg(self,username,num_tel):
        self.__cur.execute("INSERT INTO menu Values(NULL,?,?)",(username, num_tel))
        self.__db.commit()
