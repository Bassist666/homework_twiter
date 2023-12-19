from model.User import User


class Twit:
    def __init__(self, twit_id: int, body: str, author: User):
        self.twit_id = twit_id
        self.body = body
        self.author = author


    def change_twit(self, new_body: str):
        self.body = new_body


    def del_twit(self):
        self.body = 'deleted'
        self.author = 'deleted'
