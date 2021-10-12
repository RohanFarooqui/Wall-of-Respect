##-> Other Libs
from datetime import datetime

def get_date_time():
    now = datetime.now()
    dt = now.strftime("%d/%m/%Y %H:%M %p") # in dd/mm/YY H:M:S AM/PM

    dt = dt.replace('/','-')
    dt = dt.replace(':','%')

    return dt


def get_date():
    now = datetime.now()
    d = now.strftime("%d/%m/%Y") # in dd/mm/YY

    d = d.replace('/','-')

    return d

def get_time():
    now = datetime.now()
    t = now.strftime("%H:%M %p") # in  H:M:S AM/PM

    return t