select APNT_NO, PT_NAME, c.PT_NO, a.MCDP_CD, DR_NAME, APNT_YMD from APPOINTMENT as a
join DOCTOR as b
on a.MDDR_ID = b.DR_ID
join PATIENT as c
on a.PT_NO = c.PT_NO
where APNT_YMD like '2022-04-13%' and b.MCDP_CD = 'CS'
and APNT_CNCL_YN = 'N'
order by APNT_YMD;