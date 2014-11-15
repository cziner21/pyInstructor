DELIMITER $$
CREATE PROCEDURE sp_InsertIntoUsers(
     
        IN  p_firstname                    VARCHAR(255),       
        IN  p_lastname                      VARCHAR(255), 
        IN  p_email                    VARCHAR(255), 
        IN  p_password                      VARCHAR(255)   
                
     )
BEGIN 

    INSERT INTO users
         (
           firtname, 
           lastname, 
           email, 
           password
         )
    VALUES 
         ( 
           p_firstname, 
           p_lastname, 
           p_email, 
           p_password                 
         ) ; 
END$$
DELIMITER ;
