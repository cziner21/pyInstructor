DROP PROCEDURE IF EXISTS `sp_DeleteUser` 
DELIMITER $$
CREATE PROCEDURE sp_DeleteUser(
     	IN  p_id			   INT          
                
     )
BEGIN 

    DELETE FROM users
    WHERE 
       id = p_id;

END$$
DELIMITER ;