
// Render the wine data from the JSON file into grid html

$(function a() {

	var wine = [];

	$.getJSON('data.json', function(data) {

		$.each(data.wine, function(i, f) {

			var tblRow =
			// "<article>" +
			"<article class=" + "'" + f.Type_class + " " + f.Store_class + " " + f.Maker_class + "'>" +
				"<a class=" + f.Image_type + " href=" + f.Link + ">" +
					"<div class='type'>" + f.Type + "</div>" +
					"<img class='photo' src=" + f.Image + ">" +
					// "<svg width='230' height='800' viewBox='0 0 230 800' xmlns='http://www.w3.org/2000/svg'>" +
					//   "<path d='M228.108 487.522C228.108 443.202 218.679 399.829 203.602 358.336C195.12 334.762 184.751 312.129 176.269 288.554C162.132 249.891 154.59 209.347 152.703 166.914C152.703 159.37 152.703 151.825 151.763 143.34V144.281C150.823 122.594 150.823 100.901 150.823 80.162V56.5877V53.7593C150.823 49.9903 152.71 47.1553 153.65 43.3863C153.65 41.4985 154.59 40.5579 154.59 38.6701V24.5282C154.59 21.6998 152.703 18.8714 151.763 15.0958C150.823 13.208 150.823 10.3796 150.823 8.4918C150.823 4.72277 148.936 2.83498 146.108 1.8878C142.341 0.947201 136.679 0 132.912 0H94.2624C90.4947 0 87.6608 0.9406 83.8931 1.8878C80.1255 2.8284 78.2384 4.71621 79.1787 8.4918C79.1787 10.3796 79.1787 13.208 78.2384 15.0958C77.2982 17.9242 76.3513 20.7526 75.411 24.5282V38.6701C75.411 40.5579 76.3513 41.4985 76.3513 43.3863C77.2915 47.1553 79.1787 50.9309 79.1787 54.7C79.1787 84.8784 78.2384 114.109 77.2915 144.281V159.37C76.3513 171.63 75.4045 184.832 74.4642 197.085C68.8094 242.346 56.5526 285.726 37.7017 327.217C12.2491 382.851 0 440.372 0 500.724V716.664C0 733.634 0.940243 750.611 1.8871 767.581C2.82735 781.723 9.42897 789.268 22.6249 792.097C25.4523 793.038 29.2265 793.038 32.0539 793.985C73.5311 799.642 114.061 801.529 155.536 798.701C172.5 797.76 189.471 794.932 206.435 793.044C218.691 791.157 225.286 784.559 227.173 771.358C229.06 760.044 230 748.725 230 737.411C229.047 655.374 229.047 571.449 228.106 487.523L228.108 487.522Z'/>" +
					// "</svg>" +
					"<img class='placeholder' src='assets/placeholder2.png'/>" +
				"</a>" +
				// "<div class='type'>" + f.Type + "</div>" +
				"<div class='text'>" +
					"<a href=" + f.Link + ">" +
						"<p class='name'>" + f.Title + "</p>"+
					"</a>" +
					"<p class='store'>" + f.Store + "</p>" +
					"<p class='price'>" + f.Price + "</p>" +
					"<p class='maker'>" + f.Maker + "</p>" +
					"<p class='region'>" + f.Region + "</p>" +
				"</div>" +
			"</article>"
			$(tblRow).appendTo("#grid");

		});

		$(document).trigger('json_loaded');

	});

});



function b() {

	var options = {
		valueNames: ['type', 'category', 'store', 'name', 'maker', 'region'],
		page: 30,
		innerWindow: 3,
		right: 2,
		plugins: [
			 ListPagination({})
		]
	};

	var userList = new List('body', options);

	var updateList = function () {
		var type = new Array();
		var category = new Array();
		var store = new Array();
		var name = new Array();
		var maker = new Array();
		var region = new Array();

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

		$("input:checkbox[name=region]:checked").each(function () {
			region.push($(this).val());
		});

		var values_category = category.length > 0 ? category : null;
		var values_type = type.length > 0 ? type : null;
		var values_store = store.length > 0 ? store : null;
		var values_name = name.length > 0 ? name : null;
		var values_maker = maker.length > 0 ? maker : null;
		var values_region = region.length > 0 ? region : null;

		userList.filter(function (item) {
			var categoryTest;
			var typeTest;
			var storeTest;
			var nameTest;
			var makerTest;
			var regionTest;

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
					&& (_(values_region).contains(item.values().region) || !values_region)
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
		window.scroll({
			top: 0,
		});
	});

	var all_category = [];
	var all_type = [];
	var all_store = [];
	var all_name = [];
	var all_maker = [];
	var all_region = [];

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
		all_region.push(item.values().region)
	});

	_(all_category).uniq().each(function (item) {
		$(".categoryContainer").append('<label><input type="checkbox" name="category" value="' + item + '">' + item + '<span class="checkmark"></label>')
	});

//		let sort_type = all_type.sort();

	_(all_type).uniq().each(function (item) {
		$(".typeContainer").append('<input type="checkbox" name="type" id="' + item + '" value="' + item + '"><label for="' + item + '">' + item + '</label>')
	});

	let sort_store = all_store.sort();

	_(sort_store).uniq().each(function (item) {
		$(".storeContainer").append('<label><input type="checkbox" name="store" value="' + item + '">' + item + '<span class="checkmark"></label>')
	});

	_(all_name).uniq().each(function (item) {
		$(".nameContainer").append('<label><input type="checkbox" name="name" value="' + item + '">' + item + '<span class="checkmark"></label>')
	});

	let sort_maker = all_maker.sort();

	_(sort_maker).uniq().each(function (item) {
		$(".makerContainer").append('<label class="' + item + '"><input type="checkbox" name="maker" value="' + item + '">' + item + '<span class="checkmark"></label>')
	});

	let sort_region = all_region.sort();

	_(sort_region).uniq().each(function (item) {
		$(".regionContainer").append('<label class="' + item + '"><input type="checkbox" name="region" value="' + item + '">' + item + '<span class="checkmark"></label>')
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
	$(document).off("change", "input:checkbox[name=region]");
	$(document).on("change", "input:checkbox[name=region]", updateList);


}





// Set isotope function to run after json function has completed runnning

$(document).bind('json_loaded', b);
