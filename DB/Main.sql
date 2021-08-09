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

