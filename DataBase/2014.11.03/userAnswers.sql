USE [szakdolgozat]
GO

/****** Object:  Table [dbo].[userAnswers]    Script Date: 11/03/2014 06:41:23 ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE TABLE [dbo].[userAnswers](
	[id] [int] IDENTITY(1,1) NOT NULL,
	[answerId] [int] NOT NULL,
	[topicsId] [int] NOT NULL,
	[questionId] [int] NOT NULL,
 CONSTRAINT [PK_userAnswers] PRIMARY KEY CLUSTERED 
(
	[id] ASC
)WITH (PAD_INDEX  = OFF, STATISTICS_NORECOMPUTE  = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS  = ON, ALLOW_PAGE_LOCKS  = ON) ON [PRIMARY]
) ON [PRIMARY]

GO

ALTER TABLE [dbo].[userAnswers]  WITH CHECK ADD  CONSTRAINT [FK_userAnswers_answers] FOREIGN KEY([answerId])
REFERENCES [dbo].[answers] ([id])
ON UPDATE CASCADE
ON DELETE CASCADE
GO

ALTER TABLE [dbo].[userAnswers] CHECK CONSTRAINT [FK_userAnswers_answers]
GO

ALTER TABLE [dbo].[userAnswers]  WITH CHECK ADD  CONSTRAINT [FK_userAnswers_questions] FOREIGN KEY([questionId])
REFERENCES [dbo].[questions] ([id])
GO

ALTER TABLE [dbo].[userAnswers] CHECK CONSTRAINT [FK_userAnswers_questions]
GO

ALTER TABLE [dbo].[userAnswers]  WITH CHECK ADD  CONSTRAINT [FK_userAnswers_topics] FOREIGN KEY([topicsId])
REFERENCES [dbo].[topics] ([id])
GO

ALTER TABLE [dbo].[userAnswers] CHECK CONSTRAINT [FK_userAnswers_topics]
GO

