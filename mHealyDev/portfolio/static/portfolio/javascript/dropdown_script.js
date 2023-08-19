function toggleDropdown(dropdownId) {
  var dropdown = document.getElementById(dropdownId);
  if (dropdown.classList.contains("show")) {
    dropdown.classList.remove("show");
  } else {
    dropdown.classList.add("show");
  }
}

document.addEventListener("DOMContentLoaded", function () {
  var dropdownButtons = document.querySelectorAll(
    ".custom-dropdown button.dropdown-toggle"
  );

  dropdownButtons.forEach(function (button) {
    button.addEventListener("mouseenter", function () {
      var dropdownId = this.getAttribute("data-bs-target").replace("#", "");
      toggleDropdown(dropdownId);
    });

    button.addEventListener("mouseleave", function () {
      var dropdownId = this.getAttribute("data-bs-target").replace("#", "");
      toggleDropdown(dropdownId);
    });
  });
});
