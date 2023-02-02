// Controls the rendering of the wine data from the JSON file

$(function() {

  var wine = [];

  $.getJSON('data.json', function(data) {

    $.each(data.wine, function(i, f) {

      var tblRow =
      "<article class=" + "'" + f.Type + " " + f.Title + " " + f.Store + "'" + " data-type=" + f.Type + " data-store=" + f.Store + ">" +
        "<a href=" + f.Link + ">" +
          "<img src=" + f.Image + ">" +
        "</a>" +
        "<div class='tag'>" + f.Type_text + "</div>" +
        // "<div class=" + f.Type + "&nbsp;" + "tag>" + f.Type_text + "</div>" +
        "<div class='text'>" +
          "<a href=" + f.Link + ">" +
            "<p class='title'>" + f.Title_text + "</p>"+
          "</a>" +
          "<p class='store'>" + f.Store_text + "</p>" +
          "<p class='price'>" + f.Price + "</p>" +
        "</div>" +
      "</article>"
      $(tblRow).appendTo("#grid");

    });

  });

});




// Controls the search bar functionality



const clearIcon = document.querySelector(".clearIcon");
const searchBar = document.querySelector("#search");

searchBar.addEventListener("keyup", () => {
  if(searchBar.value && clearIcon.style.visibility != "visible"){
    clearIcon.style.visibility = "visible";
  } else if(!searchBar.value) {
    clearIcon.style.visibility = "hidden";
  }
});

clearIcon.addEventListener("click", () => {
  searchBar.value = "";
  clearIcon.style.visibility = "hidden";
})

function myFunction() {

  var input, filter, div, article, p, i, txtValue;
  input = document.getElementById("search");
  filter = input.value.toUpperCase();
  div = document.getElementById("grid");
  article = div.getElementsByTagName("article");

  for (i = 0; i < article.length; i++) {
    p = article[i].getElementsByTagName("p")[0];
    txtValue = p.textContent || p.innerText;
    if (txtValue.toUpperCase().indexOf(filter) > -1) {
      article[i].style.display = "";
    } else {
      article[i].style.display = "none";
    }
  }

}



// Controls the tag filtering functionality


$(document).ready(function () {

  $('.tagFilter :checkbox').click(function () {

    if ($('input:checkbox:checked').length) {
      $('article').hide();
      $('input:checkbox:checked').each(function () {
        $('article[data-' + $(this).prop('name') + '*="' + $(this).val() + '"]').show();
      });
    } else {
      $('article').show();
    }

  });

});



// Controls the string filtering functionality


$(document).ready(function () {

  $('.stringFilter :checkbox').click(function () {

    if ($('input:checkbox:checked').length) {
      $('article').hide();
      $('input:checkbox:checked').each(function () {
        if ($(this).val().contains($(this).prop('name')) {
          $('article[data-' + $(this).prop('name') + ']').show();
        });
      });
    } else {
      $('article').show();
    }

  });

});



// Scroll to the top button


jQuery(document).ready(function() {

  var btn = $('#topButton');

  $(window).scroll(function() {
    if ($(window).scrollTop() > 300) {
      btn.addClass('show');
    } else {
      btn.removeClass('show');
    }
  });

  btn.on('click', function(e) {
    e.preventDefault();
    $('html, body').animate({scrollTop:0}, '300');
  });

});



// Hide/show sidebar on mobile

/* Toggle between showing and hiding the navigation menu links when the user clicks on the hamburger menu / bar icon */

function showSidebar() {
  var x = document.getElementById("sidebar");
    x.style.display = "block";
  var body = document.getElementById("mainContent");
    body.style.overflow = "hidden"
}

function hideSidebar() {
  var x = document.getElementById("sidebar");
    x.style.display = "none";
    var body = document.getElementById("mainContent");
      body.style.overflow = "auto"
}
