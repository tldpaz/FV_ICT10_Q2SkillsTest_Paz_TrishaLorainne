// script.js
// This script controls the interaction between the dropdown menu
// and the displayed club information on the webpage.

// Object that stores club information
// Each club name acts as a key with its details as values
const clubs = {
    "Marching Band": {
        description: "Perform and practice marching routines for events.",
        meeting: "Tuesday and Wednesday 03:00-4:30 PM",
        location: "Band Room",
        moderator: "Mr. Emilio Alumno",
        members: 20
    },
    "Glee Club": {
        description: "Vocal performances and music-related activities.",
        meeting: "Monday 03:00-05:00 PM",
        location: "High School Music Room",
        moderator: "Mr. Denver Martin",
        members: 15
    },
    "Dance Club": {
        description: "Dance practice and performances for school events.",
        meeting: "Tuesday 03:00-05:00 PM",
        location: "Teatro Preciosa",
        moderator: "Mr. Alfred Cases",
        members: 18
    },
    "Math Club": {
        description: "Explores mathematical concepts and problem-solving.",
        meeting: "Monday 02:30-03:00 PM",
        location: "Room 404",
        moderator: "Mr. Nicole Gabuya",
        members: 12
    },
    "Science Club": {
        description: "Encourages scientific thinking through experiments and research.",
        meeting: "Tuesday 03:00-04:00 PM",
        location: "Room 404",
        moderator: "Ms. Jameelyn Maramag",
        members: 22
    },
    "Communications Arts Club": {
        description: "Focuses on media, communication, and arts activities.",
        meeting: "Wednesday 03:00-04:00 PM, Friday 03:00-04:00 PM",
        location: "Room 406",
        moderator: "Ms. Yannis Fernandez",
        members: 14
    },
    "COCC": {
        description: "Cadet Officer Candidate Course training program.",
        meeting: "Wednesday 02:30-04:30 PM",
        location: "Quadrangle/ Teatro Preciosa",
        moderator: "SSgt. Jemima David PA (Res)",
        members: 16
    },
    "Social Science Club": {
        description: "Discusses social issues and community projects.",
        meeting: "Tuesday 03:00-04:00 PM",
        location: "Room 409",
        moderator: "Mr. Roberto Lim",
        members: 13
    },
    "Volleyball Varsity": {
        description: "Varsity-level volleyball practice and competitions.",
        meeting: "Wednesday 03:00-04:00 PM",
        location: "Quadrangle",
        moderator: "Mr. Adrian Ruiz",
        members: 20
    },
    "Basketball Varsity": {
        description: "Varsity-level basketball practice and competitions.",
        meeting: "Monday 03:00-04:00 PM",
        location: "Quadrangle",
        moderator: "Mr. Adrian Ruiz",
        members: 18
    }
};

// Function that displays the selected club's information
function showClubInfo() {
    // Gets the selected value from the dropdown menu
    const clubName = document.getElementById("clubSelect").value;

    // Retrieves the club information from the object
    const club = clubs[clubName];

    // Displays the club details
    document.getElementById("clubInfo").innerHTML = `
        <h5>${clubName}</h5>
        <p><strong>Description:</strong> ${club.description}</p>
        <p><strong>Meeting Time:</strong> ${club.meeting}</p>
        <p><strong>Location:</strong> ${club.location}</p>
        <p><strong>Club Moderator:</strong> ${club.moderator}</p>
        <p><strong>Number of Members:</strong> ${club.members}</p>
    `;
}

