-- list names of people who starred in Toy Story
-- join table of movie title with people
--people ID is unique & different than movies ID, need to use other tables to help filter


SELECT name
FROM people
JOIN stars ON people.id = stars.person_id
JOIN movies ON movies.id = stars.movie_id
WHERE movies.title = 'Toy Story';
