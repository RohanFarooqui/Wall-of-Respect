/*=======================================================>  Wall of Respect <=======================================================*/
DROP DATABASE If EXISTS Wall_of_Fame ;

Ceate DATABASE Wall_of_Frame;

Use Wall_of_Fame;

/*============================>  Tables <============================*/
/* => Creating Role Table */
CREATE TABLE Roles(
    ID            int NOT NULL AUTO_INCREMENT, 
    Name          VARCHAR(100),               
    Access_level  Text,
    Status        boolean,
    Added_at      Date,
    Added_by      INT,
    Updated_at    Date,
    Updated_by    INT,    
    /* Constraints */
    PRIMARY KEY(ID),
    UNIQUE(Name)
);

/* => Creating User Table */
CREATE TABLE Users(
    ID            int NOT NULL AUTO_INCREMENT,
    Name          Varchar(100),  
    User_name     VARCHAR(100), 
    Img_path      VARCHAR(100),
    Email         Varchar(30),
    Pswd          CHAR(32),  
    Status        boolean,
    /* Constraints */
    PRIMARY KEY(ID),
    UNIQUE(User_Name),
    UNIQUE(Email)
);

/* => Creating User_Log Table */
Create Table Users_Log(
    ID            int NOT NULL AUTO_INCREMENT,
    User_name     VARCHAR(100), 
    Role          int NOT NULL,
    Added_at      Date,
    Added_by      INT,
    Updated_at    Date,
    Updated_by    INT, 
    /* Constraints */
    PRIMARY KEY(ID),
    UNIQUE(User_Name),
    FOREIGN KEY (Role) REFERENCES Roles(ID),
    FOREIGN KEY (Added_by) REFERENCES  Users(ID),
    FOREIGN KEY (Updated_by) REFERENCES  Users(ID)
);

/* => Creating Campaign Table */
CREATE TABLE Campaign(
    ID            int NOT NULL AUTO_INCREMENT,
    Name          VARCHAR(255),
    Status        boolean,
    Added_at      Date,
    Added_by      INT,
    Updated_at    Date,
    Updated_by    INT,    
    /* Constraints */
    PRIMARY KEY(ID),
    UNIQUE(Name)
);

/* => Creating Associates'Info Table */
CREATE TABLE Associates_info(
    ID            int NOT NULL AUTO_INCREMENT,
    Name          Varchar(100),
    Designation   Varchar(100),  
    Description   TEXT, 
    moti_quote    TEXT,  
    Img_path      VARCHAR(255),
    Campaign_id   int,
    Status        boolean,
    Added_at      Date,
    Added_by      INT,
    Updated_at    Date,
    Updated_by    INT,
    /* Constraints */
    PRIMARY KEY (ID),
    FOREIGN KEY (Campaign_id) REFERENCES Campaign(ID),
    FOREIGN KEY (Added_by) REFERENCES Users(ID),
    FOREIGN KEY (Updated_by) REFERENCES Users(ID),
    UNIQUE(Name)
);

/* => Alter Commands */
ALTER TABLE Roles AUTO_INCREMENT=1;
ALTER TABLE Users AUTO_INCREMENT=1;
ALTER TABLE Users_Log AUTO_INCREMENT=1;
ALTER TABLE Campaign AUTO_INCREMENT=1;
ALTER TABLE Associates_info AUTO_INCREMENT=1;
ALTER TABLE Campaign  ADD FOREIGN KEY (Added_by)   REFERENCES Users(ID);  
ALTER TABLE Campaign  ADD FOREIGN KEY (Updated_by) REFERENCES Users(ID); 
ALTER TABLE Roles     ADD FOREIGN KEY (Added_by)   REFERENCES Users(ID); 
ALTER TABLE Roles     ADD FOREIGN KEY (Updated_by) REFERENCES Users(ID);

/*============================>  Procedures <============================*/

/**** => Creating Role Procedures ****/

/* Add Role */
DELIMITER $$
CREATE PROCEDURE Add_Role(
    IN Name           Varchar(100),
    IN Access_level   Text,
    IN Added_by       INT
)
BEGIN 
    INSERT INTO `roles`(`Name`, `Access_level`, `Status`, `Added_at`, `Added_by`, `Updated_at`, `Updated_by`)
        VALUES (Name,Access_level,1,current_date(),Added_by,current_date(),Added_by);
END$$
DELIMITER ;

/* Update Role */
DELIMITER $$
CREATE PROCEDURE Update_Role ( 
    IN roll_name VARCHAR(100),
    IN Access_level Text,
    IN Status boolean,
    IN Updated_by INT,
    IN roll_id INT)
BEGIN
    UPDATE `roles` 
        SET `Name`= Roll_Name,`Access_level`=Access_level,`Updated_at`= current_date(),`Status`=Status,`Updated_by`= Updated_by
            WHERE `ID` = roll_id; 

    IF Status = 1 THEN
        UPDATE `users` INNER JOIN `users_log` ON users.ID = users_log.ID SET users.Status = 1 WHERE users_log.Role =  roll_id; 
    ELSE 
         UPDATE `users` INNER JOIN `users_log` ON users.ID = users_log.ID SET users.Status = 0 WHERE users_log.Role =  roll_id; 
    END IF;
    
END$$
DELIMITER ;

/* View Role */
DELIMITER $$
CREATE PROCEDURE list_Roll ()
BEGIN
    SELECT  roles.ID,roles.Name,roles.Access_level,roles.Status,roles.Added_at,
        a.User_name as Added_by ,
        roles.Updated_at,
        b.User_name as Updated_by
        FROM roles 
            INNER JOIN users  AS a  ON roles.Added_by = a.ID
            INNER JOIN users  As b  ON roles.Updated_by = b.ID; 
END$$
DELIMITER ;



