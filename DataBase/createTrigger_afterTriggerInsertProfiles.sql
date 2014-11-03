USE [szakdolgozat]
GO

/****** Object:  Trigger [dbo].[afterTriggerInsertProfiles]    Script Date: 10/25/2014 12:48:30 ******/
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

