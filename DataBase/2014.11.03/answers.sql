USE [szakdolgozat]
GO

/****** Object:  Table [dbo].[answers]    Script Date: 11/03/2014 06:40:12 ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE TABLE [dbo].[answers](
	[id] [int] IDENTITY(1,1) NOT NULL,
	[answerText] [nvarchar](max) NOT NULL,
	[questionId] [int] NOT NULL,
	[topicsId] [int] NOT NULL,
 CONSTRAINT [PK_answers] PRIMARY KEY CLUSTERED 
(
	[id] ASC
)WITH (PAD_INDEX  = OFF, STATISTICS_NORECOMPUTE  = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS  = ON, ALLOW_PAGE_LOCKS  = ON) ON [PRIMARY]
) ON [PRIMARY]

GO

ALTER TABLE [dbo].[answers]  WITH CHECK ADD  CONSTRAINT [FK_answers_questions] FOREIGN KEY([questionId])
REFERENCES [dbo].[questions] ([id])
GO

ALTER TABLE [dbo].[answers] CHECK CONSTRAINT [FK_answers_questions]
GO

ALTER TABLE [dbo].[answers]  WITH CHECK ADD  CONSTRAINT [FK_answers_topics] FOREIGN KEY([topicsId])
REFERENCES [dbo].[topics] ([id])
ON UPDATE CASCADE
ON DELETE CASCADE
GO

ALTER TABLE [dbo].[answers] CHECK CONSTRAINT [FK_answers_topics]
GO

