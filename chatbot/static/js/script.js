// document.addEventListener("DOMContentLoaded", () => {
//     const chatForm = document.getElementById("chat-form");
//     const userInput = document.getElementById("user-input");
//     const chatDisplay = document.getElementById("chat-display");

//     chatForm.addEventListener("submit", async (e) => {
//         e.preventDefault();
//         const userMessage = userInput.value.trim();

//         if (userMessage) {
//             addMessageToDisplay("user", userMessage);
//             userInput.value = "";

//             try {
//                 const response = await fetch("/chat/", {
//                     method: "POST",
//                     headers: {
//                         "Content-Type": "application/json",
//                         "X-CSRFToken": getCSRFToken(),
//                     },
//                     body: JSON.stringify({ user_input: userMessage }),
//                 });

//                 const data = await response.json();
//                 if (data.response) {
//                     addMessageToDisplay("bot", data.response);
//                 }
//             } catch (error) {
//                 addMessageToDisplay("bot", "An error occurred. Please try again.");
//             }
//         }
//     });

//     function addMessageToDisplay(sender, text) {
//         const messageContainer = document.createElement("div");
//         messageContainer.classList.add("message", sender + "-message");

//         const messageText = document.createElement("p");
//         messageText.textContent = text;

//         messageContainer.appendChild(messageText);
//         chatDisplay.appendChild(messageContainer);
//         chatDisplay.scrollTop = chatDisplay.scrollHeight;
//     }

//     function getCSRFToken() {
//         return document.querySelector("[name=csrfmiddlewaretoken]").value;
//     }
// });



// Add typing effect simulation for bot response
function simulateTyping(botMessage) {
    const chatBox = document.getElementById("chat-box");
    let i = 0;
    chatBox.innerHTML = "";
    const typingInterval = setInterval(() => {
        chatBox.innerHTML += botMessage.charAt(i);
        i++;
        if (i > botMessage.length) clearInterval(typingInterval);
    }, 30);
}

window.onload = function () {
    const botMessage = document.getElementById("bot-response").textContent.trim();
    if (botMessage) simulateTyping(botMessage);
};
