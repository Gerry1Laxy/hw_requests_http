from stackapi import StackAPI
from datetime import datetime, timedelta


class Questions:

    def __init__(self, max_pages=15):
        self.SITE = StackAPI('stackoverflow')
        self.SITE.max_pages = max_pages
        self.now = datetime.now()

    def get_questions(self, ago=2, tag='python'):
        questions = self.SITE.fetch(
            'questions',
            fromdate=self.now - timedelta(days=ago),
            todate=self.now,
            tagged=tag
        )
        print(f'По тегу "{tag}" найдено {len(questions["items"])} вопросов')
        for question in questions['items']:
            print(question['title'])


if __name__ == '__main__':
    python_questions = Questions()
    python_questions.get_questions()
