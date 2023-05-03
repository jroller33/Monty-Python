class Event:
    def __init__(self, event_date, event_type, machine_name, user):
        self.date = event_date
        self.type = event_type
        self.machine = machine_name
        self.user = user

events = [
    Event('2020-01-21 12:45:56', 'login', 'myworkstation.local', 'Dwight'),
    Event('2020-01-22 15:53:42', 'logout', 'webserver.local', 'Dwight'),
    Event('2020-01-21 18:53:21', 'login', 'webserver.local', 'Jim'),
    Event('2020-01-22 10:25:34', 'logout', 'myworkstation.local', 'Dwight'),
    Event('2020-01-21 08:20:01', 'login', 'webserver.local', 'Dwight'),
    Event('2020-01-23 11:24:35', 'logout', 'mailserver.local', 'Michael'),
]