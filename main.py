import roboter.controller.conversation

class MainError(Exception):
    pass

def main():
    roboter.controller.conversation.talk_about_restaurant()
    raise MainError

if __name__ == '__main__':
    main()
