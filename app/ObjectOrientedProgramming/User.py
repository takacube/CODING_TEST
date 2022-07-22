class User:
    def __init__(self, id):
        self.id = id

    def get_user(id):
        if id == 1:
            return User(id)
        return NullUser(id)

    def unsubscribe(self):
        self.__send_to_slack(self.id)
        return "sent to slack"

    def __send_to_slack(self, id):
        print(f"id: {id}")
        return True

    def is_null():
        return False

class NullUser(User):
    def unsubscribe(self):
        return "can not unsbscribe nulluser"

    def is_null():
        return True