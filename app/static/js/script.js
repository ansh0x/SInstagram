function likePost(postId) {
    fetch('/like-post', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ postId : postId}),
    })

    .then(respone => respone.json())
    .then(data => {
        document.getElementById(`like-count-${postId}`).innerText = data.total_likes;
    })

    let likeBtn = document.getElementById('like-btn')
    if (likeBtn.classList.contains('bxs-heart'))    {
        likeBtn.classList.remove('bxs-heart')
        likeBtn.classList.add('bx-heart')
    }
    else { 
        likeBtn.classList.remove('bx-heart')
        likeBtn.classList.add('bxs-heart')
    }
}