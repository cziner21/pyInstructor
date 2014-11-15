DROP PROCEDURE IF EXISTS `sp_UpdateAnswers` 
DELIMITER $$
CREATE PROCEDURE sp_UpdateAnswers(
     	IN  p_id			   INT,
        IN  p_answerText                  VARCHAR(255),           
	IN  p_isItCorrect		     BOOL,
	IN  p_topicId			      INT
           
                
     )
BEGIN 

    UPDATE answers
    SET                 
       answerText = p_answerText,
       isItCorrect = p_isItCorrect,
       topicId = p_topicId
    WHERE 
       id = p_id;

END$$
DELIMITER ;