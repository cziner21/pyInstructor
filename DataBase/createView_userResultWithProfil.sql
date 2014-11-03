USE [szakdolgozat]
GO

/****** Object:  View [dbo].[userResultsWithProfil]    Script Date: 10/25/2014 13:49:01 ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE VIEW [dbo].[userResultsWithProfil]
AS
SELECT     dbo.exams.examDate, dbo.profils.country, dbo.profils.city, dbo.results.result, dbo.topics.name, dbo.users.firstName, dbo.users.lastName, 
                      dbo.users.firstName + ' ' + dbo.users.lastName AS fullName
FROM         dbo.answers INNER JOIN
                      dbo.correctAnswers ON dbo.answers.id = dbo.correctAnswers.id INNER JOIN
                      dbo.exams ON dbo.answers.id = dbo.exams.id INNER JOIN
                      dbo.exams_users_conn ON dbo.exams.id = dbo.exams_users_conn.examId INNER JOIN
                      dbo.profils ON dbo.answers.id = dbo.profils.id INNER JOIN
                      dbo.questions ON dbo.answers.questionId = dbo.questions.id AND dbo.correctAnswers.questionId = dbo.questions.id INNER JOIN
                      dbo.results ON dbo.exams.id = dbo.results.examId INNER JOIN
                      dbo.results_topics_conn ON dbo.results.id = dbo.results_topics_conn.resultId INNER JOIN
                      dbo.topics ON dbo.questions.topicId = dbo.topics.id AND dbo.results_topics_conn.topicsId = dbo.topics.id INNER JOIN
                      dbo.topics_exams_conn ON dbo.exams.id = dbo.topics_exams_conn.examId AND dbo.topics.id = dbo.topics_exams_conn.topicId INNER JOIN
                      dbo.userAnswers ON dbo.answers.id = dbo.userAnswers.answerId AND dbo.questions.id = dbo.userAnswers.questionId INNER JOIN
                      dbo.users ON dbo.exams_users_conn.userId = dbo.users.id AND dbo.profils.userId = dbo.users.id INNER JOIN
                      dbo.users_results_conn ON dbo.results.id = dbo.users_results_conn.resultId AND dbo.users.id = dbo.users_results_conn.userId

GO

EXEC sys.sp_addextendedproperty @name=N'MS_DiagramPane1', @value=N'[0E232FF0-B466-11cf-A24F-00AA00A3EFFF, 1.00]
Begin DesignProperties = 
   Begin PaneConfigurations = 
      Begin PaneConfiguration = 0
         NumPanes = 4
         Configuration = "(H (1[41] 4[34] 2[7] 3) )"
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
         Begin Table = "correctAnswers"
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
         Begin Table = "exams_users_conn"
            Begin Extent = 
               Top = 6
               Left = 632
               Bottom = 95
               Right = 792
            End
            DisplayFlags = 280
            TopColumn = 0
         End
         Begin Table = "profils"
            Begin Extent = 
               Top = 96
               Left = 236
               Bottom = 215
               Right = 401
            End
            DisplayFlags = 280
            TopColumn = 0
         End
         Begin Table = "questions"
            Begin Extent = 
               Top = 96
               Left = 439
               Bottom = 200
               Right = 599
            End
            DisplayFlags = 280
            TopColumn = 0
         End
         Begin Table = "results"
            Begin Extent = 
               Top = 96
               Left = 637
               Bottom = 200
               Right = 797
            End
            DisplayFlags' , @level0type=N'SCHEMA',@level0name=N'dbo', @level1type=N'VIEW',@level1name=N'userResultsWithProfil'
GO

EXEC sys.sp_addextendedproperty @name=N'MS_DiagramPane2', @value=N' = 280
            TopColumn = 0
         End
         Begin Table = "results_topics_conn"
            Begin Extent = 
               Top = 114
               Left = 38
               Bottom = 203
               Right = 198
            End
            DisplayFlags = 280
            TopColumn = 0
         End
         Begin Table = "topics"
            Begin Extent = 
               Top = 204
               Left = 38
               Bottom = 293
               Right = 198
            End
            DisplayFlags = 280
            TopColumn = 0
         End
         Begin Table = "topics_exams_conn"
            Begin Extent = 
               Top = 204
               Left = 439
               Bottom = 293
               Right = 599
            End
            DisplayFlags = 280
            TopColumn = 0
         End
         Begin Table = "userAnswers"
            Begin Extent = 
               Top = 204
               Left = 637
               Bottom = 308
               Right = 797
            End
            DisplayFlags = 280
            TopColumn = 0
         End
         Begin Table = "users"
            Begin Extent = 
               Top = 216
               Left = 236
               Bottom = 335
               Right = 396
            End
            DisplayFlags = 280
            TopColumn = 0
         End
         Begin Table = "users_results_conn"
            Begin Extent = 
               Top = 294
               Left = 38
               Bottom = 383
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
      Begin ColumnWidths = 39
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
         Column = 1440
         Alias = 900
         Table = 1170
         Output = 720
         Append = 1400
         NewValue = 1170
         SortType = 1350
         SortOrder = 1410
         GroupBy = 1350
         Filter = 1350
         Or = 1350
         Or = 1350
         Or = 1350
      End
   End
End
' , @level0type=N'SCHEMA',@level0name=N'dbo', @level1type=N'VIEW',@level1name=N'userResultsWithProfil'
GO

EXEC sys.sp_addextendedproperty @name=N'MS_DiagramPaneCount', @value=2 , @level0type=N'SCHEMA',@level0name=N'dbo', @level1type=N'VIEW',@level1name=N'userResultsWithProfil'
GO

