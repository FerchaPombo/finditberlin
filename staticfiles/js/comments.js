document.addEventListener("DOMContentLoaded", function(event) { 
    const deleteModal = new bootstrap.Modal(document.getElementById("deleteModal"));
    const editModal = new bootstrap.Modal(document.getElementById("editModal"));
    const deleteButtons = document.getElementsByClassName("btn-delete");
    const editButtons = document.getElementsByClassName("btn-edit");
    const deleteConfirm = document.getElementById("deleteConfirm");
    const commentText = document.getElementsByTagName("textarea")[0];
    const commentForm = document.getElementById("CommentsForm");
    const submitButton = document.getElementById("submitButton");


    // empty the comment text after post

    commentText.value = "";

    for (let button of deleteButtons) {
        button.addEventListener("click", (e) => {
            let commentId = e.target.getAttribute("comment_id");
            deleteConfirm.href = `delete_comment/${commentId}`;
            deleteModal.show();
        });
    }

    for (let button of editButtons) {
        button.addEventListener("click", (e) => {
            let commentId = e.target.getAttribute("comment_id");
            let commentContent = document.getElementById(`comment${commentId}`).innerText;
            commentText.value = commentContent;
            editModal.show(); //show the edit modal
            commentText.setAttribute("data-comment-id", commentId);

            
        });
    }
})

//form submission for the edit modal 

const editForm = document.getElementById("editForm");
editForm.addEventListener("submit", function(e){
    e.preventDefault(); //Prevents default form submission 
    const commentId = commentText.getAttribute("data-comment-id");
    const editedComment = commentText.value;
    //ajax request using fetch 
    fetch(`/edit_comment/&{commentId}`, {
        method: 'POST',
        headers: {
            'Content-Type':'application/json',
            'X-CSRFToken': getcookie('csrftoken'), //define get cookie function under

        },
        body: JSON.stringify({comment: editedComment}),
    })
    .then(response => {
        if (response.ok) {
            // update the comment content on the page 
            document.getElementById('comment${commentID}').innerText = editedComment;
            //Close the edit modal
            editModal.hide();

        }
        else {
            console.error('error updating comment', response.statusText);
        }

    })
    .catch(error => {
        console.error('Error updating comment', error);
    });

});

// Function to get the CSRF token from cokkies
function getcookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.startsWith(name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue
}

