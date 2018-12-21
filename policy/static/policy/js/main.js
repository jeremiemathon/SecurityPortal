$("#id_section").change(function () {
  var url = $("#ruleForm").attr("data-subsections-url");  // get the url of the `load_cities` view
  var subsectionId = $(this).val();  // get the selected country ID from the HTML input

  $.ajax({                       // initialize an AJAX request
    url: url,                    // set the url of the request (= localhost:8000/hr/ajax/load-cities/)
    data: {
      'subsection': subsectionId       // add the country id to the GET parameters
    },
    success: function (data) {   // `data` is the return of the `load_cities` view function
      $("#id_subsection").html(data);  // replace the contents of the city input with the data that came from the server
    }
  });
});