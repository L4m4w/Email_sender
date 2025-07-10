import pytest
from generators.email_generator import EmailGenerator

@pytest.fixture(scope='module')
def email_generator():
    return EmailGenerator()

@pytest.fixture(scope='module')
def generated_emails(email_generator):
    return email_generator.generate_email(count=1000)