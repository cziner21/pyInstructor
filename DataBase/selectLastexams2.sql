SELECT   u.id,concat(lastName,' ',firstName) as fullName, email, _subQuery.result, _subQuery.lastExam, t.name as TopicName from (SELECT  id, userId as subUser, topicId as subTopic,result,
                  MAX(examDate) as lastExam
         FROM     results
         GROUP BY subUser
         ORDER BY MAX(examDate) DESC
         
         )
         _subQuery
         left outer join users u
         on u.id =_subQuery.subUser 
inner join topics t on _subQuery.subTopic = t.id 

where 1 = 1

group by u.id