USE [szakdolgozat]
GO

/****** Object:  Table [dbo].[results_topics_conn]    Script Date: 10/25/2014 12:46:22 ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE TABLE [dbo].[results_topics_conn](
	[resultId] [int] NOT NULL,
	[topicsId] [int] NOT NULL
) ON [PRIMARY]

GO

ALTER TABLE [dbo].[results_topics_conn]  WITH CHECK ADD  CONSTRAINT [FK_results_topics_conn_results] FOREIGN KEY([resultId])
REFERENCES [dbo].[results] ([id])
ON UPDATE CASCADE
ON DELETE CASCADE
GO

ALTER TABLE [dbo].[results_topics_conn] CHECK CONSTRAINT [FK_results_topics_conn_results]
GO

ALTER TABLE [dbo].[results_topics_conn]  WITH CHECK ADD  CONSTRAINT [FK_results_topics_conn_topics] FOREIGN KEY([topicsId])
REFERENCES [dbo].[topics] ([id])
ON UPDATE CASCADE
ON DELETE CASCADE
GO

ALTER TABLE [dbo].[results_topics_conn] CHECK CONSTRAINT [FK_results_topics_conn_topics]
GO

