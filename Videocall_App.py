class Videocall_App(object):
    participants_online = 0
    action = ['Speaking', 'Silent']

    def __init__(self, user_name, company):
        self.user_name = user_name
        self.company = company

    @classmethod
    def show_participants_online(cls):
        return (print(f"How many participants are attending the meeting: {cls.participants_online}"))

    @classmethod
    def go_online(cls):
        cls.participants_online = cls.participants_online + 1
        return cls.participants_online

    #@classmethod
    #def go_offline(cls):
        #cls.new_participants_online = cls.participants_online - 1
        #return cls.new_participants_online

    def status(self, action):
        if action in Videocall_App.action:
            return print(f'{self.user_name} is action')
        else:
            raise ValueError("The user must either be 'speaking' or 'silent'")
        # return f"{self.user_name} is action"


class Message(object):
    def __init__(self, user_name, message):
        self.user_name = user_name
        self.message = message

    def __status(self):  # spl method
        return print(f'{self.user_name} sent the message {self.message}')


class ChatApp(Videocall_App, Message):
    def __init__(self, user_name, company, message):
        Videocall_App.__init__(self, user_name, company)
        Message.__init__(self, user_name, message)


if __name__ == '__main__':
    CA = ChatApp('Uma', 'Welcome', 'integrify')

    print(CA.go_online())
    CA.show_participants_online()
    #print(CA.go_offline())
    CA.status('Silent')
    CA._Message__status()  # to call the __stuatus explicitly
