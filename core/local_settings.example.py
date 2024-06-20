from pathlib import Path


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

# SECURITY WARNING: keep the secret key used in production secret!
# python -c "import string as s; from secrets import SystemRandom as SR; print(''.join(SR().choices(s.ascii_letters + s.digits + s.punctuation, k=64)));"
SECRET_KEY = '''$L3lp]C`!M24{!&*LtLtdbR[_J.&CXz/:))6svGW_v4FNS7aVuetwK%Tc6p1jGz3'''  # nosec

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': Path(__file__).resolve().parent.parent / 'db.sqlite3',
    }
}


POWERBI_SERVICE_STREAM_ENDPOINT = r'''https://api.powerbi.com/beta/[...]'''
CSV_STREAM_PATH = Path(__file__).resolve().parent.parent / 'stream.csv'
