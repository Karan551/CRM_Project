console.log("Hello Django");
// const navbar = document.querySelector("#nav-bar");
const themeSwitch = document.querySelector("#theme-switch");
const themeText = document.querySelector("#theme-text");

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

themeSwitch.addEventListener("click", () => {
  themeSwitch.checked ? darkMode() : lightMode();
});
// ----------------

(function handlePageReload() {
  const themeValue = localStorage["theme"];

  themeValue === "dark"
    ? (darkMode(), (themeSwitch.checked = true))
    : lightMode();
})();
