USE [szakdolgozat]
GO

/****** Object:  Table [dbo].[profils]    Script Date: 11/03/2014 06:40:39 ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE TABLE [dbo].[profils](
	[id] [int] IDENTITY(1,1) NOT NULL,
	[country] [nvarchar](255) NULL,
	[city] [nvarchar](255) NULL,
	[address] [nvarchar](255) NULL,
	[phone] [nvarchar](100) NULL,
	[profilPictureURL] [nvarchar](max) NULL,
	[userId] [int] NOT NULL,
 CONSTRAINT [PK_profils] PRIMARY KEY CLUSTERED 
(
	[id] ASC
)WITH (PAD_INDEX  = OFF, STATISTICS_NORECOMPUTE  = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS  = ON, ALLOW_PAGE_LOCKS  = ON) ON [PRIMARY]
) ON [PRIMARY]

GO

ALTER TABLE [dbo].[profils]  WITH CHECK ADD  CONSTRAINT [FK_profils_users] FOREIGN KEY([userId])
REFERENCES [dbo].[users] ([id])
ON UPDATE CASCADE
ON DELETE CASCADE
GO

ALTER TABLE [dbo].[profils] CHECK CONSTRAINT [FK_profils_users]
GO

