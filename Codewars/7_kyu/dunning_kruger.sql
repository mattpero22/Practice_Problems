/*
 Problem: https://www.codewars.com/kata/649f1fc4771a460058981959/train/sql

 Instructions:
    Your task is to write an SQL query that does the following:
        Selects only those users where the perceived skill level is greater than the actual skill level.
        For each of these users, calculates the difference between the perceived skill level and actual skill level as "skill_overestimation".
        Adds a "overconfidence_category" message based on the degree of skill overestimation*
            'Mild case of overconfidence': skill overestimation is 2 or less
            'Moderate case of overconfidence': skill overestimation is greater than 2 and up to 5
            'Serious case of overconfidence': skill overestimation is greater than 5 and up to 7
            'Extreme case of Dunning-Kruger effect detected!': skill overestimation is more than 7

 Plan of Attack:
    1. access the users table and get all columns
    2. add an additonal column to the result RS with the skill_overestimation category
    3. add a conditional column of IF, ELSE IF, ELSE based on the skill_overestimation result
*/


SELECT 
  o.id,
  o.name,
  o.skill_overestimation,
  CASE 
    WHEN o.skill_overestimation <= 2 THEN 'Mild case of overconfidence'
    WHEN o.skill_overestimation > 2 AND o.skill_overestimation <= 5 THEN 'Moderate case of overconfidence'
    WHEN o.skill_overestimation > 5 AND o.skill_overestimation <= 7 THEN 'Serious case of overconfidence'
    WHEN o.skill_overestimation > 7 THEN 'Extreme case of Dunning-Kruger effect detected!'
  END as overconfidence_category
FROM (
  SELECT
      *,
      u.perceived_skill_level - u.actual_skill_level AS skill_overestimation
  FROM
      users u
) as o
WHERE 
  o.skill_overestimation > 0
ORDER BY
  o.skill_overestimation DESC, o.id DESC

/*
Notes:
    -- Needed to look up the syntax of the Case statement with POSTGRES SQL (initially tried IF ELSE)
    -- Got stuck on the ORDER BY. Then I realized I needed to do DESC after each, rather than both columns followed by a single DESC clause
    -- Could have done without the inner subquery which I felt complicated things. Reviewed other solutions and see that I could have calculated my skill_overestimation column in the inital RS

Results:
    -- COMPLETED: 25 minutes
*/