class Question():

    keywords = ["celcius", "multiply"]

    def __init__(self, str):
        self.question = str

    def display_ques(self):
        print(self.ques)

    def find_keywords(self):
        # split the question
        words = self.question.split()
        j = 0

        for i in words:
            if i in keywords:
                case = j
                j = j+1
