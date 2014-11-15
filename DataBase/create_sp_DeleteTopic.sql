DROP PROCEDURE IF EXISTS `sp_DeleteTopic` 
DELIMITER $$
CREATE PROCEDURE sp_DeleteTopic(
     	IN  p_id			   INT          
                
     )
BEGIN 

    DELETE FROM topics
    WHERE 
       id = p_id;

END$$
DELIMITER ;