function decodeHtml(html) {
    var txt = document.createElement("textarea");
    txt.innerHTML = html.replace(/&#(\d+);/g, function(match, dec) {
        return String.fromCharCode(dec);
    });
    return txt.value;
    }
// Replace YOUR_WORDPRESS_SITE_URL with the URL of your WordPress site
const urlA = 'https://boejaker.com/wp-json/wp/v2/posts?per_page=5';
const urlB = 'https://maxhodl.com/wp-json/wp/v2/posts?per_page=5';
fetch(urlA)
    .then(response => response.json())
    .then(posts => {
        // Replace "recent-posts" with the ID or class of the element where you want to display the posts
        const recentPostsContainer = document.getElementById("boejaker-recent-posts");

        // Loop through the posts and create HTML elements to display them
        posts.forEach(post => {
        const postLink = document.createElement("a");
        postLink.href = post.link;
        postLink.textContent = decodeHtml(post.title.rendered);

        const postImage = document.createElement("img");
        postImage.src = post.featured_media.source_url;
        postImage.alt = post.title.rendered;

        const postSummary = document.createElement("p");
        postSummary.textContent = decodeHtml(post.excerpt.rendered)
            .replace(/<\/?[^>]+(>|$)/g, '')
            .replace('[&hellip;]', '. . .');

        const listItem = document.createElement("li");
        // listItem.appendChild(postImage);
        listItem.appendChild(postLink);
        listItem.appendChild(postSummary);

        recentPostsContainer.appendChild(listItem);
        });
    })
.catch(error => console.error(error));
fetch(urlB)
    .then(response => response.json())
    .then(posts => {
        // Replace "recent-posts" with the ID or class of the element where you want to display the posts
        const recentPostsContainer = document.getElementById("maxhodl-recent-posts");

        // Loop through the posts and create HTML elements to display them
        posts.forEach(post => {
        const postLink = document.createElement("a");
        postLink.href = post.link;
        postLink.textContent = decodeHtml(post.title.rendered);

        const postImage = document.createElement("img");
        postImage.src = post.featured_media.source_url;
        postImage.alt = post.title.rendered;

        const postSummary = document.createElement("p");
        postSummary.textContent = decodeHtml(post.excerpt.rendered)
            .replace(/<\/?[^>]+(>|$)/g, '')
            .replace('[&hellip;]', '. . .');

        const listItem = document.createElement("li");
        // listItem.appendChild(postImage);
        listItem.appendChild(postLink);
        listItem.appendChild(postSummary);

        recentPostsContainer.appendChild(listItem);
        });
    })
.catch(error => console.error(error));