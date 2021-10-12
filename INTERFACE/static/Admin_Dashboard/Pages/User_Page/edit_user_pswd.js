$(document).ready(function() {
    $('#edit_user_pswd').on('show.bs.modal', function(e) {

	var _button = $(e.relatedTarget);
	var $row = $(_button).closest("tr");

	//-> Get Other Forms Field Values
	var form_field_values = $row.find("td").map(function(){ 
		return $(this).text();}).get();

    
        console.log(form_field_values[0]);

	//-> Show User ID
    $("#user_id_for_pswd").val(form_field_values[0]);

    });

  });

