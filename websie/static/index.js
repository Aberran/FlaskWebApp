function deleteNote(noteId) {

    fetch("/delete-note", {
      method: "POST",
      body: JSON.stringify({ noteId: noteId }),
    }).then((_res) => {
      window.location.reload();
    });
  }

  document.addEventListener("DOMContentLoaded", function () {
    let themeSwitcher = document.getElementById("themeSwitcher");
    let bodyElement = document.body;
    let signupButton = document.querySelector("#signUp");
    let mediaIconsGitHub = document.querySelector('#media-icons-gitHub');
    let mediaIconsLinkedIn = document.querySelector('#media-icons-linkedIn');

    // Check if the theme preference is stored in local storage
    if (localStorage.getItem("theme") === "light") {
      bodyElement.dataset.bsTheme = "light";
      themeSwitcher.checked = true;
    }

    bodyElement.classList.remove("d-none");

    // Add an event listener to the theme switcher checkbox
    themeSwitcher.addEventListener("change", function () {
      if (this.checked) {
        bodyElement.dataset.bsTheme = "light";
        localStorage.setItem("theme", "light");
      } else {
        bodyElement.dataset.bsTheme = "dark";
        localStorage.setItem("theme", "dark");
      }
      updateTheme();
    });

    function updateTheme() {
      let currentTheme = bodyElement.dataset.bsTheme;
      if (currentTheme === "light") {
        signupButton.classList.add("text-dark", "border-black");
        mediaIconsGitHub.classList.add("text-dark");
        mediaIconsLinkedIn.classList.add("text-dark");
      } else {
        signupButton.classList.remove("text-dark", "border-black");
        mediaIconsGitHub.classList.remove("text-dark");
        mediaIconsLinkedIn.classList.remove("text-dark");
      }
    }

    updateTheme(); // Call the function on page load
  });