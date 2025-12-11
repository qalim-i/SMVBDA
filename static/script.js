const btn = document.getElementById("langToggle");
const currentPath = window.location.pathname;

// Set correct button text
if (currentPath.includes("kannada")) {
  btn.textContent = "English";
} else {
  btn.textContent = "Kannada";
}

// Handle page switch
btn.addEventListener("click", () => {
  if (currentPath.includes("kannada")) {
    window.location.href = "/";
  } else {
    window.location.href = "/kannada/";
  }
});
