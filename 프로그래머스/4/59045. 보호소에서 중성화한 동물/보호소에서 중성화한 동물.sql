-- 코드를 입력하세요
SELECT A.ANIMAL_ID, A.ANIMAL_TYPE, A.NAME 
FROM ANIMAL_OUTS AS A
join ANIMAL_INS as b
on a.ANIMAL_ID = b.ANIMAL_ID 
where (SEX_UPON_OUTCOME like 'Spayed%' or SEX_UPON_OUTCOME like 'Neutered%')
and SEX_UPON_INTAKE like 'Intact%';