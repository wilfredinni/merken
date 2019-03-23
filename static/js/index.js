// index message
let message = document.getElementById("HomeMessage");
let closeNotificationBtn = document.getElementById("closeNotification");


const closeMessage = () => (message.style.display = "none");
closeNotificationBtn.addEventListener("click", closeMessage);
