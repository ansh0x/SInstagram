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

    let likeBtn = document.getElementById(`like-btn-${postId}`)
    if (likeBtn.classList.contains('active-like'))    {
        likeBtn.classList.remove('bxs-heart')
        likeBtn.classList.remove('active-like')
        likeBtn.classList.add('bx-heart')
    }
    else { 
        likeBtn.classList.remove('bx-heart')
        likeBtn.classList.add('bxs-heart')
        likeBtn.classList.add('active-like')
    }
}

function deletePost(postId) {
    fetch('delete-post', {
        method : 'POST',
        headers : {
            'Content-Type' : 'application/json'
        },
        body : JSON.stringify({ postId : postId })
    })
}

function fullPost(postId) {
    var overlayId = 'post-overlay-' + postId;
    var popupId = 'popUp-post-' + postId;

    document.getElementById(overlayId).style.display = 'block';
    document.getElementById(popupId).style.display = 'block';
}

function closePopUp(postId) {
    var overlayId = 'post-overlay-' + postId;
    var popupId = 'popUp-post-' + postId;

    document.getElementById(overlayId).style.display = 'none';
    document.getElementById(popupId).style.display = 'none';
}

var overlays = document.querySelectorAll('.post-overlay');
overlays.forEach(function(overlay) {
    overlay.addEventListener('click', function() {
        var postId = overlay.id.split('-')[2];
        closePopUp(postId);
    });
});