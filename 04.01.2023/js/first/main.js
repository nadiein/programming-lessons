/*
    You would like to add the ability to render comments on a previously static website. The comments are submitted only via a mobile app, so the website itself just needs to display the latest comments. Comments should be fetched on the client (browser) side and then displayed inside all tags that have the class comment-list  (there can be more than one such tag). All of these elements will have a data-count  attribute determining the number of comments to fetch.
    Here's an example of such a tag:
    <div class="comment-list" data-count=10></div>
    The comment data for this tag can be obtained by making an AJAX call to the following mocked endpoint:
    https://www.example.com/comments?count=10
    While the comments are being loaded, the comment-list  elements should be filled with the text Loading...
    Please use only textContent  for setting the text content of the elements.
    The DOM structure of each comment is expected to be:
    <div class="comment-item">
    <div class="comment-item__username">{username}</div>
    <div class="comment-item__message">{message}</div>
    </div>

    Write a function: function solution();
    that, given a DOM tree representing an HTML document, renders comments as described above.
    use fetch api
*/

function solution() {
    const commentsList = document.querySelectorAll('.comment-list');

    commentsList.forEach(commentList => {
        const savedState = commentList.textContent;
        const count = commentList.dataset.count;

        commentList.textContent = 'Loading...';

        fetch(`https://www.example.com/comments?count=${count}`)
        .then(res => res.json())
        .then(comments => {
            commentList.textContent = '';

            comments.forEach(comment => {
            const commentItem = document.createElement('div');
            commentItem.classList.add('comment-item');

            const username = document.createElement('div');
            username.classList.add('comment-item__username');
            username.textContent = comment.username;

            const message = document.createElement('div');
            message.classList.add('comment-item__message');
            message.textContent = comment.message;

            commentItem.appendChild(username);
            commentItem.appendChild(message);

            commentList.appendChild(commentItem);
            });
        })
        .catch(error => {
            commentList.textContent = savedState;
        });
    });
}
