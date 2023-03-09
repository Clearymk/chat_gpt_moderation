import pymysql
import time


class DataBase(object):
    def __init__(self, database="openai"):
        self.count = 0
        try:
            self.mysql = pymysql.connect(host='10.19.124.172',
                                         port=10255,
                                         user='root',
                                         password='catlab1a509',
                                         database=database)
        except Exception:
            time.sleep(2)
            self.__init__()

    def insert_moderation(self, text, hate, hate_threatening,
                          self_harm, sexual, sexual_minors,
                          violence, violence_graphic, hate_flag,
                          hate_threatening_flag, self_harm_flag, sexual_flag,
                          sexual_minors_flag, violence_flag, violence_graphic_flag, flagged):

        insert_sql = "insert into openai.moderation_result(text, hate, hate_threatening, " \
                     "self_harm, sexual, sexual_minors, " \
                     "violence, violence_graphic, hate_flag, " \
                     "hate_threatening_flag, self_harm_flag, sexual_flag, " \
                     "sexual_minors_flag, violence_flag, violence_graphic_flag, flagged) " \
                     "values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

        cursor = self.mysql.cursor()
        cursor.execute(insert_sql, (text, hate, hate_threatening,
                                    self_harm, sexual, sexual_minors,
                                    violence, violence_graphic, hate_flag,
                                    hate_threatening_flag, self_harm_flag, sexual_flag,
                                    sexual_minors_flag, violence_flag, violence_graphic_flag, flagged))
        cursor.close()
        self.mysql.commit()



