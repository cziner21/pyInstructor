USE [szakdolgozat]
GO

/****** Object:  Table [dbo].[users_results_conn]    Script Date: 10/25/2014 12:47:27 ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE TABLE [dbo].[users_results_conn](
	[userId] [int] NOT NULL,
	[resultId] [int] NOT NULL
) ON [PRIMARY]

GO

ALTER TABLE [dbo].[users_results_conn]  WITH CHECK ADD  CONSTRAINT [FK_users_results_conn_results] FOREIGN KEY([resultId])
REFERENCES [dbo].[results] ([id])
ON UPDATE CASCADE
ON DELETE CASCADE
GO

ALTER TABLE [dbo].[users_results_conn] CHECK CONSTRAINT [FK_users_results_conn_results]
GO

ALTER TABLE [dbo].[users_results_conn]  WITH CHECK ADD  CONSTRAINT [FK_users_results_conn_users] FOREIGN KEY([userId])
REFERENCES [dbo].[users] ([id])
ON UPDATE CASCADE
ON DELETE CASCADE
GO

ALTER TABLE [dbo].[users_results_conn] CHECK CONSTRAINT [FK_users_results_conn_users]
GO

