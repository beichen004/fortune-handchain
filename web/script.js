document.addEventListener("DOMContentLoaded", () => {
  const urlParams = new URLSearchParams(window.location.search);
  const sign = urlParams.get("sign") || "aries";
  const day = urlParams.get("day") || "today";

  document.getElementById("sign").textContent = sign;
  document.getElementById("day").textContent = day;

  const apiUrl = `https://fortune-handchain-api-git-main-feifeizhengs-projects.vercel.app/api/fortune/daily/${sign}/${day}`;

  fetch(apiUrl)
    .then(r => {
      if (!r.ok) throw new Error(`HTTP ${r.status}`);
      return r.json();
    })
    .then(data => {
      document.getElementById("fortune").textContent = data.fortune;
    })
    .catch(err => {
      console.error(err);
      document.getElementById("fortune").textContent = "加载失败: " + err.message;
    });
});
