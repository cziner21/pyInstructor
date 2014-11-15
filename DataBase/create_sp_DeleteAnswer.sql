DROP PROCEDURE IF EXISTS `sp_DeleteAnswer` 
DELIMITER $$
CREATE PROCEDURE sp_DeleteAnswer(
     	IN  p_id			   INT          
                
     )
BEGIN 

    DELETE FROM answers
    WHERE 
       id = p_id;

END$$
DELIMITER ;