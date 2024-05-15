// success/error messages
document.addEventListener('DOMContentLoaded', function () {
  var alert = document.getElementById('alert');
  if (alert) {
    setTimeout(function () {
      alert.style.display = 'none';
    }, 4000);

    var closeButton = alert.querySelector('.close');
    closeButton.addEventListener('click', function () {
      alert.style.display = 'none';
    });
  }
});

// for display account drop down menu
const dropdownMenu = document.querySelector('.dropdown-menu');
const dropdownButton = document.querySelector('.dropdown-button');

if (dropdownButton && dropdownMenu) {
  dropdownButton.addEventListener('click', (event) => {
    event.stopPropagation(); // Prevent the click event from propagating to document
    dropdownMenu.classList.toggle('show');
  });

  dropdownButton.addEventListener('mouseover', () => {
    dropdownMenu.classList.add('show');
  });

  document.addEventListener('click', (event) => {
    const isDropdownClicked =
      dropdownButton.contains(event.target) ||
      dropdownMenu.contains(event.target);
    if (!isDropdownClicked) {
      dropdownMenu.classList.remove('show');
    }
  });
}

// Upload Image
const photoInput = document.querySelector('#avatar');
const photoPreview = document.querySelector('#preview-avatar');
if (photoInput)
  photoInput.onchange = () => {
    const [file] = photoInput.files;
    if (file) {
      photoPreview.src = URL.createObjectURL(file);
    }
  };

// Scroll to Bottom
const conversationThread = document.querySelector('.room__box');
if (conversationThread)
  conversationThread.scrollTop = conversationThread.scrollHeight;
