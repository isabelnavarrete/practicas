     $(".room_gallery").owlCarousel({
    loop: true,
    nav: true,
    dots: false,
    items: 1,
    navText: ['<i class="fal fa-long-arrow-left"></i>', '<i class="fal fa-long-arrow-right"></i>'],
    autoplay: false,
});

$(function() {
    let text_wrapper = $(".room .room_content .text"),
        see_more = $(".room .room_content .see_more");

    text_wrapper.each(function () {
         let lines = $(this).html().replace("<br>", "\n").split("\n");
         if (lines.length >= 5 ) {
             $(this).closest(".room_content").find(".see_more").addClass("visible");
         }
    });
    see_more.on("click", function () {
       $(this).closest(".room_content").find(".text").toggleClass("exceded");
       $(this).closest(".room_content").toggleClass("exceded");
       $(this).toggleClass("toggled");
    });
});