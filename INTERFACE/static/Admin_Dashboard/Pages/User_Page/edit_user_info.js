$(document).ready(function() {
    $('#edit_user_info').on('show.bs.modal', function(e) {

	var _button = $(e.relatedTarget);
	var $row = $(_button).closest("tr");

	//-> Get Other Forms Field Values
	var form_field_values = $row.find("td").map(function(){ 
		return $(this).text();}).get();
	//-> Get Image Path
	var image_path = $row.find("td").find('img:first').attr('src');
   
	var x      = form_field_values[1].trim().split("\n");
	var name   = x[0].trim();
	var u_name = form_field_values[2].trim();

	var email  = form_field_values[3].trim();
	var pswd   = form_field_values[4].trim();
	var role   = x[1].trim();
	var status = form_field_values[9].trim();

	
	//-> Show Image Default	
	$("#update_img").val(image_path);
	//-> Show Associate ID 
    $("#user_id").val(form_field_values[0]);
	//-> Show Name
	$('#update_name').val(name);
	//-> Show U_name 
	$('#update_u_name').val(u_name);
	//-> Show Email 
	$('#update_email').val(email);
	//-> Show Password
	//$('#update_pswd').val(pswd);
	//-> Show Role
	$("select option").filter(function() {
		return $(this).text() == role;
	}).attr('selected', true);
	//-> Show Status 
	$("select option").filter(function() {
		return $(this).text() == status;
	}).attr('selected', true);

    });
  });





