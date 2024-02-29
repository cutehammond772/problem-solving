WITH TOTAL_GRADE (EMP_NO, TOTAL) AS (
    SELECT EMP_NO, SUM(SCORE)
    FROM HR_GRADE
    GROUP BY EMP_NO
)
SELECT a.TOTAL AS SCORE, b.EMP_NO, b.EMP_NAME, b.POSITION, b.EMAIL
FROM TOTAL_GRADE a, HR_EMPLOYEES b
WHERE 
    a.EMP_NO = b.EMP_NO
    AND a.TOTAL = (SELECT MAX(c.TOTAL) FROM TOTAL_GRADE c);