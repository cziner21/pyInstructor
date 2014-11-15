DROP PROCEDURE IF EXISTS `sp_DeleteQuestion` 
DELIMITER $$
CREATE PROCEDURE sp_DeleteQuestion(
     	IN  p_id			   INT          
                
     )
BEGIN 

    DELETE FROM questions       
    WHERE 
       id = p_id;

END$$
DELIMITER ;