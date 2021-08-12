/*============================>  Table Data <============================*/

/* ====> Role <==== */

INSERT INTO `roles` (`ID`, `Name`, `Access_level`, `Status`, `Added_at`, `Added_by`, `Updated_at`, `Updated_by`) VALUES
(1, 'Admin', '{\"add_user\": \"Yes\", \"edit_user\": \"Yes\", \"user_page\": \"Yes\", \"add_role\": \"Yes\", \"edit_role\": \"Yes\", \"role_page\": \"Yes\", \"add_assc\": \"Yes\", \"edit_assc\": \"Yes\", \"assc_page\": \"Yes\", \"add_camp\": \"Yes\", \"edit_camp\": \"Yes\", \"camp_page\": \"Yes\"}', 1, '2021-08-28', 1, '2021-08-28', 1),
(2, 'User [Page]', '{\"add_user\": \"No\", \"edit_user\": \"No\", \"user_page\": \"Yes\", \"add_role\": \"No\", \"edit_role\": \"No\", \"role_page\": \"No\", \"add_assc\": \"No\", \"edit_assc\": \"No\", \"assc_page\": \"No\", \"add_camp\": \"No\", \"edit_camp\": \"No\", \"camp_page\": \"No\"}', 1, '2021-08-28', 1, '2021-08-29', 1),
(3, 'User [Edit]', '{\"add_user\": \"No\", \"edit_user\": \"Yes\", \"user_page\": \"Yes\", \"add_role\": \"No\", \"edit_role\": \"No\", \"role_page\": \"No\", \"add_assc\": \"No\", \"edit_assc\": \"No\", \"assc_page\": \"No\", \"add_camp\": \"No\", \"edit_camp\": \"No\", \"camp_page\": \"No\"}', 1, '2021-08-29', 1, '2021-08-29', 1),
(4, 'User [Add]', '{\"add_user\": \"Yes\", \"edit_user\": \"No\", \"user_page\": \"Yes\", \"add_role\": \"No\", \"edit_role\": \"No\", \"role_page\": \"No\", \"add_assc\": \"No\", \"edit_assc\": \"No\", \"assc_page\": \"No\", \"add_camp\": \"No\", \"edit_camp\": \"No\", \"camp_page\": \"No\"}', 1, '2021-08-29', 1, '2021-08-29', 1),
(5, 'User [All]', '{\"add_user\": \"Yes\", \"edit_user\": \"Yes\", \"user_page\": \"Yes\", \"add_role\": \"No\", \"edit_role\": \"No\", \"role_page\": \"No\", \"add_assc\": \"No\", \"edit_assc\": \"No\", \"assc_page\": \"No\", \"add_camp\": \"No\", \"edit_camp\": \"No\", \"camp_page\": \"No\"}', 1, '2021-08-29', 1, '2021-08-29', 1),
(6, 'Role [Page]', '{\"add_user\": \"No\", \"edit_user\": \"No\", \"user_page\": \"No\", \"add_role\": \"No\", \"edit_role\": \"No\", \"role_page\": \"Yes\", \"add_assc\": \"No\", \"edit_assc\": \"No\", \"assc_page\": \"No\", \"add_camp\": \"No\", \"edit_camp\": \"No\", \"camp_page\": \"No\"}', 1, '2021-08-29', 1, '2021-08-29', 1),
(7, 'Role [Edit]', '{\"add_user\": \"No\", \"edit_user\": \"No\", \"user_page\": \"No\", \"add_role\": \"No\", \"edit_role\": \"Yes\", \"role_page\": \"Yes\", \"add_assc\": \"No\", \"edit_assc\": \"No\", \"assc_page\": \"No\", \"add_camp\": \"No\", \"edit_camp\": \"No\", \"camp_page\": \"No\"}', 1, '2021-08-29', 1, '2021-08-29', 1),
(8, 'Role [Add]', '{\"add_user\": \"No\", \"edit_user\": \"No\", \"user_page\": \"No\", \"add_role\": \"Yes\", \"edit_role\": \"No\", \"role_page\": \"Yes\", \"add_assc\": \"No\", \"edit_assc\": \"No\", \"assc_page\": \"No\", \"add_camp\": \"No\", \"edit_camp\": \"No\", \"camp_page\": \"No\"}', 1, '2021-08-29', 1, '2021-08-29', 1),
(9, 'Role [All]', '{\"add_user\": \"No\", \"edit_user\": \"No\", \"user_page\": \"No\", \"add_role\": \"Yes\", \"edit_role\": \"Yes\", \"role_page\": \"Yes\", \"add_assc\": \"No\", \"edit_assc\": \"No\", \"assc_page\": \"No\", \"add_camp\": \"No\", \"edit_camp\": \"No\", \"camp_page\": \"No\"}', 1, '2021-08-29', 1, '2021-08-29', 1),
(10, 'Associate  [Page]', '{\"add_user\": \"No\", \"edit_user\": \"No\", \"user_page\": \"No\", \"add_role\": \"No\", \"edit_role\": \"No\", \"role_page\": \"No\", \"add_assc\": \"No\", \"edit_assc\": \"No\", \"assc_page\": \"Yes\", \"add_camp\": \"No\", \"edit_camp\": \"No\", \"camp_page\": \"No\"}', 1, '2021-08-29', 1, '2021-08-29', 1),
(11, 'Associate [Edit]', '{\"add_user\": \"No\", \"edit_user\": \"No\", \"user_page\": \"No\", \"add_role\": \"No\", \"edit_role\": \"No\", \"role_page\": \"No\", \"add_assc\": \"No\", \"edit_assc\": \"Yes\", \"assc_page\": \"Yes\", \"add_camp\": \"No\", \"edit_camp\": \"No\", \"camp_page\": \"No\"}', 1, '2021-08-29', 1, '2021-08-29', 1),
(12, 'Associate [Add]', '{\"add_user\": \"No\", \"edit_user\": \"No\", \"user_page\": \"No\", \"add_role\": \"No\", \"edit_role\": \"No\", \"role_page\": \"No\", \"add_assc\": \"Yes\", \"edit_assc\": \"No\", \"assc_page\": \"Yes\", \"add_camp\": \"No\", \"edit_camp\": \"No\", \"camp_page\": \"No\"}', 1, '2021-08-29', 1, '2021-08-29', 1),
(13, 'Associate [All]', '{\"add_user\": \"No\", \"edit_user\": \"No\", \"user_page\": \"No\", \"add_role\": \"No\", \"edit_role\": \"No\", \"role_page\": \"No\", \"add_assc\": \"Yes\", \"edit_assc\": \"Yes\", \"assc_page\": \"Yes\", \"add_camp\": \"No\", \"edit_camp\": \"No\", \"camp_page\": \"No\"}', 1, '2021-08-29', 1, '2021-08-29', 1),
(14, 'Campaign [Page]', '{\"add_user\": \"No\", \"edit_user\": \"No\", \"user_page\": \"No\", \"add_role\": \"No\", \"edit_role\": \"No\", \"role_page\": \"No\", \"add_assc\": \"No\", \"edit_assc\": \"No\", \"assc_page\": \"No\", \"add_camp\": \"No\", \"edit_camp\": \"No\", \"camp_page\": \"Yes\"}', 1, '2021-08-29', 1, '2021-08-29', 1),
(15, 'Campaign [Edit]', '{\"add_user\": \"No\", \"edit_user\": \"No\", \"user_page\": \"No\", \"add_role\": \"No\", \"edit_role\": \"No\", \"role_page\": \"No\", \"add_assc\": \"No\", \"edit_assc\": \"No\", \"assc_page\": \"No\", \"add_camp\": \"No\", \"edit_camp\": \"Yes\", \"camp_page\": \"Yes\"}', 1, '2021-08-29', 1, '2021-08-29', 1),
(16, 'Campaign [Add]', '{\"add_user\": \"No\", \"edit_user\": \"No\", \"user_page\": \"No\", \"add_role\": \"No\", \"edit_role\": \"No\", \"role_page\": \"No\", \"add_assc\": \"No\", \"edit_assc\": \"No\", \"assc_page\": \"No\", \"add_camp\": \"Yes\", \"edit_camp\": \"No\", \"camp_page\": \"Yes\"}', 1, '2021-08-29', 1, '2021-08-29', 1),
(17, 'Campaign [ALL]', '{\"add_user\": \"No\", \"edit_user\": \"No\", \"user_page\": \"No\", \"add_role\": \"No\", \"edit_role\": \"No\", \"role_page\": \"No\", \"add_assc\": \"No\", \"edit_assc\": \"No\", \"assc_page\": \"No\", \"add_camp\": \"Yes\", \"edit_camp\": \"Yes\", \"camp_page\": \"Yes\"}', 1, '2021-08-29', 1, '2021-08-29', 1),
(18, 'View', '{\"add_user\": \"No\", \"edit_user\": \"No\", \"user_page\": \"Yes\", \"add_role\": \"No\", \"edit_role\": \"No\", \"role_page\": \"Yes\", \"add_assc\": \"No\", \"edit_assc\": \"No\", \"assc_page\": \"Yes\", \"add_camp\": \"No\", \"edit_camp\": \"No\", \"camp_page\": \"Yes\"}', 1, '2021-09-12', 1, '2021-09-12', 1);


/* ====> Users <==== */

INSERT INTO `users` (`ID`, `Name`, `User_name`, `Img_path`, `Email`, `Pswd`, `Status`) VALUES
(1, 'Admin', 'admin', '/Media/11-09-2021%2018%2500%20PM-Admin.png', 'admin@gmail.com', '81dc9bdb52d04dc20036dbd8313ed055', 1),
(2, 'Ali Wajid Raza', 'ali', '/Media/11-09-2021%2017%2558%20PM-Ali%20Wajid%20Raza.png', 'ali.raza@touchstone.com.pk', '81dc9bdb52d04dc20036dbd8313ed055', 1),
(3, 'Abdur Rehman', 'AR', '/Media/13-09-2021%2001%2543%20AM-Abdur%20Rehman.png', 'abdurrehman@touchstone.com.pk', '81dc9bdb52d04dc20036dbd8313ed055', 1),
(4, 'Talha Hayat', 'talha', '/Media/11-09-2021%2018%2502%20PM-Talha%20Hayat.png', 'Talha.Hayat@touchstone.com.pk', '81dc9bdb52d04dc20036dbd8313ed055', 1),
(5, 'Mustafeez Rasul', 'mrasul', '/Media/11-09-2021%2019%2508%20PM-Mustafeez%20Rasul.png', 'mrasul@touchstone.com.pk', '81dc9bdb52d04dc20036dbd8313ed055', 1),
(6, 'Test', 'test', '/Media/12-09-2021%2020%2525%20PM-Test.png', 'test@gmail.com', '81dc9bdb52d04dc20036dbd8313ed055', 0);

/* ====> Users Logs <==== */
INSERT INTO `users_log` (`ID`, `User_name`, `Role`, `Added_at`, `Added_by`, `Updated_at`, `Updated_by`) VALUES
(1, 'admin', 1, '2021-08-31', 1, '2021-09-11', 1),
(2, 'ali', 1, '2021-08-31', 1, '2021-09-11', 1),
(3, 'AR', 1, '2021-08-31', 1, '2021-09-13', 1),
(4, 'talha', 1, '2021-09-11', 1, '2021-09-11', 1),
(5, 'mrasul', 1, '2021-09-11', 1, '2021-09-11', 1),
(6, 'test', 18, '2021-09-12', 1, '2021-09-13', 1);