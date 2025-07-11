from utils.email_sender import EmailSender
from generators.email_generator import EmailGenerator
import os
from dotenv import load_dotenv
from configs import settings

# Загрузка переменных окружения из .env файла
load_dotenv()


def main():
    generator = EmailGenerator()

    emails = generator.generate_email(count=1000)

    smtp_config = {
        'server': os.getenv('SMTP_SERVER', 'smtp.gmail.com'),
        'port': int(os.getenv('SMTP_PORT', 587)),
        'username': os.getenv('SMTP_USERNAME'),
        'password': os.getenv('SMTP_PASSWORD')
    }

    sender = EmailSender(**smtp_config)

    try:
        print(f"Начинаю отправку {len(emails)} писем...")
        sender.send_emails(emails)
        print("Все письма успешно отправлены!")
    except Exception as e:
        print(f"Ошибка при отправке: {str(e)}")


if __name__ == "__main__":
    main()