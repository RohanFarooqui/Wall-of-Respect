import json

def get_role_list(user_list,assc_list,role_list,camp_list):
    default_dic = {'add_user':'No','edit_user':'No','user_page':'No','add_role':'No','edit_role':'No','role_page':'No','add_assc':'No','edit_assc':'No','assc_page':'No','add_camp':'No','edit_camp':'No','camp_page':'No'}

    complete_list = user_list + role_list + assc_list + camp_list

    for i in default_dic:
        if i in complete_list:
            default_dic[i] = "Yes"

    user_access_dic = json.dumps(default_dic)

    return user_access_dic