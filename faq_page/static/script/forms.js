$(document).ready(function(){
    $("#add-blog").click(function(a){
    const result = $.post("/faq-page/submit_blog", {
      title: $('#id_title').val(),
      content: $('#id_content').val()}, 
      )
      a.preventDefault()
    window.location = '/faq-page/blog'
})
})