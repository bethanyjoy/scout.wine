


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

  // var $grid = $('#grid').imagesLoaded( function() {
  //   // init Isotope after all images have loaded
  //   $grid.isotope({
  //     itemSelector: 'article',
  //     filter: selections,
  //   });
  // });




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

      // var $grid = $('#grid').isotope({
      //   itemSelector: 'article',
      //   filter: selections,
      // });

    });


  });



  function b() {


    var $grid = $('#grid').isotope({
      itemSelector: 'article',
      filter: selections,
    });

    // layout Isotope after each image loads
    // $grid.imagesLoaded().progress( function() {
    //   $grid.isotope('layout');
    // });


    // CHECKBOXES
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


    // DROPDOWN
    $("#dropdown-filter").on("change", function() {
      // get filter value from option value
      filterValue = $(this).val();
      console.log(filterValue);
      $grid.isotope();
    });

    // BBUTTONS
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






$(document).bind('json_loaded', b);
