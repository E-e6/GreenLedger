let credits = 0;
function addPoints() {
  credits += Math.floor(Math.random()*10)+5;
  document.getElementById("credits").innerText = credits;
  updateLeaderboard();
}
function updateLeaderboard() {
  const leaderboard = document.getElementById("leaderboard");
  leaderboard.innerHTML = `<li>You – ${credits}</li><li>Alice – 25</li><li>Bob – 20</li>`;
}
