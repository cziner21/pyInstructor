DROP PROCEDURE IF EXISTS `sp_UpdateOwnuserDataAndProfil` 
DELIMITER $$
CREATE PROCEDURE sp_UpdateOwnuserDataAndProfil(
     	IN  p_id			   INT,
        IN  p_firstName		           VARCHAR(255),       
        IN  p_lastName                     VARCHAR(255),
	IN  p_email			   VARCHAR(255),
	In  p_password                     VARCHAR(255),
	IN  p_city                         VARCHAR(255),
        IN  p_address			   VARCHAR(255),
        IN  p_phone			   VARCHAR(100),
        IN  p_birthday                     DATE
        
           
                
     ) 
BEGIN 

    UPDATE users u
    INNER JOIN profil p ON u.id = p.userId
    SET                 
       u.firstName = p_firstName,
       u.lastName = p_lastName,
       u.email = p_email,
       u.password = p_password,
       p.city = p_city,
       p.address = p_address,
       p.phone = p_phone,
       p.birthday = p_birthday
       
    WHERE 
       u.id = p_id;

END$$
DELIMITER ;