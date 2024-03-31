document.addEventListener("DOMContentLoaded", function(event) { 
    const deleteModal = new bootstrap.Modal(document.getElementById("deleteModal"));
    const editModal = new bootstrap.Modal(document.getElementById("editModal"));
    const editButtons = document.getElementsByClassName("btn-edit");
    const deleteButtons = document.getElementsByClassName("btn-delete");
    const deleteConfirm = document.getElementById("deleteConfirm");
    const commentText = document.getElementsByTagName("textarea")[0];
    const commentForm = document.getElementById("commentForm");
    const editCommentForm = document.getElementById("editForm");
    const submitButton = document.getElementById("submitButton");

    // empty the comment text after post

    for (let button of deleteButtons) {
        button.addEventListener("click", (e) => {
            let commentId = e.target.getAttribute("comment_id");
            deleteConfirm.href = `delete_comment/${commentId}`;
            deleteModal.show();
        });
    }


    /**
    * Initializes edit functionality for the provided edit buttons.
    *
    * For each button in the `editButtons` collection:
    * - Retrieves the associated comment's ID upon click.
    * - Fetches the content of the corresponding comment.
    * - Populates the `commentText` input/textarea with the comment's content for editing.
    * - Updates the submit button's text to "Update".
    * - Sets the form's action attribute to the `edit_comment/{commentId}` endpoint.
    */
    for (let button of editButtons) {
      button.addEventListener("click", (e) => {
        let commentId = e.target.getAttribute("comment_id");
        let commentContent = document.getElementById(`comment${commentId}`).innerText;
        commentText.value = commentContent;
        submitButton.innerText = "Update";
        commentForm.setAttribute("action", `edit_comment/${commentId}`);
      });
    }
});

//// form submission for the edit modal
//const editForm = document.getElementById("editForm");
//editForm.addEventListener("submit", function(e) {
//    e.preventDefault(); //Prevents default form submission
//    const commentId = commentText.getAttribute("data-comment-id");
//    const editedComment = commentText.value;
//    //ajax request using fetch
//    fetch(`/edit_comment/${commentId}`, {
//        method: 'POST',
//        headers: {
//            'Content-Type': 'application/json',
//            'X-CSRFToken': getCookie('csrftoken'), //define get cookie function under
//        },
//        body: JSON.stringify({comment: editedComment}),
//    })
//    .then(response => {
//        if (response.ok) {
//            // update the comment content on the page
//            document.getElementById('/comment${commentId}').innerText = editedComment;
//            //Close the edit modal
//            editModal.hide();
//        } else {
//            console.error('error updating comment', response.statusText);
//        }
//    })
//    .catch(error => {
//        console.error('Error updating comment', error);
//    });
//});

// Function to get the CSRF token from cookies
function getCookie(name) {
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
    return cookieValue;
}