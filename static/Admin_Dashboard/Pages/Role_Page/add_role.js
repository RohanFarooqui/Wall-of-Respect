$(document).ready(function() {
    //---------------------------------------------------------> This Js run when adding role <---------------------------------------------------------\\
    $('#btn_add_role').click(function(){
        //-> Restrict Check Box
        user_page = document.getElementById("user_page");
        add_user  = document.getElementById("add_user");
        edit_user = document.getElementById("edit_user");

        user_page.addEventListener('change', function(e) {
                var check_box_value = user_page.checked;

                if(check_box_value == true){
                    add_user.disabled  = false;
                    edit_user.disabled = false;
                }
                else if(check_box_value == false){
                    add_user.disabled  = true;
                    edit_user.disabled = true;
                    add_user.checked   = false;
                    edit_user.checked  = false;
                }
                
        });

        role_page = document.getElementById("role_page");
        add_role  = document.getElementById("add_role");
        edit_role = document.getElementById("edit_role");

        role_page.addEventListener('change', function(e) {
            var check_box_value = role_page.checked;

            if(check_box_value == true){
                add_role.disabled  = false;
                edit_role.disabled = false;
            }
            else if(check_box_value == false){
                add_role.disabled  = true;
                edit_role.disabled = true;
                add_role.checked   = false;
                edit_role.checked  = false;
            }
                
        });


        assc_page = document.getElementById("assc_page");
        add_assc  = document.getElementById("add_assc");
        edit_assc = document.getElementById("edit_assc");

        assc_page.addEventListener('change', function(e) {
            var check_box_value = assc_page.checked;

            if(check_box_value == true){
                add_assc.disabled  = false;
                edit_assc.disabled = false;
            }
            else if(check_box_value == false){
                add_assc.disabled  = true;
                edit_assc.disabled = true;
                add_assc.checked   = false;
                edit_assc.checked  = false;
            }
                
        });


        camp_page = document.getElementById("camp_page");
        add_camp  = document.getElementById("add_camp");
        edit_camp = document.getElementById("edit_camp");

        camp_page.addEventListener('change', function(e) {
            var check_box_value = camp_page.checked;

            if(check_box_value == true){
                add_camp.disabled  = false;
                edit_camp.disabled = false;
            }
            else if(check_box_value == false){
                add_camp.disabled  = true;
                edit_camp.disabled = true;
                add_camp.checked   = false;
                edit_camp.checked  = false;
            }
                
        });

    });

    //---------------------------------------------------------> This Js run when editing role <---------------------------------------------------------\\

    u_user_page =  document.getElementById("update_user_page");
    add_user    = document.getElementById("update_add_user");
    edit_user   = document.getElementById("update_edit_user");

    u_user_page.addEventListener('change', function(e) {
        var check_box_value = u_user_page.checked;

        if(check_box_value == true){
            add_user.disabled  = false;
            edit_user.disabled = false;
        }
        else if(check_box_value == false){
            add_user.disabled  = true;
            edit_user.disabled = true;
            add_user.checked   = false;
            edit_user.checked  = false;
        }     
    });

    u_role_page = document.getElementById("update_role_page");
    add_role  = document.getElementById("update_add_role");
    edit_role = document.getElementById("update_edit_role");

    u_role_page.addEventListener('change', function(e) {
        var check_box_value = u_role_page.checked;

        if(check_box_value == true){
            add_role.disabled  = false;
            edit_role.disabled = false;
        }
        else if(check_box_value == false){
            add_role.disabled  = true;
            edit_role.disabled = true;
            add_role.checked   = false;
            edit_role.checked  = false;
        }       
    });


    u_assc_page = document.getElementById("update_assc_page");
    add_assc  = document.getElementById("update_add_assc");
    edit_assc = document.getElementById("update_edit_assc");

    u_assc_page.addEventListener('change', function(e) {
        var check_box_value = u_assc_page.checked;
        console.log(check_box_value);

        if(check_box_value == true){
            add_assc.disabled  = false;
            edit_assc.disabled = false;
        }
        else if(check_box_value == false){
            add_assc.disabled  = true;
            edit_assc.disabled = true;
            add_assc.checked   = false;
            edit_assc.checked  = false;
        }     
    });


    u_camp_page = document.getElementById("update_camp_page");
    add_camp  = document.getElementById("update_add_camp");
    edit_camp = document.getElementById("update_edit_camp");

    u_camp_page.addEventListener('change', function(e) {
        var check_box_value = u_camp_page.checked;

        if(check_box_value == true){
            add_camp.disabled  = false;
            edit_camp.disabled = false;
        }
        else if(check_box_value == false){
            add_camp.disabled  = true;
            edit_camp.disabled = true;
            add_camp.checked   = false;
            edit_camp.checked  = false;
        }      
    });

    
});




