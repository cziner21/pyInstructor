USE [szakdolgozat]
GO

/****** Object:  Table [dbo].[exams]    Script Date: 11/03/2014 06:40:32 ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE TABLE [dbo].[exams](
	[id] [int] IDENTITY(1,1) NOT NULL,
	[examDate] [datetime] NOT NULL,
	[topicsId] [int] NOT NULL,
 CONSTRAINT [PK_exams] PRIMARY KEY CLUSTERED 
(
	[id] ASC
)WITH (PAD_INDEX  = OFF, STATISTICS_NORECOMPUTE  = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS  = ON, ALLOW_PAGE_LOCKS  = ON) ON [PRIMARY]
) ON [PRIMARY]

GO

ALTER TABLE [dbo].[exams]  WITH CHECK ADD  CONSTRAINT [FK_exams_topics] FOREIGN KEY([topicsId])
REFERENCES [dbo].[topics] ([id])
ON UPDATE CASCADE
ON DELETE CASCADE
GO

ALTER TABLE [dbo].[exams] CHECK CONSTRAINT [FK_exams_topics]
GO

