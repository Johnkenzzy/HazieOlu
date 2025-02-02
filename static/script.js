document.getElementById('hamburger').addEventListener('click', () => {
  const navLinks = document.querySelector('.nav-links');
  const hamburgerIcon = document.getElementById('hamburger');

  // Toggle the active class for the nav and the hamburger icon
  navLinks.classList.toggle('active');
  hamburgerIcon.classList.toggle('active');
});


function toggleDescription(element) {
    const shortText = element.querySelector('.short-text');
    const fullText = element.querySelector('.full-text');

    if (fullText.style.display === 'none') {
        fullText.style.display = 'inline';
        shortText.style.display = 'none';
        element.classList.add('expanded');
    } else {
        fullText.style.display = 'none';
        shortText.style.display = 'inline';
        element.classList.remove('expanded');
    }
}


function startCountdown() {
  document.querySelectorAll('.timer').forEach(timer => {
      let deadline = new Date(timer.dataset.deadline).getTime();

      function updateTimer() {
          let now = new Date().getTime();
          let timeLeft = deadline - now;

          if (timeLeft <= 0) {
              timer.innerHTML = "Time's up!";
              timer.parentElement.classList.add('danger');
              return;
          }

          let days = Math.floor(timeLeft / (1000 * 60 * 60 * 24));
          let hours = Math.floor((timeLeft % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
          let minutes = Math.floor((timeLeft % (1000 * 60 * 60)) / (1000 * 60));
          let seconds = Math.floor((timeLeft % (1000 * 60)) / 1000);

          timer.innerHTML = `${days}d ${hours}h ${minutes}m ${seconds}s`;

          // Add warning class if time is less than 1 day
          if (timeLeft < 24 * 60 * 60 * 1000) {
              timer.parentElement.classList.add('warning');
          }

          setTimeout(updateTimer, 1000);
      }

      updateTimer();
  });
}

document.addEventListener('DOMContentLoaded', startCountdown);
