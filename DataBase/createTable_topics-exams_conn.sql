USE [szakdolgozat]
GO

/****** Object:  Table [dbo].[topics_exams_conn]    Script Date: 10/25/2014 12:46:55 ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE TABLE [dbo].[topics_exams_conn](
	[topicId] [int] NOT NULL,
	[examId] [int] NULL
) ON [PRIMARY]

GO

ALTER TABLE [dbo].[topics_exams_conn]  WITH CHECK ADD  CONSTRAINT [FK_topics_exams_conn_exams] FOREIGN KEY([examId])
REFERENCES [dbo].[exams] ([id])
ON UPDATE CASCADE
ON DELETE CASCADE
GO

ALTER TABLE [dbo].[topics_exams_conn] CHECK CONSTRAINT [FK_topics_exams_conn_exams]
GO

ALTER TABLE [dbo].[topics_exams_conn]  WITH CHECK ADD  CONSTRAINT [FK_topics_exams_conn_topics] FOREIGN KEY([topicId])
REFERENCES [dbo].[topics] ([id])
ON UPDATE CASCADE
ON DELETE CASCADE
GO

ALTER TABLE [dbo].[topics_exams_conn] CHECK CONSTRAINT [FK_topics_exams_conn_topics]
GO

