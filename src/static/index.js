var ws = new WebSocket("ws://localhost:8000/ws");
var sendButton = document.getElementById("sendButton");
var userInput = document.getElementById("userInput");
var chatHistory = document.getElementById("chatHistory");
var lastUserMessageDiv = null;
var isNewUserInput = true;

ws.onmessage = function (event) {
  var message = event.data.trim();

  if (lastUserMessageDiv && !isNewUserInput) {
    var shouldAddSpace = true;
    var noPrependSpaceChars = [",", ".", "!", "?", ";", ":"];
    if (noPrependSpaceChars.includes(message.charAt(0))) {
      shouldAddSpace = false;
    }
    lastUserMessageDiv.querySelector(".message-content").textContent +=
      (shouldAddSpace ? " " : "") + message;
  } else {
    var messageContainer = document.createElement("div");
    messageContainer.classList.add("message-container", "ai-response");

    var messageContent = document.createElement("div");
    messageContent.classList.add("message-content");
    messageContent.textContent = message;

    messageContainer.appendChild(messageContent);
    chatHistory.appendChild(messageContainer);
    lastUserMessageDiv = messageContainer;
    isNewUserInput = false;
  }
};

sendButton.addEventListener("click", sendMessage);

function sendMessage() {
  var message = userInput.value.trim();

  if (message) {
    var userInputContainer = document.createElement("div");
    userInputContainer.classList.add("message-container", "user-input");

    var userInputContent = document.createElement("div");
    userInputContent.classList.add("message-content");
    userInputContent.textContent = message;

    userInputContainer.appendChild(userInputContent);
    chatHistory.appendChild(userInputContainer);
    chatHistory.scrollTop = chatHistory.scrollHeight;
  }

  ws.send(message);
  userInput.value = "";
  isNewUserInput = true;
  lastUserMessageDiv = null;
}

userInput.addEventListener("keypress", function (event) {
  if (event.key === "Enter" && !event.ctrlKey) {
    event.preventDefault();
    sendMessage();
  }
});
