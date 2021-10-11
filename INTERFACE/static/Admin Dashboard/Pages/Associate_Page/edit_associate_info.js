 $(document).ready(function() {
    $('#edit_associate_info').on('show.bs.modal', function(e) {

	var _button = $(e.relatedTarget);
	var $row = $(_button).closest("tr");

	//-> Get Other Forms Field Values
	var form_field_values = $row.find("td").map(function(){ return $(this).text();}).get();
	//-> Get Image Path
	var image_path = $row.find("td").find('img:first').attr('src');

	var x       = form_field_values[1].trim().split("\n");
	var name    = x[0].trim();
	var design  = x[1].trim();
	var camp    = form_field_values[4].trim();
	var status  = form_field_values[9].trim();
	var descrip = form_field_values[2].trim();
	var quote   = form_field_values[3].trim();

	console.log(design);
	
	//-> Show Image Default	
	$("#update_img").val(image_path);
	//-> Show Associate ID 
    $("#assc_id").val(form_field_values[0]);
	//-> Show First Name
	$('#update_name').val(name);
	//-> Show Designation
	$('#update_desig').val(design);
	//-> Show Drop Down Value for Campaign
	$("select option:contains("+camp+")").attr('selected', true);
	//-> Show Drop Down Value for Status
	$("select option").filter(function() {
		return $(this).text() == status;
	}).attr('selected', true);
	//-> Show Description
	$('#update_descrip').val(descrip);
	//-> Show Quote
	$('#update_quote').val(quote);


    });
  });





