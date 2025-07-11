from utils.email_sender import EmailSender
from generators.email_generator import EmailGenerator
import os
from dotenv import load_dotenv
from configs import settings

# Загрузка переменных окружения из .env файла
load_dotenv()


def main():
    generator = EmailGenerator()

    emails = generator.generate_email(count=1)

    smtp_config = {
        'smtp_server': settings.user_data.server,
        'smtp_port': settings.user_data.port,
        'username': settings.user_data.username,
        'password': settings.user_data.password
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