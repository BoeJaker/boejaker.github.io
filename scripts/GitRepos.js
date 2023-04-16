// GitHub username and API endpoint
const username = "boejaker";
const endpoint = `https://api.github.com/users/${username}/repos?per_page=100`;

fetch(endpoint)
  .then(response => response.json())
  .then(data => {
    const tableBody = document.querySelector("#repoTable tbody");
    const reposWithSummary = data.filter(repo => {
        console.log(repo.name)
      return true;
    });
    reposWithSummary.forEach(repo => {
    const summaryUrl = `https://raw.githubusercontent.com/${username}/${repo.name}/master/.summary`;
    fetch(summaryUrl)
      .then(response => {
        if (response.status === 404) {
          throw new Error("Summary file not found");
        }
        return response.text();
      })
      .then(summary => {
        if (summary.trim()) { // Check if summary is not empty
          const readmeUrl = `https://github.com/${username}/${repo.name}/blob/master/README.md`;
          const row = tableBody.insertRow();
          const nameCell = row.insertCell();
          const summaryCell = row.insertCell();
          nameCell.innerHTML = `<h3><a href="https://github.com/${username}/${repo.name}/">${repo.name}</a></h3>`;
          summaryCell.innerHTML = summary;
        }
      })
      .catch(error => console.error(error));
    });
  })
  .catch(error => console.error(error));