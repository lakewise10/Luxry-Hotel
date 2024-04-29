// Nav-Bar
var nav = document.querySelector("nav");
window.addEventListener("scroll", function () {
  if (this.window.pageYOffset > 100) {
    nav.classList.add("bg-dark", "shadow");
  } else {
    nav.classList.remove("bg-dark");
  }
});

// JS Counter
let nums = document.querySelectorAll(".nums .num");
let section = document.querySelector(".reviews");
let started = false;

window.onscroll = function () {
  if (window.scrollY >= section.offsetTop) {
    if (!started) {
      nums.forEach((num) => startCount(num));
    }
    started = true;
  }
};

function startCount(el) {
  let goal = el.dataset.goal;
  let count = setInterval(() => {
    el.textContent++;
    if (el.textContent == goal) {
      clearInterval(count);
    }
  }, 1000 / goal);
}
