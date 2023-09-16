<!-- old nav bar -->

<nav class="navabar navbar-expand-lg navbar-light bg-transparent">
      <div class='container'> 
        <button 
          class="navbar-toggler" 
          type="button" 
          data-toggle="collapse" 
          data-target="#navbar">
          <span class="navbar-toggler-icon"></span>
        </button>
          <div class="collapse navbar-collapse" id="navbar">
            <div class="navbar-nav">
              {% if user.is_authenticated %}
              <a href="/" class="nav-item nav-link" id="'Logo">Logo</a>
              <a href="/home" class="nav-item nav-link" id="'home">Home</a>
              <a href="/logout" class="nav-item nav-link" id="'logout">Logout</a>
              {% else %}
              <a href="/" class="nav-item nav-link" id="'Logo">Logo</a>
              <a href="/login" class="nav-item nav-link" id="'login">Login</a>
              <a href="/sign-up" class="nav-item nav-link" id="'signUp">Sign Up</a>
              {% endif %}
            </div>
          </div>
      </div>
    </nav>

    <script
      src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js"
      integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl"
      crossorigin="anonymous"
    ></script>

    <link
      rel="stylesheet"
      href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css"
      integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh"
      crossorigin="anonymous"
    />
    <link
      rel="stylesheet"
      href="https://stackpath.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css"
      crossorigin="anonymous"
    />

    <script
      src="https://code.jquery.com/jquery-3.2.1.slim.min.js"
      integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN"
      crossorigin="anonymous"
    ></script>
    <script
      src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js"
      integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q"
      crossorigin="anonymous"
    ></script>
    <script
      src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js"
      integrity="sha384-C6RzsynM9kWDrMNeT87bh95OGNyZPhcTNXj1NW7RuBCsyN/o0jlpcV8Qyq46cDfL"
      crossorigin="anonymous"
    ></script>

    function setDarkMode() {
        let bodyElement = document.body;
        let signupButton = document.querySelector("#signUp");
        let signupHref = document.querySelector("#sign-up-href");
        let textAreas = document.querySelector(".form-control");
        let subButtons = document.querySelector(".btn");

        const currentTheme = (bodyElement.dataset.bsTheme =
          bodyElement.dataset.bsTheme == "light" ? "dark" : "light");
        localStorage.setItem("theme", currentTheme);
        console.log(currentTheme);

        // Toggle Bootstrap classes for the navigation bar
        signupButton.classList.toggle("border-dark");
        signupButton.classList.toggle("border-light");

        // Toggle text color
        signupButton.classList.toggle("text-black");
        signupButton.classList.toggle("text-white");

        // links
        signupHref.classList.toggle("link-dark");
        signupHref.classList.toggle("link-light");

        // submit buttons
        subButtons.classList.toggle("btn-dark");
        subButtons.classList.toggle("border-light");
      }

      function checkTheme() {
        const currentTheme = localStorage.getItem("theme");
        if (currentTheme) {
          let bodyElement = document.body;
          bodyElement.dataset.bsTheme = currentTheme;
          let checkbox = document.getElementById("selector");
          // Apply styles based on the theme
          if (currentTheme == "dark") {
            checkbox.checked = true;
            // Apply dark mode styles
            // ...
          } else {
            checkbox.checked = false;
            // Apply light mode styles
            // ...
          }
        }
      }
      checkTheme();