CREATE TABLE FINAL_TABLE AS
SELECT users.user_id AS 'User ID', users.country AS 'Country', job_titles.job_title AS 'Job Titles', addresses.street_address AS 'Street Address'
FROM users
INNER JOIN
job_titles
ON users.user_id=job_titles.user_id
INNER JOIN
addresses
ON users.user_id=job_titles.user_id;
