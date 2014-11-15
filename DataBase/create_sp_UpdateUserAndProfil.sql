DROP PROCEDURE IF EXISTS `sp_UpdateUserAndProfil` 
DELIMITER $$
CREATE PROCEDURE sp_UpdateUserAndProfil(
     	IN  p_id			   INT,
        IN  p_firstName		           VARCHAR(255),       
        IN  p_lastName                     VARCHAR(255),
	IN  p_email			   VARCHAR(255),
	IN  p_city                         VARCHAR(255),
        IN  p_address			   VARCHAR(255),
        IN  p_phone			   VARCHAR(100),
        IN  p_birthday                     DATE,
        IN  p_privilidge                   INT(1)
           
                
     ) 
BEGIN 

    UPDATE users u
    INNER JOIN profil p ON u.id = p.userId
    SET                 
       u.firstName = p_firstName,
       u.lastName = p_lastName,
       u.email = p_email,
       p.city = p_city,
       p.address = p_address,
       p.phone = p_phone,
       p.birthday = p_birthday,
       p.privilidge = p_privilidge
    WHERE 
       u.id = p_id;

END$$
DELIMITER ;