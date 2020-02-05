import os
import sys
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")
django.setup()

from datacenter.models import Passcard, Visit


if __name__ == "__main__":
    # Программируем здесь
    passcard = Passcard.objects.all()
    print(passcard)
    print('Количество пропусков:', Passcard.objects.count())