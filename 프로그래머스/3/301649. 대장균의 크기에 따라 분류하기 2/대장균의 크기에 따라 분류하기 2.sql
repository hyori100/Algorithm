-- 코드를 작성해주세요
SELECT ID, 
    (case 
        when PER <=  0.25 then 'CRITICAL'
        when PER <=  0.5 then 'HIGH' 
        when PER <=  0.75 then 'MEDIUM' 
        else 'LOW'
    end) as COLONY_NAME
FROM (
    select 
        ID, 
        PERCENT_RANK() OVER (ORDER BY SIZE_OF_COLONY DESC) AS PER
    from ECOLI_DATA) as p
ORDER BY ID;