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



// ---------------------------------------------------------------------Correct

// Add typing effect simulation for bot response
// function simulateTyping(botMessage) {
//     const chatBox = document.getElementById("chat-box");
//     let i = 0;
//     chatBox.innerHTML = "";
//     const typingInterval = setInterval(() => {
//         chatBox.innerHTML += botMessage.charAt(i);
//         i++;
//         if (i > botMessage.length) clearInterval(typingInterval);
//     }, 30);
// }

// window.onload = function () {
//     const botMessage = document.getElementById("bot-response").textContent.trim();
//     if (botMessage) simulateTyping(botMessage);
// };



// -----------------------------------------------------------------------Correct


const chatBox = document.getElementById("chat-messages");
chatBox.scrollTop = chatBox.scrollHeight;














































// Simple chatbot logic
// function chatbot(input) {
//     let output = "";
//     input = input.toLowerCase();
//     if (input.includes("hello") || input.includes("hi")) {
//         output = "Hello, nice to meet you!";
//     } else if (input.includes("how are you")) {
//         output = "I'm doing fine, thank you for asking.";
//     } else if (input.includes("what is your name")) {
//         output = "My name is Jarvis, I'm a chatbot.";
//     } else if (input.includes("what can you do")) {
//         output = "I can chat with you and answer some simple questions.";
//     } else if (input.includes("tell me a joke")) {
//         output = "Why did the chicken go to the seance? To get to the other side.";
//     } else {
//         output = "Sorry, I don't understand that. Please try something else.";
//     }
//     return output;
// }

// // Display the user message in the chat
// function displayUserMessage(message) {
//     let chat = document.getElementById("chat");
//     let userMessage = document.createElement("div");
//     userMessage.classList.add("message", "user");
//     let userAvatar = document.createElement("div");
//     userAvatar.classList.add("avatar");
//     let userText = document.createElement("div");
//     userText.classList.add("text");
//     userText.innerHTML = message;
//     userMessage.appendChild(userAvatar);
//     userMessage.appendChild(userText);
//     chat.appendChild(userMessage);
//     chat.scrollTop = chat.scrollHeight;
// }

// // Display the bot message in the chat
// function displayBotMessage(message) {
//     let chat = document.getElementById("chat");
//     let botMessage = document.createElement("div");
//     botMessage.classList.add("message", "bot");
//     let botAvatar = document.createElement("div");
//     botAvatar.classList.add("avatar");
//     let botText = document.createElement("div");
//     botText.classList.add("text");
//     botText.innerHTML = message;
//     botMessage.appendChild(botAvatar);
//     botMessage.appendChild(botText);
//     chat.appendChild(botMessage);
//     chat.scrollTop = chat.scrollHeight;
// }

// // Handle form submission
// document.querySelector(".chat-form").addEventListener("submit", function(event) {
//     event.preventDefault(); // Prevent default form submission
//     let input = document.getElementById("input").value;
//     if (input) {
//         displayUserMessage(input);
//         let output = chatbot(input);
//         setTimeout(function() {
//             displayBotMessage(output);
//         }, 1000);
//         document.getElementById("input").value = "";
//     }
// });









// Check for bot response in the template
// document.addEventListener('DOMContentLoaded', () => {
//     const botResponse = document.getElementById('bot-response');
//     if (botResponse) {
//         botResponse.scrollIntoView();
//     }
// });

// // Optional: Additional JS functionality for client-side input
// const inputField = document.querySelector('.input');
// const form = document.querySelector('.chat-form');

// form.addEventListener('submit', (event) => {
//     const userInput = inputField.value.trim();
//     if (!userInput) {
//         event.preventDefault();
//         alert("Please enter a message.");
//     }
// });























// function simulateTyping(botMessage) {
//     const chatBox = document.getElementById("chat-box");
//     let i = 0;
//     chatBox.innerHTML = "";
//     const typingInterval = setInterval(() => {
//         chatBox.innerHTML += botMessage.charAt(i);
//         i++;
//         if (i > botMessage.length) clearInterval(typingInterval);
//     }, 30);
// }

// window.onload = function () {
//     const botMessage = document.getElementById("bot-response").textContent.trim();
//     if (botMessage) simulateTyping(botMessage);
// };

// // New chat button functionality
// document.getElementById("new-chat-btn").addEventListener("click", function () {
//     const chatHistory = document.getElementById("chat-history");
//     chatHistory.innerHTML = "<li>Starting a new chat...</li>";
//     document.getElementById("chat-box").innerHTML = "<p>Ask something to start the conversation!</p>";
// });











// Add typing effect simulation for bot response
// function simulateTyping(botMessage) {
//     const chatBox = document.getElementById("chat-box");
//     let i = 0;
//     chatBox.innerHTML = "";
//     const typingInterval = setInterval(() => {
//         chatBox.innerHTML += botMessage.charAt(i);
//         i++;
//         if (i > botMessage.length) clearInterval(typingInterval);
//     }, 30);
// }

// window.onload = function () {
//     const botMessage = document.getElementById("bot-response").textContent.trim();
//     if (botMessage) simulateTyping(botMessage);
// };




// ****************************************************************************************** using template

// Function to generate bot response (can be replaced with actual bot logic)
// function getBotResponse(userInput) {
//     return `Bot says: ${userInput}`;
// }

// // Send button click event handler
// $('#sendBtn').on('click', function() {
//     var userMessage = $('#userInput').val().trim();
//     if (userMessage !== "") {
//         // Add user message to the chat body
//         var userMessageHTML = `<div class="chat-box-body-send">
//                                     <p>${userMessage}</p>
//                                     <span>${new Date().toLocaleTimeString()}</span>
//                                 </div>`;
//         $('#chatBody').append(userMessageHTML);
        
//         // Scroll to the bottom of the chat body
//         $('#chatBody').scrollTop($('#chatBody')[0].scrollHeight);

//         // Clear the input field
//         $('#userInput').val('');

//         // Get bot response and add it to the chat
//         var botMessage = getBotResponse(userMessage);
//         var botMessageHTML = `<div class="chat-box-body-receive">
//                                     <p>${botMessage}</p>
//                                     <span>${new Date().toLocaleTimeString()}</span>
//                                 </div>`;
//         $('#chatBody').append(botMessageHTML);

//         // Scroll to the bottom after bot response
//         $('#chatBody').scrollTop($('#chatBody')[0].scrollHeight);
//     }
// });

// // Enter key functionality to send message
// $('#userInput').on('keypress', function(event) {
//     if (event.key === 'Enter') {
//         $('#sendBtn').click();
//     }
// });

// // Open chat when the chat button is clicked
// $('.chat-button').on('click', function() {
//     $('.chat-button').css({"display": "none"});
//     $('.chat-box').css({"visibility": "visible"});
// });

// // Close chat when the header close icon is clicked
// $('.chat-box .chat-box-header p').on('click', function() {
//     $('.chat-button').css({"display": "block"});
//     $('.chat-box').css({"visibility": "hidden"});
// });

// // Modal functionality (for extra options)
// $("#addExtra").on("click", function() {
//     $(".modal").toggleClass("show-modal");
// });
// $(".modal-close-button").on("click", function() {
//     $(".modal").toggleClass("show-modal");
// });




// ****************************************************************************************** using template