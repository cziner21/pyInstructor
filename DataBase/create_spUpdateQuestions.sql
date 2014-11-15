DROP PROCEDURE IF EXISTS `sp_UpdateQuestions` 
DELIMITER $$
CREATE PROCEDURE sp_UpdateQuestions(
     	IN  p_id			   INT,
        IN  p_questionText                  VARCHAR(255),       
        IN  p_topicId                      INT
           
                
     )
BEGIN 

    UPDATE questions
    SET                 
       questionText = p_questionText,
       topicId = p_topicId
    WHERE 
       id = p_id;

END$$
DELIMITER ;