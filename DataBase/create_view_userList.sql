CREATE VIEW UserList
   AS
  SELECT u.id,concat(lastName,' ',firstName) as fullName, email, city, address, phone, birthday, registered, privilidge
  FROM users u
  inner join profil p ON p.userId = u.id