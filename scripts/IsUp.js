function is_wp_up(siteUrl, statusElementId) {
    const postsEndpoint = '/wp-json/wp/v2/posts';
    // Make a GET request to the WordPress REST API to retrieve the latest posts
    fetch(`${siteUrl}${postsEndpoint}`)
        .then(response => {
            if (response.ok) {
                // If the response is successful, update the status element to show a green tick
                document.getElementById(statusElementId).innerHTML = `<span style="color:#25633a;">&#10004; Online</span> `;
            } else {
                // If the response is not successful, update the status element to show a red cross
                document.getElementById(statusElementId).innerHTML = `<span style="color::#88263b;">&#10060; Offline</span>`;
            }
        })
        .catch(error => {
            // If there is an error, update the status element to show a red cross
            document.getElementById(statusElementId).innerHTML = `<span style="color:#88263b;">&#10060; Offline</span>`;
        });
}