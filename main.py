# main.py
# This program stores information about school clubs using a dictionary
# and displays the selected club's details using a function.

# Dictionary that contains all club information
# Each key is the club name, and the value is another dictionary
# holding the club's details.
clubs = {
    "Marching Band": {
        "description": "Perform and practice marching routines for events.",
        "meeting_time": "Tuesday and Wednesday 03:00-4:30 PM",
        "location": "Band Room",
        "moderator": "Mr. Emilio Alumno",
        "members": 20
    },
    "Glee Club": {
        "description": "Vocal performances and music-related activities.",
        "meeting_time": "Monday 03:00-05:00 PM",
        "location": "High School Music Room",
        "moderator": "Mr. Denver Martin",
        "members": 15
    },
    "Dance Club": {
        "description": "Dance practice and performances for school events.",
        "meeting_time": "Tuesday 03:00-05:00 PM",
        "location": "Teatro Preciosa",
        "moderator": "Mr. Alfred Cases",
        "members": 18
    },
    "Math Club": {
        "description": "Explores mathematical concepts and problem-solving.",
        "meeting_time": "Monday 02:30-03:00 PM",
        "location": "Room 404",
        "moderator": "Mr. Nicole Gabuya",
        "members": 12
    },
    "Science Club": {
        "description": "Encourages scientific thinking through experiments and research.",
        "meeting_time": "Tuesday 03:00-04:00 PM",
        "location": "Room 404",
        "moderator": "Ms. Jameelyn Maramag",
        "members": 22
    },
    "Communications Arts Club": {
        "description": "Focuses on media, communication, and arts activities.",
        "meeting_time": "Wednesday 03:00-04:00 PM, Friday 03:00-04:00 PM",
        "location": "Room 406",
        "moderator": "Ms. Yannis Fernandez",
        "members": 14
    },
    "COCC": {
        "description": "Cadet Officer Candidate Course training program.",
        "meeting_time": "Wednesday 02:30-04:30 PM",
        "location": "Quadrangle/ Teatro Preciosa",
        "moderator": "SSgt. Jemima David PA (Res)",
        "members": 16
    },
    "Social Science Club": {
        "description": "Discusses social issues and community projects.",
        "meeting_time": "Tuesday 03:00-04:00 PM",
        "location": "Room 409",
        "moderator": "Mr. Roberto Lim",
        "members": 13
    },
    "Volleyball Varsity": {
        "description": "Varsity-level volleyball practice and competitions.",
        "meeting_time": "Wednesday 03:00-04:00 PM",
        "location": "Quadrangle",
        "moderator": "Mr. Adrian Ruiz",
        "members": 20
    },
    "Basketball Varsity": {
        "description": "Varsity-level basketball practice and competitions.",
        "meeting_time": "Monday 03:00-04:00 PM",
        "location": "Quadrangle",
        "moderator": "Mr. Adrian Ruiz",
        "members": 18
    }
}

# Function that displays club information based on user input
def display_club_info():
    # Displays the list of available clubs
    print("Available Clubs:")
    for club in clubs:
        print("-", club)

    # Asks the user to input the name of the club they want to view
    choice = input("\nEnter club name: ")

    # Checks if the input exists in the dictionary
    if choice in clubs:
        club = clubs[choice]

        # Displays all details of the selected club
        print("\n--- Club Information ---")
        print("Description:", club["description"])
        print("Meeting Time:", club["meeting_time"])
        print("Location:", club["location"])
        print("Club Moderator:", club["moderator"])
        print("Number of Members:", club["members"])
    else:
        # Displays a message if the club is not found
        print("Club not found.")

# Calls the function to run the program
display_club_info()

