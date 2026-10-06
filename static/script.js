const posts = [
  {
    id: "simple-ui",
    title: "چطور یک رابط کاربری ساده طراحی کنیم؟",
    summary: "چند اصل کاربردی برای ساخت رابط‌هایی خلوت، خوانا و قابل استفاده.",
    category: "طراحی",
    tags: ["مینیمال", "رابط کاربری"],
    date: "۲۸ مرداد ۱۴۰۳",
  },
  {
    id: "javascript",
    title: "شروع کار با جاوااسکریپت مدرن",
    summary: "مروری کوتاه بر مفاهیم پایه‌ای که برای شروع توسعه وب نیاز دارید.",
    category: "توسعه وب",
    tags: ["JavaScript", "برنامه‌نویسی"],
    date: "۲۱ مرداد ۱۴۰۳",
  },
  {
    id: "performance",
    title: "چرا سرعت سایت مهم است؟",
    summary: "تأثیر عملکرد سایت بر تجربه کاربر و چند راه ساده برای بهبود آن.",
    category: "بهینه‌سازی",
    tags: ["سرعت", "SEO"],
    date: "۱۴ مرداد ۱۴۰۳",
  },
];

const postList = document.querySelector("#post-list");
const searchInput = document.querySelector("#search-input");
const emptyState = document.querySelector("#empty-state");

function renderPosts(items) {
  postList.innerHTML = items
    .map(
      (post) => `
        <article class="post">
          <a class="post-link" href="detail.html" aria-label="${post.title}">
            <h2>${post.title}</h2>
            <p>${post.summary}</p>
          </a>
          <div class="post-meta">
            <span class="category">${post.category}</span>
            <small>${post.date}</small>
            <div class="tags" aria-label="تگ‌های مقاله">
              ${post.tags.map((tag) => `<span class="tag">#${tag}</span>`).join("")}
            </div>
            <button class="wishlist-button" type="button">
              ♡ افزودن
            </button>
          </div>
        </article>
      `,
    )
    .join("");

  emptyState.hidden = items.length > 0;
}

function filterPosts(event) {
  const query = event.target.value.trim().toLocaleLowerCase("fa");
  const filteredPosts = posts.filter((post) =>
    `${post.title} ${post.summary} ${post.category} ${post.tags.join(" ")}`
      .toLocaleLowerCase("fa")
      .includes(query),
  );

  renderPosts(filteredPosts);
}

searchInput.addEventListener("input", filterPosts);
renderPosts(posts);
