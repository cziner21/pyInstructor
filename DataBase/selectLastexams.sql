SELECT   u.id,
         concat(lastName,' ',firstName) as fullName, email,
         _subQuery.result,_subQuery.lastExam,t.name as TopicName
FROM users u inner join  (SELECT  id, userId as subUser, topicId as subTopic,result,
                  MAX(examDate) as lastExam
         FROM     results
         GROUP BY id
         ORDER BY MAX(examDate) DESC
         
         )
         _subQuery
         on _subQuery.subUser = u.id
inner join topics t on t.id = _subQuery.subTopic

where 1 = 1

group by u.id