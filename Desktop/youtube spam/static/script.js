document.addEventListener("DOMContentLoaded", function () {
    document.getElementById("spamForm").addEventListener("submit", async function (e) {
      e.preventDefault(); // Prevent default form submission
  
      const comment = document.getElementById("commentInput").value; // Get the comment from input field
  
      if (comment.trim() === "") {
        alert("Please enter a comment");
        return;
      }
  
      // Send POST request to Flask backend
      const response = await fetch('/predict', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ comment }),
      });
  
      const result = await response.json(); // Get the result from the response
      document.getElementById("result").innerText = "" + result.result; // Show result on the page
      document.getElementById("result").style.display = "block"; // Make sure it's visible
    });

    function openForm() {
      document.getElementById("form-container").style.display = "block";
      document.getElementById("typing-header").classList.add("hide-typing");
    }
    
    function closeForm() {
      document.getElementById("form-container").style.display = "none";
      document.getElementById("typing-header").classList.remove("hide-typing");
    }
    
  });
  