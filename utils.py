from datetime import datetime


def get_now():
    return datetime.now().strftime("%Y-%m-%dT %H:%M:%SZ")
