document.getElementById('hamburger').addEventListener('click', () => {
  const navLinks = document.querySelector('.nav-links');
  const hamburgerIcon = document.getElementById('hamburger');

  // Toggle the active class for the nav and the hamburger icon
  navLinks.classList.toggle('active');
  hamburgerIcon.classList.toggle('active');
});
