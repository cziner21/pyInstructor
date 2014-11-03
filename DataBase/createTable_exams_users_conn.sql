USE [szakdolgozat]
GO

/****** Object:  Table [dbo].[exams_users_conn]    Script Date: 10/25/2014 12:45:15 ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE TABLE [dbo].[exams_users_conn](
	[examId] [int] NOT NULL,
	[userId] [int] NOT NULL
) ON [PRIMARY]

GO

ALTER TABLE [dbo].[exams_users_conn]  WITH CHECK ADD  CONSTRAINT [FK_exams_users_conn_exams] FOREIGN KEY([examId])
REFERENCES [dbo].[exams] ([id])
ON UPDATE CASCADE
ON DELETE CASCADE
GO

ALTER TABLE [dbo].[exams_users_conn] CHECK CONSTRAINT [FK_exams_users_conn_exams]
GO

ALTER TABLE [dbo].[exams_users_conn]  WITH CHECK ADD  CONSTRAINT [FK_exams_users_conn_users] FOREIGN KEY([userId])
REFERENCES [dbo].[users] ([id])
ON UPDATE CASCADE
ON DELETE CASCADE
GO

ALTER TABLE [dbo].[exams_users_conn] CHECK CONSTRAINT [FK_exams_users_conn_users]
GO

