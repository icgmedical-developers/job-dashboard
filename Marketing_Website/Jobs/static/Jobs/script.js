//$(document).ready(function() {
//$('.search-box').focus();
//});

const wrapper = document.querySelector(".wrapper");
const header = document.querySelector(".header");

wrapper.addEventListener("scroll", (e) => {
 e.target.scrollTop > 30
  ? header.classList.add("header-shadow")
  : header.classList.remove("header-shadow");
});

const toggleButton = document.querySelector(".dark-light");

toggleButton.addEventListener("click", () => {
 document.body.classList.toggle("dark-mode");
});

const jobCards = document.querySelectorAll(".job-card");
const logo = document.querySelector(".logo");
const jobLogos = document.querySelector(".job-logos");
const jobDetailTitle = document.querySelector(
 ".job-explain-content .job-card-title"
);
// const jobCardsContainer = document.querySelector(".job-cards");
// const jobOverviews = document.querySelectorAll(".job-overview");
// const jobBg = document.querySelector(".job-bg");

// jobCards.forEach((jobCard) => {
//  jobCard.addEventListener("click", () => {
// //   const number = Math.floor(Math.random() * 10);
// //   const url = `https://unsplash.it/640/425?image=${number}`;
// //   jobBg.src = url;

//   const logo = jobCard.querySelector("img");
//   const bg = logo.style.backgroundColor;
//   console.log(bg);
// //   jobBg.style.background = bg;
// // document.querySelectorAll(".job-overview").forEach((overview) => {
// //   overview.style.display = "none";
// // });
// // const jobDetail = jobCard.closest(".job-overview");
    
// // if (jobDetail) {
// //   jobDetail.style.display = "flex"; // Show only this job
// // }
//   const title = jobCard.querySelector(".job-card-title");
//   jobDetailTitle.textContent = title.textContent;
//   jobLogos.innerHTML = logo.outerHTML;
//   jobCardsContainer.style.display = "none";

//     // Show the job overview
//     jobOverview.style.display = "flex";
//   // wrapper.classList.add("detail-page");
//   // wrapper.scrollTop = 0;
//  });
// });

// jobCards.forEach((jobCard, index) => {
//   jobCard.addEventListener("click", () => {
//     // Hide all job cards
//     jobCardsContainer.style.display = "none";

//     // Hide all job overview sections first
//     jobOverviews.forEach((overview) => {
//       overview.style.display = "none";
//     });

//     // Get the related job overview (assuming there's a corresponding one)
//     const jobOverview = jobOverviews[index]; // Matching by index

//     if (jobOverview) {
//       jobOverview.style.display = "flex"; // Show the clicked job's overview
//     }

//     // Update job details
//     const logo = jobCard.querySelector("img");
//     const title = jobCard.querySelector(".job-card-title");
    
//     jobDetailTitle.textContent = title.textContent;
//     jobLogos.innerHTML = logo.outerHTML;
//   });
// });



const jobOverviews = document.querySelectorAll(".job-explain-content");
const jobCardsContainer = document.querySelector(".job-cards");

// Hide all job overviews initially
jobOverviews.forEach((overview) => {
  overview.style.display = "none";
});

jobCards.forEach((jobCard, index) => {
  jobCard.addEventListener("click", () => {
    // Hide all job cards
    jobCardsContainer.style.display = "none";

    // Hide all job overviews first
    jobOverviews.forEach((overview) => {
      overview.style.display = "none";
    });

    // Show only the clicked job's overview
    if (jobOverviews[index]) {
      jobOverviews[index].style.display = "flex"; // Adjust if needed
    }
  });
});



logo.addEventListener("click", () => {
 wrapper.classList.remove("detail-page");
 wrapper.scrollTop = 0;
   jobBg.style.background = bg;
});
