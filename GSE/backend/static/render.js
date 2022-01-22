const sidebar = document.getElementById("sidebar");
sidebar.innerHTML=`
<aside id="sidebar" class="sidebar">
<ul class="sidebar-nav" id="sidebar-nav">
  <li class="nav-item">
    <a class="nav-link collapsed" href="/">
      <i class="bi bi-grid"></i>
      <span>Tableau de bord</span>
    </a>
  </li>
  <!-- End Dashboard Nav -->

  <li class="nav-heading">Pages</li>
  <li class="nav-item">
    <a class="nav-link collapsed" href="http://127.0.0.1:8000/entreprises">
      <i class="bi bi-bank2"></i>
      <span>Entreprises</span>
    </a>
  </li>
  <li class="nav-item">
  <a class="nav-link collapsed" href="http://127.0.0.1:8000/encadreurs">
    <i class="bi bi-person"></i>
    <span>Encadreurs</span>
  </a>
</li>
  <li class="nav-item">
    <a class="nav-link collapsed" href="http://127.0.0.1:8000/stages">
      <i class="bi bi-stack"></i>            <span>Stages</span>
    </a>
  </li>
  <li class="nav-item">
    <a class="nav-link collapsed" href="http://127.0.0.1:8000/etudiants">
      <i class="bi bi-person"></i>
      <span>Etudiants</span>
    </a>
  </li>
  <li class="nav-item">
  <a class="nav-link collapsed" href="http://127.0.0.1:8000/enseignants">
    <i class="bi bi-person"></i>
    <span>Enseignants</span>
  </a>
</li>
<li class="nav-item">
<a class="nav-link collapsed" href="http://127.0.0.1:8000/types">
<i class="bi bi-stack"></i>   
  <span>Types de stage</span>
</a>
</li>
</ul>
</aside>`;

const header  = document.getElementById("header");
header.innerHTML = ` 
<header id="header" class="header fixed-top d-flex align-items-center">
  <div class="d-flex align-items-center justify-content-between">
    <a href="/" class="logo d-flex align-items-center">
      <img src="static/img/logo.png" alt="logo" />
      <span class="d-none d-lg-block">DREFC</span>
    </a>
    <i class="bi bi-list toggle-sidebar-btn"></i>
  </div>
  <!-- End Logo -->

  <div class="search-bar">
    <form
      class="search-form d-flex align-items-center"
      method="POST"
      action="#"
    >
      <input
        type="text"
        name="query" 
        placeholder="Search"
        title="Enter search keyword"
      />
      <button type="submit" title="Search">
        <i class="bi bi-search"></i>
      </button>
    </form>
  </div>
  <!-- End Search Bar -->
</header>
`;



const footer = document.getElementById("footer");
footer.innerHTML=`    <footer id="footer" class="footer">
<div class="copyright">
  &copy; Copyright <strong><span> ESI</span></strong
  >.| Tous droits réservés
</div>
</footer>`;


