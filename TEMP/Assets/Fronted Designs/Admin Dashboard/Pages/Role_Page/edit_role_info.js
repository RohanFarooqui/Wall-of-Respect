$(document).ready(function() {
    //---------------------------------------------------------> Load Values in Form when edit <---------------------------------------------------------\\
    $('#edit_role_info').on('show.bs.modal', function(e) {
        var _button = $(e.relatedTarget);
        var $row = $(_button).closest("tr");

        var form_field_values = $row.find("td").map(function(){ return $(this).text();}).get();

        var role_id    = form_field_values[0].trim();
        var role_name  = form_field_values[1].trim();
        var role_status= form_field_values[7].trim();
        
        var role_access= JSON.parse(form_field_values[2].trim());

        //-> Role ID 
        $('#update_roll_id').val(role_id);
        //-> Role Name 
        $('#update_roll_name').val(role_name);
        //-> Role Status 
        $("select option").filter(function() {
            return $(this).text() == role_status;
        }).attr('selected', true);
        
        
        //-> Check Box User
        if(role_access.user_page == "Yes"){$('#update_user_page')[0].checked = true;}
        else{$('#update_user_page')[0].checked = false;}

        if(role_access.add_user == "Yes"){$('#update_add_user')[0].checked = true; $( "#update_add_user" ).prop( "disabled", false );}
        else{$('#update_add_user')[0].checked = false;$( "#update_add_user" ).prop( "disabled", true );}

        if(role_access.edit_user == "Yes"){$('#update_edit_user')[0].checked = true;$( "#update_edit_user" ).prop( "disabled", false );}
        else{$('#update_edit_user')[0].checked = false;$( "#update_edit_user" ).prop( "disabled", true );}

        //-> Check Box Role
        if(role_access.role_page == "Yes"){ $('#update_role_page')[0].checked = true;}
        else{$('#update_role_page')[0].checked = false;}

        if(role_access.add_role == "Yes"){$('#update_add_role')[0].checked = true;$( "#update_add_role" ).prop( "disabled", false );}
        else{$('#update_add_role')[0].checked = false;$( "#update_add_role" ).prop( "disabled", true );}

        if(role_access.edit_role == "Yes"){$('#update_edit_role')[0].checked = true;$( "#update_edit_role" ).prop( "disabled", false );}
        else{$('#update_edit_role')[0].checked = false;$( "#update_edit_role" ).prop( "disabled", true );}
        
        //-> Check Box Associate
        if(role_access.assc_page == "Yes"){$('#update_assc_page')[0].checked = true;}
        else{$('#update_assc_page')[0].checked = false;}

        if(role_access.add_assc == "Yes"){$('#update_add_assc')[0].checked = true;$( "#update_add_assc" ).prop( "disabled", false );}
        else{$('#update_add_assc')[0].checked = false;$( "#update_add_assc" ).prop( "disabled", true );}

        if(role_access.edit_assc == "Yes"){$('#update_edit_assc')[0].checked = true;$( "#update_edit_assc" ).prop( "disabled", false );}
        else{$('#update_edit_assc')[0].checked = false;$( "#update_edit_assc" ).prop( "disabled", true );}



        //-> Check Box  Campaign
        if(role_access.camp_page == "Yes"){$('#update_camp_page')[0].checked = true;}
        else{$('#update_camp_page')[0].checked = false;} 

        if( role_access.add_camp == "Yes"){$('#update_add_camp')[0].checked = true;$( "#update_add_camp" ).prop( "disabled", false );}
        else{$('#update_add_camp')[0].checked = false;$( "#update_add_camp" ).prop( "disabled", true );}

        if(role_access.edit_camp == "Yes"){$('#update_edit_camp')[0].checked = true;$( "#update_edit_camp" ).prop( "disabled", false );}
        else{$('#update_edit_camp')[0].checked = false;$( "#update_edit_camp" ).prop( "disabled", true );}
	
    });

    
    

});







