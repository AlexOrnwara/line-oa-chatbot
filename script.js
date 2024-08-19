// script.js

const userList = document.getElementById('user-list');
const refreshButton = document.getElementById('refresh-button');

// Function to fetch user IDs from the API
async function fetchUserIds() {
    try {
        const response = await fetch('https://line-chatbot-nine.vercel.app/webhook'); // Replace with your actual API endpoint
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        const data = await response.json();
        displayUserIds(data.userIds); // Assuming the response contains an array of user IDs
    } catch (error) {
        console.error('Error fetching user IDs:', error);
        userList.innerHTML = '<li>Error fetching user IDs.</li>';
    }
}

// Function to display user IDs in the UI
function displayUserIds(userIds) {
    userList.innerHTML = ''; // Clear the list
    userIds.forEach(userId => {
        const li = document.createElement('li');
        li.textContent = userId;
        userList.appendChild(li);
    });
}

// Event listener for the refresh button
refreshButton.addEventListener('click', fetchUserIds);

// Fetch user IDs on page load
fetchUserIds();