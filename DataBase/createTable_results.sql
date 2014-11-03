USE [szakdolgozat]
GO

/****** Object:  Table [dbo].[results]    Script Date: 10/25/2014 12:46:04 ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE TABLE [dbo].[results](
	[id] [int] IDENTITY(1,1) NOT NULL,
	[result] [int] NOT NULL,
	[examId] [int] NOT NULL,
 CONSTRAINT [PK_results] PRIMARY KEY CLUSTERED 
(
	[id] ASC
)WITH (PAD_INDEX  = OFF, STATISTICS_NORECOMPUTE  = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS  = ON, ALLOW_PAGE_LOCKS  = ON) ON [PRIMARY]
) ON [PRIMARY]

GO

ALTER TABLE [dbo].[results]  WITH CHECK ADD  CONSTRAINT [FK_results_exams] FOREIGN KEY([examId])
REFERENCES [dbo].[exams] ([id])
ON UPDATE CASCADE
ON DELETE CASCADE
GO

ALTER TABLE [dbo].[results] CHECK CONSTRAINT [FK_results_exams]
GO

