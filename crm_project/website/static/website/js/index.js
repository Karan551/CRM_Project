console.log("Hello Django");
// const navbar = document.querySelector("#nav-bar");
const themeSwitch = document.querySelector("#theme-switch");
const themeText = document.querySelector("#theme-text");
const passwordInput = document.querySelector('input[type="password"]');
let checkboxInput = document.querySelectorAll('input[type="checkbox"]');

const darkMode = () => {
  document.documentElement.setAttribute("data-bs-theme", "dark");

  themeText.textContent = "Dark";

  localStorage["theme"] = "dark";
};

const lightMode = () => {
  document.documentElement.setAttribute("data-bs-theme", "light");

  themeText.textContent = "Light";
  localStorage["theme"] = "light";
};

//  --------------- To add event listener
themeSwitch.addEventListener("click", () => {
  themeSwitch.checked ? darkMode() : lightMode();
});
// ---------------- IIFE to reload page

(function handlePageReload() {
  const themeValue = localStorage["theme"];

  themeValue === "dark"
    ? (darkMode(), (themeSwitch.checked = true))
    : lightMode();
})();

// ---------------- To checkbox and password field
if (checkboxInput[1]) {
  checkboxInput = checkboxInput[1];
  checkboxInput.addEventListener("click", () => {
    if (checkboxInput.checked) {
      passwordInput.type = "text";
    } else {
      passwordInput.type = "password";
    }
  });
}
