-- list all shows
-- in tv shows
SELECT tv_shows.title AS title, tv_show_genres.genre_id AS genre_id
FROM tv_show_genres
WHERE genre_id IS NULL
RIGHT JOIN tv_shows ON tv_show_genres.show_id=tv_shows.id
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;