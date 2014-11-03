USE [szakdolgozat]
GO

/****** Object:  View [dbo].[userResultsWithoutProfil]    Script Date: 10/25/2014 13:48:51 ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE VIEW [dbo].[userResultsWithoutProfil]
AS
SELECT     dbo.exams.examDate, dbo.results.result, dbo.topics.name, dbo.users.firstName, dbo.users.lastName, 
                      dbo.users.firstName + ' ' + dbo.users.lastName AS fullName
FROM         dbo.answers INNER JOIN
                      dbo.correctAnswers AS ca ON dbo.answers.id = ca.id INNER JOIN
                      dbo.exams ON dbo.answers.id = dbo.exams.id INNER JOIN
                      dbo.exams_users_conn AS euc ON dbo.exams.id = euc.examId INNER JOIN
                      dbo.questions ON dbo.answers.questionId = dbo.questions.id AND ca.questionId = dbo.questions.id INNER JOIN
                      dbo.results ON dbo.exams.id = dbo.results.examId INNER JOIN
                      dbo.topics ON dbo.questions.topicId = dbo.topics.id INNER JOIN
                      dbo.topics_exams_conn AS tec ON dbo.exams.id = tec.examId AND dbo.topics.id = tec.topicId INNER JOIN
                      dbo.userAnswers AS ua ON dbo.answers.id = ua.answerId AND dbo.questions.id = ua.questionId INNER JOIN
                      dbo.users ON euc.userId = dbo.users.id

GO

EXEC sys.sp_addextendedproperty @name=N'MS_DiagramPane1', @value=N'[0E232FF0-B466-11cf-A24F-00AA00A3EFFF, 1.00]
Begin DesignProperties = 
   Begin PaneConfigurations = 
      Begin PaneConfiguration = 0
         NumPanes = 4
         Configuration = "(H (1[28] 4[36] 2[18] 3) )"
      End
      Begin PaneConfiguration = 1
         NumPanes = 3
         Configuration = "(H (1 [50] 4 [25] 3))"
      End
      Begin PaneConfiguration = 2
         NumPanes = 3
         Configuration = "(H (1 [50] 2 [25] 3))"
      End
      Begin PaneConfiguration = 3
         NumPanes = 3
         Configuration = "(H (4 [30] 2 [40] 3))"
      End
      Begin PaneConfiguration = 4
         NumPanes = 2
         Configuration = "(H (1 [56] 3))"
      End
      Begin PaneConfiguration = 5
         NumPanes = 2
         Configuration = "(H (2 [66] 3))"
      End
      Begin PaneConfiguration = 6
         NumPanes = 2
         Configuration = "(H (4 [50] 3))"
      End
      Begin PaneConfiguration = 7
         NumPanes = 1
         Configuration = "(V (3))"
      End
      Begin PaneConfiguration = 8
         NumPanes = 3
         Configuration = "(H (1[56] 4[18] 2) )"
      End
      Begin PaneConfiguration = 9
         NumPanes = 2
         Configuration = "(H (1 [75] 4))"
      End
      Begin PaneConfiguration = 10
         NumPanes = 2
         Configuration = "(H (1[66] 2) )"
      End
      Begin PaneConfiguration = 11
         NumPanes = 2
         Configuration = "(H (4 [60] 2))"
      End
      Begin PaneConfiguration = 12
         NumPanes = 1
         Configuration = "(H (1) )"
      End
      Begin PaneConfiguration = 13
         NumPanes = 1
         Configuration = "(V (4))"
      End
      Begin PaneConfiguration = 14
         NumPanes = 1
         Configuration = "(V (2))"
      End
      ActivePaneConfig = 0
   End
   Begin DiagramPane = 
      Begin Origin = 
         Top = 0
         Left = 0
      End
      Begin Tables = 
         Begin Table = "answers"
            Begin Extent = 
               Top = 6
               Left = 38
               Bottom = 110
               Right = 198
            End
            DisplayFlags = 280
            TopColumn = 0
         End
         Begin Table = "ca"
            Begin Extent = 
               Top = 6
               Left = 236
               Bottom = 95
               Right = 396
            End
            DisplayFlags = 280
            TopColumn = 0
         End
         Begin Table = "exams"
            Begin Extent = 
               Top = 6
               Left = 434
               Bottom = 95
               Right = 594
            End
            DisplayFlags = 280
            TopColumn = 0
         End
         Begin Table = "euc"
            Begin Extent = 
               Top = 6
               Left = 632
               Bottom = 95
               Right = 792
            End
            DisplayFlags = 280
            TopColumn = 0
         End
         Begin Table = "questions"
            Begin Extent = 
               Top = 96
               Left = 236
               Bottom = 200
               Right = 396
            End
            DisplayFlags = 280
            TopColumn = 0
         End
         Begin Table = "results"
            Begin Extent = 
               Top = 96
               Left = 434
               Bottom = 200
               Right = 594
            End
            DisplayFlags = 280
            TopColumn = 0
         End
         Begin Table = "topics"
            Begin Extent = 
               Top = 96
               Left = 632
               Bottom = 185
               Right = 792
            End
            DisplayFlags = 280
            TopCo' , @level0type=N'SCHEMA',@level0name=N'dbo', @level1type=N'VIEW',@level1name=N'userResultsWithoutProfil'
GO

EXEC sys.sp_addextendedproperty @name=N'MS_DiagramPane2', @value=N'lumn = 0
         End
         Begin Table = "tec"
            Begin Extent = 
               Top = 114
               Left = 38
               Bottom = 203
               Right = 198
            End
            DisplayFlags = 280
            TopColumn = 0
         End
         Begin Table = "ua"
            Begin Extent = 
               Top = 186
               Left = 632
               Bottom = 290
               Right = 792
            End
            DisplayFlags = 280
            TopColumn = 0
         End
         Begin Table = "users"
            Begin Extent = 
               Top = 204
               Left = 38
               Bottom = 323
               Right = 198
            End
            DisplayFlags = 280
            TopColumn = 0
         End
      End
   End
   Begin SQLPane = 
   End
   Begin DataPane = 
      Begin ParameterDefaults = ""
      End
      Begin ColumnWidths = 28
         Width = 284
         Width = 1500
         Width = 1500
         Width = 1500
         Width = 1500
         Width = 1500
         Width = 1500
         Width = 1500
         Width = 1500
         Width = 1500
         Width = 1500
         Width = 1500
         Width = 1500
         Width = 1500
         Width = 1500
         Width = 1500
         Width = 1500
         Width = 1500
         Width = 1500
         Width = 1500
         Width = 1500
         Width = 1500
         Width = 1500
         Width = 1500
         Width = 1500
         Width = 1500
         Width = 1500
         Width = 1500
      End
   End
   Begin CriteriaPane = 
      Begin ColumnWidths = 11
         Column = 2040
         Alias = 900
         Table = 1170
         Output = 720
         Append = 1400
         NewValue = 1170
         SortType = 1350
         SortOrder = 1410
         GroupBy = 1350
         Filter = 1350
         Or = 1905
         Or = 1350
         Or = 1350
      End
   End
End
' , @level0type=N'SCHEMA',@level0name=N'dbo', @level1type=N'VIEW',@level1name=N'userResultsWithoutProfil'
GO

EXEC sys.sp_addextendedproperty @name=N'MS_DiagramPaneCount', @value=2 , @level0type=N'SCHEMA',@level0name=N'dbo', @level1type=N'VIEW',@level1name=N'userResultsWithoutProfil'
GO

