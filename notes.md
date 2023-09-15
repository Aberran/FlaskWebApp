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