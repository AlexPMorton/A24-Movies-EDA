SELECT title, release_date, genre, director, budget, domestic_revenue,
international_revenue, worldwide_revenue, runtime, mpaa_rating,
CASE WHEN film IS NOT NULL AND film <> 'Skin' THEN 'YES' ELSE 'NO' END AS oscar_win
FROM (
	SELECT * 
	FROM a24_released_movies arm 
	LEFT JOIN academy_award_winners aaw
		ON arm.title = aaw.film 
	) AS a24_oscars	
ORDER BY title;