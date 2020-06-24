$(document).ready(function () {
    $($('.carousel-item')[0]).addClass("active")
    $("form").submit(function () {
        console.log($(".form-control").val())
        return false
    })
})