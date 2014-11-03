USE [szakdolgozat]
GO

/****** Object:  Trigger [dbo].[afterTriggerInsertProfiles]    Script Date: 11/03/2014 06:42:13 ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE TRIGGER [dbo].[afterTriggerInsertProfiles] ON [dbo].[users]
FOR INSERT
AS 
BEGIN 
    insert into [dbo].[profils]
           (userId) 
    SELECT id
    FROM inserted
END


GO

