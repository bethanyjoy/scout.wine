

  // Render the wine data from the JSON file into grid html

  $(function a() {

    var wine = [];

    $.getJSON('data.json', function(data) {

      $.each(data.wine, function(i, f) {

        var tblRow =
        "<article class=" + "'" + f.Type + " " + f.Store + "'" + " data-type=" + f.Type + " data-store=" + f.Store + ">" +
          "<a class='image' href=" + f.Link + ">" +
            "<img src=" + f.Image + ">" +
          "</a>" +
          "<div class='type'>" + f.Type_text + "</div>" +
          "<div class='text'>" +
            "<a href=" + f.Link + ">" +
              "<p class='name'>" + f.Title_text + "</p>"+
            "</a>" +
            "<p class='store'>" + f.Store_text + "</p>" +
            "<p class='price'>" + f.Price + "</p>" +
            "<p class='maker'>" + f.Maker + "</p>" +
          "</div>" +
        "</article>"
        $(tblRow).appendTo("#grid");

      });

      $(document).trigger('json_loaded');

    });

  });



  function b() {

    var options = {
      valueNames: ['type', 'category', 'store', 'name', 'maker'],
      page: 60,
			innerWindow: 3,
			right: 2,
      plugins: [
         ListPagination({})
      ]
    };
    var userList = new List('search-results', options);

    var updateList = function () {
      var type = new Array();
      var category = new Array();
      var store = new Array();
      var name = new Array();
      var maker = new Array();

      $("input:checkbox[name=type]:checked").each(function () {
        type.push($(this).val());
      });

      // $("input:checkbox[name=category]:checked").each(function () {
      //   if($(this).val().indexOf('|') > 0){
      //      var arr = $(this).val().split('|');
      //      var arrayLength = arr.length;
      //      category = category.concat(arr);
      //      console.log('Multiple values:' + arr);
      //   }else{
      //      category.push($(this).val());
      //      console.log('Single values:' + arr);
      //   }
      // });

      $("input:checkbox[name=store]:checked").each(function () {
        store.push($(this).val());
      });

      $("input:checkbox[name=name]:checked").each(function () {
        name.push($(this).val());
      });
      
      $("input:checkbox[name=maker]:checked").each(function () {
        maker.push($(this).val());
      });

      var values_category = category.length > 0 ? category : null;
      var values_type = type.length > 0 ? type : null;
      var values_store = store.length > 0 ? store : null;
      var values_name = name.length > 0 ? name : null;
      var values_maker = maker.length > 0 ? maker : null;

      userList.filter(function (item) {
        var categoryTest;
        var typeTest;
        var storeTest;
        var nameTest;
        var makerTest;

        if(item.values().category.indexOf('|') > 0){
          var categoryArr = item.values().category.split('|');
          for(var i = 0; i < categoryArr.length; i++){
             if(_(values_category).contains(categoryArr[i])){
                categoryTest = true;
             }
          }
        }

        return (_(values_category).contains(item.values().category) || !values_category || categoryTest)
            && (_(values_type).contains(item.values().type) || !values_type)
            && (_(values_store).contains(item.values().store) || !values_store)
            && (_(values_name).contains(item.values().name) || !values_name)
            && (_(values_maker).contains(item.values().maker) || !values_maker)
      });
    }

    userList.on("updated", function () {
      $('.sort').each(function () {
        if ($(this).hasClass("asc")) {
          $(this).find(".fa").addClass("fa-sort-alpha-asc").removeClass("fa-sort-alpha-desc").show();
        } else if ($(this).hasClass("desc")) {
          $(this).find(".fa").addClass("fa-sort-alpha-desc").removeClass("fa-sort-alpha-asc").show();
        } else {
          $(this).find(".fa").hide();
        }
      });
    });

    var all_category = [];
    var all_type = [];
    var all_store = [];
    var all_name = [];
    var all_maker = [];

    updateList();

    _(userList.items).each(function (item) {
      if(item.values().category.indexOf('|') > 0){
        var arr = item.values().category.split('|');
        all_category = all_category.concat(arr);
      }else{
        all_category.push(item.values().category)
      }

      all_type.push(item.values().type)
      all_store.push(item.values().store)
      all_name.push(item.values().name)
      all_maker.push(item.values().maker)
    });

    _(all_category).uniq().each(function (item) {
      $(".categoryContainer").append('<label><input type="checkbox" name="category" value="' + item + '">' + item + '<span class="checkmark"></label>')
    });

    _(all_type).uniq().each(function (item) {
      $(".typeContainer").append('<input type="checkbox" name="type" id="' + item + '" value="' + item + '"><label for="' + item + '">' + item + '</label>')
    });
    
    _(all_store).uniq().each(function (item) {
      $(".storeContainer").append('<label><input type="checkbox" name="store" value="' + item + '">' + item + '<span class="checkmark"></label>')
    });

    _(all_name).uniq().each(function (item) {
      $(".nameContainer").append('<label><input type="checkbox" name="name" value="' + item + '">' + item + '<span class="checkmark"></label>')
    });
    
    _(all_maker).uniq().each(function (item) {
      $(".makerContainer").append('<label class="' + item + '"><input type="checkbox" name="maker" value="' + item + '">' + item + '<span class="checkmark"></label>')
    });

    $(document).off("change", "input:checkbox[name=category]");
    $(document).on("change", "input:checkbox[name=category]", updateList);
    $(document).off("change", "input:checkbox[name=type]");
    $(document).on("change", "input:checkbox[name=type]", updateList);
    $(document).off("change", "input:checkbox[name=store]");
    $(document).on("change", "input:checkbox[name=store]", updateList);
    $(document).off("change", "input:checkbox[name=name]");
    $(document).on("change", "input:checkbox[name=name]", updateList);
    $(document).off("change", "input:checkbox[name=maker]");
    $(document).on("change", "input:checkbox[name=maker]", updateList);


  }





// Set isotope function to run after json function has completed runnning

$(document).bind('json_loaded', b);

