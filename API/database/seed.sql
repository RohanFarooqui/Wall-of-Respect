-- ============================>  Table Data <============================

--  ====> Role <==== 
INSERT INTO roles (ID, Name, Access_level, Status, Added_at, Added_by, Updated_at, Updated_by) VALUES
(2, 'User [Page]'      ,'{"add_user": "No", "edit_user": "No", "user_page": "Yes", "add_role": "No", "edit_role": "No", "role_page": "No", "add_assc": "No", "edit_assc": "No", "assc_page": "No", "add_camp": "No", "edit_camp": "No", "camp_page": "No"}'           ,True,'2021-08-28',1,'2021-08-29',1),
(3, 'User [Edit]'      ,'{"add_user": "No", "edit_user": "Yes", "user_page": "Yes", "add_role": "No", "edit_role": "No", "role_page": "No", "add_assc": "No", "edit_assc": "No", "assc_page": "No", "add_camp": "No", "edit_camp": "No", "camp_page": "No"}'          ,True,'2021-08-29',1,'2021-08-29',1),
(4, 'User [Add]'       ,'{"add_user": "Yes", "edit_user": "No", "user_page": "Yes", "add_role": "No", "edit_role": "No", "role_page": "No", "add_assc": "No", "edit_assc": "No", "assc_page": "No", "add_camp": "No", "edit_camp": "No", "camp_page": "No"}'          ,True,'2021-08-29',1,'2021-08-29',1),
(5, 'User [All]'       ,'{"add_user": "Yes", "edit_user": "Yes", "user_page": "Yes", "add_role": "No", "edit_role": "No", "role_page": "No", "add_assc": "No", "edit_assc": "No", "assc_page": "No", "add_camp": "No", "edit_camp": "No", "camp_page": "No"}'         ,True,'2021-08-29',1,'2021-08-29',1),
(6, 'Role [Page]'      ,'{"add_user": "No", "edit_user": "No", "user_page": "No", "add_role": "No", "edit_role": "No", "role_page": "Yes", "add_assc": "No", "edit_assc": "No", "assc_page": "No", "add_camp": "No", "edit_camp": "No", "camp_page": "No"}'           ,True,'2021-08-29',1,'2021-08-29',1),
(7, 'Role [Edit]'      ,'{"add_user": "No", "edit_user": "No", "user_page": "No", "add_role": "No", "edit_role": "Yes", "role_page": "Yes", "add_assc": "No", "edit_assc": "No", "assc_page": "No", "add_camp": "No", "edit_camp": "No", "camp_page": "No"}'          ,True,'2021-08-29',1,'2021-08-29',1),
(8, 'Role [Add]'       ,'{"add_user": "No", "edit_user": "No", "user_page": "No", "add_role": "Yes", "edit_role": "No", "role_page": "Yes", "add_assc": "No", "edit_assc": "No", "assc_page": "No", "add_camp": "No", "edit_camp": "No", "camp_page": "No"}'          ,True,'2021-08-29',1,'2021-08-29',1),
(9, 'Role [All]'       ,'{"add_user": "No", "edit_user": "No", "user_page": "No", "add_role": "Yes", "edit_role": "Yes", "role_page": "Yes", "add_assc": "No", "edit_assc": "No", "assc_page": "No", "add_camp": "No", "edit_camp": "No", "camp_page": "No"}'         ,True,'2021-08-29',1,'2021-08-29',1),
(10,'Associate  [Page]','{"add_user": "No", "edit_user": "No", "user_page": "No", "add_role": "No", "edit_role": "No", "role_page": "No", "add_assc": "No", "edit_assc": "No", "assc_page": "Yes", "add_camp": "No", "edit_camp": "No", "camp_page": "No"}'           ,True,'2021-08-29',1,'2021-08-29',1),
(11,'Associate [Edit]' ,'{"add_user": "No", "edit_user": "No", "user_page": "No", "add_role": "No", "edit_role": "No", "role_page": "No", "add_assc": "No", "edit_assc": "Yes", "assc_page": "Yes", "add_camp": "No", "edit_camp": "No", "camp_page": "No"}'          ,True,'2021-08-29',1,'2021-08-29',1),
(12,'Associate [Add]'  ,'{"add_user": "No", "edit_user": "No", "user_page": "No", "add_role": "No", "edit_role": "No", "role_page": "No", "add_assc": "Yes", "edit_assc": "No", "assc_page": "Yes", "add_camp": "No", "edit_camp": "No", "camp_page": "No"}'          ,True,'2021-08-29',1,'2021-08-29',1),
(13,'Associate [All]'  ,'{"add_user": "No", "edit_user": "No", "user_page": "No", "add_role": "No", "edit_role": "No", "role_page": "No", "add_assc": "Yes", "edit_assc": "Yes", "assc_page": "Yes", "add_camp": "No", "edit_camp": "No", "camp_page": "No"}'         ,True,'2021-08-29',1,'2021-08-29',1),
(14,'Campaign [Page]'  ,'{"add_user": "No", "edit_user": "No", "user_page": "No", "add_role": "No", "edit_role": "No", "role_page": "No", "add_assc": "No", "edit_assc": "No", "assc_page": "No", "add_camp": "No", "edit_camp": "No", "camp_page": "Yes"}'           ,True,'2021-08-29',1,'2021-08-29',1),
(15,'Campaign [Edit]'  ,'{"add_user": "No", "edit_user": "No", "user_page": "No", "add_role": "No", "edit_role": "No", "role_page": "No", "add_assc": "No", "edit_assc": "No", "assc_page": "No", "add_camp": "No", "edit_camp": "Yes", "camp_page": "Yes"}'          ,True,'2021-08-29',1,'2021-08-29',1),
(16,'Campaign [Add]'   ,'{"add_user": "No", "edit_user": "No", "user_page": "No", "add_role": "No", "edit_role": "No", "role_page": "No", "add_assc": "No", "edit_assc": "No", "assc_page": "No", "add_camp": "Yes", "edit_camp": "No", "camp_page": "Yes"}'          ,True,'2021-08-29',1,'2021-08-29',1),
(17,'Campaign [ALL]'   ,'{"add_user": "No", "edit_user": "No", "user_page": "No", "add_role": "No", "edit_role": "No", "role_page": "No", "add_assc": "No", "edit_assc": "No", "assc_page": "No", "add_camp": "Yes", "edit_camp": "Yes", "camp_page": "Yes"}'         ,True,'2021-08-29',1,'2021-08-29',1),
(18,'View'             ,'{"add_user": "No", "edit_user": "No", "user_page": "Yes", "add_role": "No", "edit_role": "No", "role_page": "Yes", "add_assc": "No", "edit_assc": "No", "assc_page": "Yes", "add_camp": "No", "edit_camp": "No", "camp_page": "Yes"}'        ,True,'2021-09-12',1,'2021-09-12',1);


--  ====> Users <==== 
INSERT INTO users (ID, Name, User_name, Img_path, Email, Pswd, Status) VALUES
(2,'Ali Wajid Raza' ,'ali'   ,'/media/users/11-09-2021%2017%2558%20PM-Ali%20Wajid%20Raza.png','ali.raza@touchstone.com.pk'   ,'81dc9bdb52d04dc20036dbd8313ed055',True),
(3,'Abdur Rehman'   ,'AR'    ,'/media/users/13-09-2021%2001%2543%20AM-Abdur%20Rehman.png'    ,'abdurrehman@touchstone.com.pk','81dc9bdb52d04dc20036dbd8313ed055',True),
(4,'Talha Hayat'    ,'talha' ,'/media/users/11-09-2021%2018%2502%20PM-Talha%20Hayat.png'     ,'Talha.Hayat@touchstone.com.pk','81dc9bdb52d04dc20036dbd8313ed055',True),
(5,'Mustafeez Rasul','mrasul','/media/users/11-09-2021%2019%2508%20PM-Mustafeez%20Rasul.png' ,'mrasul@touchstone.com.pk'     ,'81dc9bdb52d04dc20036dbd8313ed055',True),
(6,'Test'           ,'test'  ,'/media/users/12-09-2021%2020%2525%20PM-Test.png'              ,'test@gmail.com'               ,'81dc9bdb52d04dc20036dbd8313ed055',True);

--  ====> Users Logs <==== 
INSERT INTO users_log (ID, User_name, Role, Added_at, Added_by, Updated_at, Updated_by) VALUES
(2, 'ali'   , 1 , '2021-08-31', 1, '2021-09-11', 1),
(3, 'AR'    , 1 , '2021-08-31', 1, '2021-09-13', 1),
(4, 'talha' , 1 , '2021-09-11', 1, '2021-09-11', 1),
(5, 'mrasul', 1 , '2021-09-11', 1, '2021-09-11', 1),
(6, 'test'  , 18, '2021-09-12', 1, '2021-09-13', 1);

--  ====> Campaign <==== 
INSERT INTO campaign (ID, Name, Status, Added_at, Added_by, Updated_at, Updated_by) VALUES
(1, 'Solar '               , True, '2021-08-25', 1, '2021-09-12', 1),
(2, 'Mortgage'             , True, '2021-08-25', 1, '2021-09-12', 1),
(3, 'Auto Warranty '       , True, '2021-08-25', 1, '2021-09-12', 1),
(4, 'Quality assurance'    , True, '2021-08-25', 1, '2021-09-12', 1),
(5, 'Management operations', True, '2021-08-25', 1, '2021-09-12', 1),
(6, 'CMU-1'                , True, '2021-08-25', 1, '2021-08-25', 1),
(7, 'GDR'                  , True, '2021-08-25', 1, '2021-08-25', 1),
(8, 'EDDY'                 , True, '2021-08-25', 1, '2021-08-25', 1),
(9, 'EDDY-IB'              , True, '2021-08-25', 1, '2021-08-25', 1),
(10, 'EDDY-OB'             , True, '2021-08-25', 1, '2021-08-25', 1),
(11, 'Training Dept.'      , True, '2021-08-25', 1, '2021-08-25', 1),
(12, 'Admin'               , True, '2021-08-25', 1, '2021-08-25', 1);

--  ====> Associates <==== 
INSERT INTO associates_info (ID, Name, Designation, Description, moti_quote, Img_path, Campaign_id, Status, Added_at, Added_by, Updated_at, Updated_by) VALUES
(1, 'MUHAMMAD NAUMAN', 'Mortgage', 'Member of the Mortgage program.', 'It''s not how far you fall, but how high you bounce that counts. Every setback is an opportunity to return stronger, wiser, and more determined than before.', '/media/associates/25-08-2021%2002%2528%20AM-MUHAMMAD%20.png'          , 2 , True, '2021-08-25', 1, '2021-09-12', 1),
(2, 'AMEER HAMZA', 'Solar', 'Member of the Solar program.', 'Go an extra mile, because it is never crowded. Consistent effort beyond what is expected is what turns ordinary work into meaningful achievement.', '/media/associates/25-08-2021%2002%2530%20AM-AMEER%20.png'             , 1 , True, '2021-08-25', 1, '2021-08-25', 1),
(3, 'BISMA ANWAR', 'CMU-1', 'Member of the CMU-1 program.', 'Keep your squats low and your standards high. Real progress comes from discipline, patience, and refusing to compromise on the quality of your work.', '/media/associates/25-08-2021%2003%2526%20AM-BISMA%20.png'             , 6 , True, '2021-08-25', 1, '2021-08-25', 1),
(4, 'ABDUL MANNAN', 'GDR', 'Member of the GDR program.', 'Strive for progress, not perfection. Small improvements made consistently will take you further than waiting for the perfect moment to begin.', '/media/associates/25-08-2021%2003%2527%20AM-ABDUL%20.png'             , 7 , True, '2021-08-25', 1, '2021-08-25', 1),
(5, 'EHSAN UL HAQ', 'EDDY', 'Member of the EDDY program.', 'Quality means doing it right even when no one is looking. Let excellence become a habit that reflects your character in every task you complete.', '/media/associates/25-08-2021%2003%2530%20AM-EHSAN%20.png'             , 8 , True, '2021-08-25', 1, '2021-08-25', 1),
(6, 'HUMAYUN  JAVED', 'EDDY-IB', 'Member of the EDDY-IB program.', 'I don''t know the word quit; either I never did, or I have abolished it. Challenges may slow you down, but determination will always keep you moving forward.', '/media/associates/25-08-2021%2003%2532%20AM-HUMAYUN%20.png'           , 9 , True, '2021-08-25', 1, '2021-08-25', 1),
(7, 'ABEER ASLAM', 'EDDY-OB', 'Member of the EDDY-OB program.', 'Success is the sum of small efforts repeated day in and day out. Stay consistent, trust the process, and allow your daily actions to build remarkable results.', '/media/associates/25-08-2021%2003%2541%20AM-ABEER.png'                , 10, True, '2021-08-25', 1, '2021-08-25', 1),
(8, 'Faizan Jamil  Hashmi', 'Management Operations', 'Member of the Management Operations program.', 'Blood, sweat, and respect: the first two you give, and the last one you earn. Dedication and honest effort create a reputation that words alone cannot build.', '/media/associates/25-08-2021%2003%2543%20AM-Faizan%20Jamil%20.png'    , 5 , True, '2021-08-25', 1, '2021-08-25', 1),
(9, 'Syed Muhammad Ali', 'Training Department', 'Member of the Training Department.', 'Minds are like parachutes; they work best when open. Stay curious, welcome new ideas, and never stop learning from the people and experiences around you.', '/media/associates/25-08-2021%2003%2545%20AM-Syed%20Muhammad.png'      , 11, True, '2021-08-25', 1, '2021-08-25', 1),
(10, 'Nasir Ali', 'Administration', 'Member of the Administration team.', 'There is no substitute for hard work; always remain humble and hungry. Let your achievements inspire greater effort instead of making you comfortable.', '/media/associates/25-08-2021%2003%2546%20AM-Nasir%20.png'             , 12, True, '2021-08-25', 1, '2021-08-25', 1),
(11, 'Danyal Mansoor', 'Quality Assurance', 'Member of the Quality Assurance team.', 'Quality is a reflection of you. Give every responsibility your full attention so that the final result represents your commitment, care, and professionalism.', '/media/associates/25-08-2021%2003%2547%20AM-Danyal%20.png'            , 4 , True, '2021-08-25', 1, '2021-09-12', 1),
(12, 'Nimra Aleem', 'Mortgage', 'Member of the Mortgage program.', 'Quality is a reflection of you. Approach each task with care, because consistent excellence builds trust and leaves a lasting impression.', '/media/associates/12-09-2021%2020%2524%20PM-Nimra%20Aleem.png'        , 2 , True, '2021-09-12', 1, '2021-09-12', 1),
(13, 'Samiullah Saeed', 'Solar', 'Member of the Solar program.', 'There is no substitute for hard work; always remain humble and hungry. Success grows when ambition is balanced with gratitude and respect for others.', '/media/associates/12-09-2021%2020%2524%20PM-Samiullah%20Saeed.png'    , 1 , True, '2021-09-12', 1, '2021-09-12', 1),
(14, 'Umaima', 'Mortgage', 'Member of the Mortgage program.', 'It''s not how far you fall, but how high you bounce that counts. Difficult moments do not define you; the courage to rise and continue does.', '/media/associates/12-09-2021%2020%2524%20PM-Umaima.png'               , 2 , True, '2021-09-12', 1, '2021-09-12', 1),
(15, 'Zarafshan Yousafzai', 'Solar', 'Member of the Solar program.', 'Go an extra mile, because it is never crowded. The additional effort you make today can become the opportunity and success you experience tomorrow.', '/media/associates/12-09-2021%2020%2524%20PM-Zarafshan%20Yousafzai.png', 2 , True, '2021-09-12', 1, '2021-09-12', 1);
