SELECT s1.Score AS Score, (SELECT COUNT(DISTINCT S2.Score) FROM Scores as S2 WHERE S2.Score > S1.Score)+1 AS Rank
FROM Scores AS s1
ORDER BY Rank 