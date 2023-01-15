##
#

def main():

    with open("commands.txt") as command_file:
        command_lines = [i.split() for i in command_file]
    commands = [line for line in command_lines]

    with open("schedule.txt") as schedule_file:
        schedule_lines = [i.strip().split(";") for i in schedule_file]

    schedule = {}
    for line in schedule_lines:
        
        day = line[0]
        time = line[1]

        if day not in schedule:
            schedule[day] = {time: line[2]}
        else:
            schedule[day][time] = line[2]

    for command in commands:

        day = command[1]
        action = command[0]
        
        if action == "v":

            print(f"\nViewing current appointments scheduled for day {day}:")
            for appointment in schedule[day]:
                print(appointment, schedule[day][appointment], sep=": ")

        else:

            time = command[2]
            print(f"\nInserting appointment on day {day}, at {time}...")
            if day in schedule and time in schedule[day]:
                print("Appointment scheduling unsuccessful. Time frame already occupied.")
                continue
            schedule[day] = {}
            schedule[day].update({time: " ".join(command[2:])})
            print("Appointment scheduling successful!")

main()