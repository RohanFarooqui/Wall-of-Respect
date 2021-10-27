INSERT INTO users (ID, Name, User_name, Img_path, Email, Pswd, Status) VALUES
(1,'Admin','admin' ,'/Media/11-09-2021%2018%2500%20PM-Admin.png','admin@gmail.com','81dc9bdb52d04dc20036dbd8313ed055',True);

INSERT INTO roles (ID, Name, Access_level, Status, Added_at, Added_by, Updated_at, Updated_by) VALUES
(1, 'Admin'            ,'{\"add_user\": \"Yes\", \"edit_user\": \"Yes\", \"user_page\": \"Yes\", \"add_role\": \"Yes\", \"edit_role\": \"Yes\", \"role_page\": \"Yes\", \"add_assc\": \"Yes\", \"edit_assc\": \"Yes\", \"assc_page\": \"Yes\", \"add_camp\": \"Yes\", \"edit_camp\": \"Yes\", \"camp_page\": \"Yes\"}',True,'2021-08-28',1,'2021-08-28',1);

INSERT INTO users_log (ID, User_name, Role, Added_at, Added_by, Updated_at, Updated_by) VALUES
(1, 'admin' , 1 , '2021-08-31', 1, '2021-09-11', 1);