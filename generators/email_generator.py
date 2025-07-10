from faker import Faker
from datetime import datetime, timedelta
import random


class EmailGenerator:
    def __init__(self):
        self.fake = Faker()

    def generate_email(self, count=1000):
        emails = []
        for _ in range(count):
            email = {
                'subject': self._generate_subject(),
                'sender': self._generate_sender(),
                'recipient': self._generate_recipient(),
                'body': self._generate_body(),
                'date': self._generate_date(),
                'is_read': random.choice([True, False]),
                'labels': self._generate_labels(),
                'attachments': self._generate_attachments()
            }
            emails.append(email)
        return emails

    def _generate_subject(self):
        return self.fake.sentence(nb_words=6)

    def _generate_sender(self):
        return self.fake.email()

    def _generate_recipient(self):
        return self.fake.email()

    def _generate_body(self):
        return '\n\n'.join(self.fake.paragraphs(nb=random.randint(1, 5)))

    def _generate_date(self):
        return self.fake.date_time_between(start_date='-1y', end_date='now')

    def _generate_labels(self):
        labels = ['work', 'personal', 'important', 'spam']
        return random.sample(labels, k=random.randint(0, 3))

    def _generate_attachments(self):
        if random.random() > 0.7:
            return [self.fake.file_name() for _ in range(random.randint(1, 3))]
        return []