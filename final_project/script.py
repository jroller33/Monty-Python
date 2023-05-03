import logging
import event    # event.py module
from event import events

logging.basicConfig(filename='final_project/current_users.log', encoding='utf-8', level=logging.INFO, force=True)   # 'force=True' is required. also make sure to include relative file path


def get_event_date(event):
    return event.date

def current_users(events):
    events.sort(key=get_event_date)

    machines = {} 

    for event in events:
        if event.machine not in machines:
            machines[event.machine] = set()

        if event.type == "login":
            machines[event.machine].add(event.user)

        elif event.type == "logout" and event.user in machines:
            machines[event.machine].remove(event.user)

    return machines


def generate_log(machines):
    for machine, users in machines.items():
        if len(users) > 0:
            user_list = ", ".join(users)
            logging.info(f"{machine}: {user_list}")

users = current_users(events)
generate_log(users)



# logging.debug('So should this')
# logging.warning('And this, too')
# logging.error('And non-ASCII stuff, too, like Øresund and Malmö')




# numbers1 = [4, 5, 2, 9, 6, 3, 7]
# numbers1.sort() # modifies the original list
# print(numbers1)

# nums2 = [2, 5, 3, 7, 9, 6, 8]

# print(sorted(nums2))    # sorted() doesn't modify the original list
# print(nums2)


# names = ["Dwight", "Angela", "Jim", "Pam"]
# print(sorted(names)) # sorts alphabetically by default if it's a list of strings

# print(sorted(names, key=len)) # sorts by the length of each string in the list
