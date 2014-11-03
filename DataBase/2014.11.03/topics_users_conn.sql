USE [szakdolgozat]
GO

/****** Object:  Table [dbo].[topics_users_conn]    Script Date: 11/03/2014 06:41:14 ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE TABLE [dbo].[topics_users_conn](
	[topicId] [int] NOT NULL,
	[userId] [int] NOT NULL
) ON [PRIMARY]

GO

ALTER TABLE [dbo].[topics_users_conn]  WITH CHECK ADD  CONSTRAINT [FK_topics_users_conn_topics] FOREIGN KEY([topicId])
REFERENCES [dbo].[topics] ([id])
ON UPDATE CASCADE
ON DELETE CASCADE
GO

ALTER TABLE [dbo].[topics_users_conn] CHECK CONSTRAINT [FK_topics_users_conn_topics]
GO

ALTER TABLE [dbo].[topics_users_conn]  WITH CHECK ADD  CONSTRAINT [FK_topics_users_conn_users] FOREIGN KEY([userId])
REFERENCES [dbo].[users] ([id])
ON UPDATE CASCADE
ON DELETE CASCADE
GO

ALTER TABLE [dbo].[topics_users_conn] CHECK CONSTRAINT [FK_topics_users_conn_users]
GO

