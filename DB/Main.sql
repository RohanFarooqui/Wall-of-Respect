/*=======================================================>  Wall of Respect <=======================================================*/
DROP DATABASE If EXISTS Wall_of_Fame ;

Ceate DATABASE Wall_of_Frame;

Use Wall_of_Fame;


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