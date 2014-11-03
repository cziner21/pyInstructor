USE [szakdolgozat]
GO

/****** Object:  Table [dbo].[correctAnswers]    Script Date: 11/03/2014 06:40:22 ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE TABLE [dbo].[correctAnswers](
	[id] [int] IDENTITY(1,1) NOT NULL,
	[questionId] [int] NOT NULL,
	[answerId] [int] NOT NULL,
	[topicsId] [int] NOT NULL,
 CONSTRAINT [PK_correctAnswers] PRIMARY KEY CLUSTERED 
(
	[id] ASC
)WITH (PAD_INDEX  = OFF, STATISTICS_NORECOMPUTE  = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS  = ON, ALLOW_PAGE_LOCKS  = ON) ON [PRIMARY]
) ON [PRIMARY]

GO

ALTER TABLE [dbo].[correctAnswers]  WITH CHECK ADD  CONSTRAINT [FK_correctAnswers_answers] FOREIGN KEY([answerId])
REFERENCES [dbo].[answers] ([id])
ON UPDATE CASCADE
ON DELETE CASCADE
GO

ALTER TABLE [dbo].[correctAnswers] CHECK CONSTRAINT [FK_correctAnswers_answers]
GO

ALTER TABLE [dbo].[correctAnswers]  WITH CHECK ADD  CONSTRAINT [FK_correctAnswers_questions] FOREIGN KEY([questionId])
REFERENCES [dbo].[questions] ([id])
GO

ALTER TABLE [dbo].[correctAnswers] CHECK CONSTRAINT [FK_correctAnswers_questions]
GO

ALTER TABLE [dbo].[correctAnswers]  WITH CHECK ADD  CONSTRAINT [FK_correctAnswers_topics] FOREIGN KEY([topicsId])
REFERENCES [dbo].[topics] ([id])
GO

ALTER TABLE [dbo].[correctAnswers] CHECK CONSTRAINT [FK_correctAnswers_topics]
GO

