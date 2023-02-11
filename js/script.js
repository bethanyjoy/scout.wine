// quick search regex
var qsRegex;
var buttonFilter;
var filterValue;
var $selects = $('#checkbox-filter select');
var $checkboxes = $('#checkbox-filter input');
var filterCheckbox;
var clearAll= $('.clear-all');
var resetFilter;
var selections;

// init Isotope

selections = function() {
    var $this = $(this);
    var searchResult = qsRegex ? $this.text().match( qsRegex ) : true;
    var buttonResult = buttonFilter ? $this.is( buttonFilter ) : true;
    var selectResult = filterValue ? $this.is(filterValue) : true;
    var checkboxResult = filterCheckbox ? $this.is(filterCheckbox) : true;
    var resetResult = resetFilter ? $this.is(resetFilter) : true;


    return searchResult && buttonResult && selectResult && checkboxResult && resetResult;

  }


  // Render the wine data from the JSON file into grid html

  $(function a() {

    var wine = [];

    $.getJSON('data.json', function(data) {

      $.each(data.wine, function(i, f) {

        var tblRow =
        "<article class=" + "'" + f.Type + " " + f.Title + " " + f.Store + "'" + " data-type=" + f.Type + " data-store=" + f.Store + ">" +
          "<a href=" + f.Link + ">" +
            "<img src=" + f.Image + ">" +
          "</a>" +
          "<div class='tag'>" + f.Type_text + "</div>" +
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

      $(document).trigger('json_loaded');

    });

  });



  function b() {


    // Initialize isotope
    var $grid = $('#grid').isotope({
      itemSelector: 'article',
      filter: selections,
    });



    // Checkbox filter
    $selects.add( $checkboxes ).change( function() {
      var exclusives = [];
      var inclusives = [];
      $selects.each( function( i, elem ) {
        if ( elem.value ) {
          exclusives.push( elem.value );
        }
      });
      $checkboxes.each( function( i, elem ) {
        if ( elem.checked ) {
          inclusives.push( elem.value );
        }
      });
      exclusives = exclusives.join('');
      if ( inclusives.length ) {
        filterCheckbox = $.map( inclusives, function( value ) {
          return value + exclusives;
        });
        filterCheckbox = filterCheckbox.join(', ');
      } else {
        filterCheckbox = exclusives;
      }
      $grid.isotope();
      //console.log(filterCheckbox);
    });

    $('label').click(function(){
      console.log(filterCheckbox);
    });




    // Dropdown filter
    $("#dropdown-filter").on("change", function() {
      // get filter value from option value
      filterValue = $(this).val();
      console.log(filterValue);
      $grid.isotope();
    });

    // Button filter
    $('#button-filter').on( 'click', 'button', function() {
      buttonFilter = $( this ).attr('data-filter');
      console.log(buttonFilter);
      $grid.isotope();
    });

    // use value of search field to filter
    var $quicksearch = $('#quicksearch').keyup( debounce( function() {
      qsRegex = new RegExp( $quicksearch.val(), 'gi' );
      $grid.isotope();
    }) );


      // change is-checked class on buttons
    $('.button-group').each( function( i, buttonGroup ) {
      var $buttonGroup = $( buttonGroup );
      $buttonGroup.on( 'click', 'button', function() {
        $buttonGroup.find('.is-checked').removeClass('is-checked');
        $( this ).addClass('is-checked');
      });
    });

    clearAll.on( 'click', function() {
        buttonFilter = '*';
        filterValue = '*';
        filterCheckbox = '*';
        qsRegex = '';
        $('#quicksearch').val('');
        $('input:checkbox').removeAttr('checked');
        $('#dropdown-filter').prop('selectedIndex',0);
        $('.button-group').each( function() {
           $(this).find('.is-checked').removeClass('is-checked');
        });

        $grid.isotope();

    });

    // debounce so filtering doesn't happen every millisecond
    function debounce( fn, threshold ) {
      var timeout;
      return function debounced() {
        if ( timeout ) {
          clearTimeout( timeout );
        }
        function delayed() {
          fn();
          timeout = null;
        }
        setTimeout( delayed, threshold || 100 );
      };
    }

  }





// Set isotope function to run after json function has completed runnning

$(document).bind('json_loaded', b);





// Hide/show sidebar on mobile

  function showSidebar() {
    var x = document.getElementById("filters");
      x.style.display = "flex";
    var x = document.getElementById("showButton");
      x.style.display = "none";
    var x = document.getElementById("hideButton");
      x.style.display = "block";
    var x = document.getElementById("sidebar");
      x.style.height = "100vh";
    var x = document.getElementById("main");
      x.style.overflow = "hidden"
  }

  function hideSidebar() {
    var x = document.getElementById("filters");
      x.style.display = "none";
    var x = document.getElementById("showButton");
      x.style.display = "block";
    var x = document.getElementById("hideButton");
      x.style.display = "none";
      var x = document.getElementById("sidebar");
        x.style.height = "auto";
    var x = document.getElementById("main");
        x.style.overflow = "auto"
    }
