/*
 Problem: https://www.codewars.com/kata/64f04aeeab2583003c819b1e/train/sql

 Instructions:
    Write a SQL query to achieve the following:

        Return a list of genres.
        Count the number of books in each genre.
        List titles of the books in each genre as an array. The titles within this array should be sorted alphabetically.
        The output should be ordered by the number of books in each genre in descending order, and then alphabetically by genre name for genres with the same book count.
*/

SELECT 
  genre,
  count(genre) AS count,
  array_agg(title ORDER BY title) AS books
FROM
  (
    SELECT
      unnest(genres) AS genre,
      title
    FROM
      books
  ) AS genre_to_books
GROUP BY
  genre
ORDER BY
  count DESC,
  genre


/*
Notes:
    -- Learned about the UNNEST method in PostgreSQL : used to break a list/array into parts and returns a record set in the form:
        Initial columns:
        
        title1  //  title2
        column1 // {array1, array2, array3}
        column2 // {array1, array2}

        SELECT unnest(title2) AS title2s
            =>

        array1
        array2
        array3
        array1
        array2

Results:
    -- FAILED: (18 minutes of trying)