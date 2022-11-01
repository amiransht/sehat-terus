$(document).ready(function(){
    // Prepare the preview for profile picture
    document.getElementById("profpic").addEventListener("change", function(){
        var reader = new FileReader();
        reader.onload = function(){
            var output = document.getElementById('profpicPreview');
            output.src = reader.result;
        };
        reader.readAsDataURL(event.target.files[0]);
    });
});