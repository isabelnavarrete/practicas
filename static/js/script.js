$(".go").click(function () {
  var maps_from_value = $("#google-maps-from-value").val(),
      mapaUrl = 'https://www.google.com/maps?saddr=@place@&daddr=' + maps_from_value + '&output=embed',
      newurl = mapaUrl.replace("@place@", $(".place").val());

  $(".mapa").attr("src",newurl);
});