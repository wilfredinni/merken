let scrollButton = document.getElementById("scroll");
scrollButton.style.display = "none";
window.onscroll = function() {
  scrollFunction();
};

function scrollFunction() {
  if (document.documentElement.scrollTop > 200) {
    scrollButton.style.display = "block";
  } else {
    scrollButton.style.display = "none";
  }
}
let intervalId = 0;

function scrollStep() {
  if (window.pageYOffset === 0) {
    clearInterval(intervalId);
  }
  window.scroll(0, window.pageYOffset - 2e3);
}

function scrollToTop() {
  intervalId = setInterval(scrollStep, 16.66);
}
scrollButton.addEventListener("click", scrollToTop);


// index message
let message = document.getElementById("HomeMessage");
let closeNotificationBtn = document.getElementById("closeNotification");

// functions
const closeMessage = () => (message.style.display = "none");

// listeners
closeNotificationBtn.addEventListener("click", closeMessage);


