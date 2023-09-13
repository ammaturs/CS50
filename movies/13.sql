--list the names of all people who starred in a movie in which Kevin Bacon also starred
-- maybe lets try getting a list of the movies which kevin beacons in, then from there say who else is in those movies
SELECT DISTINCT name
FROM people
JOIN stars ON people.id = stars.person_id
JOIN movies ON stars.movie_id = movies.id
WHERE movies.title IN (
    SELECT movies.title
    FROM movies
    JOIN stars ON movies.id = stars.movie_id
    JOIN people ON stars.person_id = people.id
    WHERE people.name = 'Kevin Bacon'
    AND people.birth = '1958')
    AND people.name != 'Kevin Bacon';
