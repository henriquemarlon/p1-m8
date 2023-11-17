import re
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Pose

class Chatbot():
    def __init__(self):

        self.intentions = {
            r'(hello|hi|hey|hi there|hiya)': 'greeting',
            r'(bye|goodbye|see you)': 'farewell',
            r'\b([cC]ar[tT]a?ã?o|[Pp]agamento)\b': 'Intenção A',
            r'\b([Pp]?e?d?i?d?o|[Ee]?n?t?r?e?g?a)\b': 'Intenção B',
        }

        self.intention = None

    def go_to(self):
        print(f'OK! A intenção da pergunta foi {self.intention}')

    def end_chat(self):
        print('Goodbye!')
        exit()

    def identify_intention(self, text):
        for expression, intention in self.intentions.items():
            print(text)
            match = re.search(expression, text, re.IGNORECASE)
            if match:
                print(expression)
                print(intention)
                return intention
        return None

    def perform_action(self, intention):
        if intention:
            if intention == 'greeting':
                print('Hi Icarus! I am Daedalus your father. Where you want you go?')

            elif intention == 'farewell':
                return self.end_chat()

            else:
                self.go_to()
        else:
            print('Sorry, I did not understand what you said.')

    def start_conversation(self):
        while True:
            text = input("You: ")
            self.intention = self.identify_intention(text)
            self.perform_action(self.intention)

def main(args=None):
    chatbot = Chatbot()
    chatbot.start_conversation()

if __name__ == '__main__':
    main()
