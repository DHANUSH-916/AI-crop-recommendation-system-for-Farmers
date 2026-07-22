// ==========================================
// CropAI - Main JavaScript
// ==========================================

// -------------------------------
// Dark Mode
// -------------------------------

function toggleDarkMode() {

    document.body.classList.toggle("dark-mode");

    if (document.body.classList.contains("dark-mode")) {

        localStorage.setItem("theme", "dark");

    } else {

        localStorage.setItem("theme", "light");

    }

}

// Load saved theme

window.addEventListener("load", () => {

    const theme = localStorage.getItem("theme");

    if (theme === "dark") {

        document.body.classList.add("dark-mode");

    }

});

// -------------------------------
// Navbar Background on Scroll
// -------------------------------

window.addEventListener("scroll", () => {

    const navbar = document.querySelector(".navbar");

    if (window.scrollY > 50) {

        navbar.style.background = "rgba(27,94,32,.97)";
        navbar.style.boxShadow = "0 8px 25px rgba(0,0,0,.15)";

    } else {

        navbar.style.background = "rgba(46,125,50,.96)";
        navbar.style.boxShadow = "none";

    }

});

// -------------------------------
// Smooth Scroll
// -------------------------------

document.querySelectorAll('a[href^="#"]').forEach(anchor => {

    anchor.addEventListener("click", function (e) {

        e.preventDefault();

        const target = document.querySelector(this.getAttribute("href"));

        if (target) {

            target.scrollIntoView({

                behavior: "smooth"

            });

        }

    });

});

// -------------------------------
// Loader During Prediction
// -------------------------------

const form = document.querySelector("form");

if (form) {

    form.addEventListener("submit", function () {

        const loader = document.querySelector(".loader");

        if (loader) {

            loader.style.display = "block";

        }

    });

}

// -------------------------------
// Animate Progress Bars
// -------------------------------

window.addEventListener("load", () => {

    const bars = document.querySelectorAll(".progress-bar");

    bars.forEach(bar => {

        const width = bar.style.width;

        bar.style.width = "0";

        setTimeout(() => {

            bar.style.width = width;

        }, 300);

    });

});

// ==========================================
// Scroll Reveal Animation
// ==========================================

const observer = new IntersectionObserver((entries) => {

    entries.forEach(entry => {

        if (entry.isIntersecting) {

            entry.target.classList.add("fade-in");

        }

    });

}, {

    threshold: 0.15

});

document.querySelectorAll(

    ".feature-card, .prediction-card, .info-box"

).forEach(el => observer.observe(el));

// ==========================================
// Scroll To Top Button
// ==========================================

const topBtn = document.createElement("button");

topBtn.innerHTML = "↑";

topBtn.className = "scroll-top";

document.body.appendChild(topBtn);

topBtn.style.cssText = `

position:fixed;
bottom:25px;
right:25px;
width:50px;
height:50px;
border:none;
border-radius:50%;
background:#2E7D32;
color:white;
font-size:22px;
cursor:pointer;
display:none;
z-index:9999;
box-shadow:0 8px 20px rgba(0,0,0,.25);
transition:.3s;

`;

window.addEventListener("scroll", () => {

    if (window.scrollY > 400) {

        topBtn.style.display = "block";

    } else {

        topBtn.style.display = "none";

    }

});

topBtn.onclick = () => {

    window.scrollTo({

        top: 0,

        behavior: "smooth"

    });

};

// ==========================================
// Input Validation
// ==========================================

document.querySelectorAll("input[type='number']").forEach(input => {

    input.addEventListener("input", function () {

        if (this.value < 0) {

            this.value = "";

        }

    });

});

// ==========================================
// Success Notification
// ==========================================

window.addEventListener("load", () => {

    const cropTitle = document.querySelector(".result-card h2");

    if (cropTitle) {

        const toast = document.createElement("div");

        toast.innerHTML = "✅ Prediction completed successfully!";

        toast.style.cssText = `

position:fixed;
top:20px;
right:20px;
background:#2E7D32;
color:white;
padding:15px 25px;
border-radius:10px;
font-weight:600;
z-index:9999;
box-shadow:0 8px 25px rgba(0,0,0,.2);

`;

        document.body.appendChild(toast);

        setTimeout(() => {

            toast.remove();

        }, 3000);

    }

});

// ==========================================
// Current Year in Footer (Optional)
// ==========================================

const yearElement = document.getElementById("currentYear");

if (yearElement) {

    yearElement.textContent = new Date().getFullYear();

}

// ==========================================
// Console Welcome
// ==========================================

console.log("🌱 CropAI Loaded Successfully");