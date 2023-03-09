from database import DataBase


class Moderation:
    def __init__(self, text, hate, hate_threatening,
                 self_harm, sexual, sexual_minors,
                 violence, violence_graphic, hate_flag,
                 hate_threatening_flag, self_harm_flag, sexual_flag,
                 sexual_minors_flag, violence_flag, violence_graphic_flag, flagged):
        self.text = text
        self.hate = hate
        self.hate_threatening = hate_threatening
        self.self_harm = self_harm
        self.sexual = sexual
        self.sexual_minors = sexual_minors
        self.violence = violence
        self.violence_graphic = violence_graphic
        self.hate_flag = hate_flag
        self.hate_threatening_flag = hate_threatening_flag
        self.self_harm_flag = self_harm_flag
        self.sexual_flag = sexual_flag
        self.sexual_minors_flag = sexual_minors_flag
        self.violence_flag = violence_flag
        self.violence_graphic_flag = violence_graphic_flag
        self.flagged = flagged

    def insert_to_db(self):
        db = DataBase()
        db.insert_moderation(self.text, self.hate, self.hate_threatening,
                             self.self_harm, self.sexual, self.sexual_minors,
                             self.violence, self.violence_graphic, self.hate_flag,
                             self.hate_threatening_flag, self.self_harm_flag, self.sexual_flag,
                             self.sexual_minors_flag, self.violence_flag, self.violence_graphic_flag, self.flagged)
        db.mysql.close()
