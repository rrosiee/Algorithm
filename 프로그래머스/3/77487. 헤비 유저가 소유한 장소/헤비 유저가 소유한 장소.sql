-- 공간을 둘 이상 등록한 사람을 헤비 유저라고 부른다.
-- 헤비 유저가 등록한 공간의 정보를 아이디 순으로 조회하는 SQL문

SELECT ID, NAME, HOST_ID
FROM PLACES
WHERE HOST_ID in (SELECT HOST_ID FROM PLACES GROUP BY HOST_ID HAVING COUNT(ID) >= 2)
ORDER BY ID ASC;

