$(document).ready(function() {
    $('#edit_campaign_info').on('show.bs.modal', function(e) {

	var _button = $(e.relatedTarget);
	var $row = $(_button).closest("tr");

	//-> Get Other Forms Field Values
	var form_field_values = $row.find("td").map(function(){ return $(this).text();}).get();
	
    var ID = form_field_values[0].trim();
    var Camp_name = form_field_values[1].trim();
    var Status    = form_field_values[6];

	

	//-> Campaign ID 
	$('#update_camp_id').val(ID);
	//-> Campaign Name 
    $("#update_camp_name").val(Camp_name);
	//-> Show Drop Down Value for Status
	var status = Status.trim();
	$("select option").filter(function() {
		return $(this).text() == status;
	}).attr('selected', true);
	
    });
  });





