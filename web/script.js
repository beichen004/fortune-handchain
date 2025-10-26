document.addEventListener("DOMContentLoaded", () => {
  const urlParams = new URLSearchParams(window.location.search);
  const sign = urlParams.get("sign") || "aries";
  const day = urlParams.get("day") || "today";

  document.getElementById("sign").textContent = sign;
  document.getElementById("day").textContent = day;

  const apiUrl = "https://fortune-handchain-api.vercel.app/api/fortune/daily/" + sign + "/" + day;

  fetch(apiUrl, { mode: 'cors' })
    .then(response => {
      if (!response.ok) throw new Error(`HTTP error! Status: ${response.status}`);
      return response.json();
    })
    .then(data => {
      document.getElementById("fortune").textContent = data.fortune;
    })
    .catch(error => {
      console.error("Fetch error:", error);
      document.getElementById("fortune").textContent = "Failed to load: " + error.message;
    });
});
