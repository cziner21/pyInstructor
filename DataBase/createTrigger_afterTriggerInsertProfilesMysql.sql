delimiter $$

CREATE TRIGGER afterTriggerInsertProfiles AFTER INSERT ON users
FOR EACH ROW 
BEGIN
 insert into profil(userId)
 select id from users where id = New.id;
END$$
delimiter ;