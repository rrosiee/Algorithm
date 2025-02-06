-- USED_GOODS_BOARD: 중고거래 게시판 정보(BOARD_ID, WRITER, TITLE, CONTENTS, PRICE, CREATED_DATE, STATUS, VIEWS)
-- USED_GOODS_REPLY : 중고거래 게시판 첨부파일 정보 (REPLY_ID, BOARD_ID, WRITER_ID, CONTENTS, CREATED_DATE)


SELECT A.TITLE, A.BOARD_ID, B.REPLY_ID, B.WRITER_ID, B.CONTENTS, DATE_FORMAT(B.CREATED_DATE, '%Y-%m-%d') AS CREATED_DATE
FROM USED_GOODS_BOARD AS A
INNER JOIN USED_GOODS_REPLY AS B
ON A.BOARD_ID = B.BOARD_ID
WHERE SUBSTR(A.CREATED_DATE, 1, 7) = '2022-10'
ORDER BY B.CREATED_DATE ASC, A.TITLE ASC;