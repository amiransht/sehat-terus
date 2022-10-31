$(document).ready(function () {
  $.get("/faq-page/getblog", function (data) {
    for (i = 0; i < data.length; i++) {
      $(".cardblog").append(`
        <div class="card col-lg-1 col-md-1 col-sm-1" style="width: 50rem;">
          <div class="card-body">
            <h5 class="card-title my-2">${data[i].fields.title}</h5>
            <p class="card-text my-2">${data[i].fields.content}</p>
          </div>
        </div>`)
    }
  })
})