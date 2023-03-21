from data import Data
from datetime import date

class Joke:

    jokes = [] # class level attribute

    data_source = Data('jokes_data')

    def __init__(self, joke_data):
        
        self.date_added = joke_data['date_added']
        self.text = joke_data['text']

        Joke.jokes.append(self)

    # instance level methods
    def say(self):
        print(self.text)

    def serialize(self):
        return({
            'date_added': str(self.date_added),
            'text': self.text
        })

    # class level method

    @classmethod
    def load(cls):
        data = Joke.data_source.get()
        [cls(row) for row in data]

    @classmethod
    def save(cls):
        cls.data_source.save([joke.serialize() for joke in cls.jokes])

    @classmethod
    def create(cls, text):

        new_joke = cls({
            'date_added': date.today(),
            'text': text
        })

        cls.save()

        return new_joke

    @classmethod
    def update(cls, id, text):
         Joke.jokes[id - 1].text = text
         cls.save()

    @classmethod
    def delete(cls, id):
        del(Joke.jokes[id - 1])
        cls.save()