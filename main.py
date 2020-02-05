import os
import sys
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")
django.setup()

from datacenter.models import Passcard, Visit

if __name__ == "__main__":
    # Программируем здесь
    is_activ_cards = []
    is_activ_cards = Passcard.objects.filter(is_active=True)
    print('Активных пропусков:', len(is_activ_cards))
    print('Количество пропусков:', Passcard.objects.count())
