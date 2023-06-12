CNproperty = ["knowledge_id","title","cloud_service","product_name","detail","error_message","environment","category","reference","incident_number","problem_number","user_name","division_name","ts_system_name","registration_date"]
    

SQL_FIRST="""WITH SearchTable(knowledge_id, error_message, title, detail, cloud_service, product_name) AS (
SELECT knowledge_table.knowledge_id, knowledge_table.error_message, knowledge_table.title, knowledge_table.detail, 
product_mateview.cloud_service, product_mateview.product_name 
FROM knowledge_table 
LEFT OUTER JOIN product_mateview ON knowledge_table.knowledge_id = product_mateview.knowledge_id), 
resultID(knowledge_id) AS (
SELECT SearchTable.knowledge_id 
FROM SearchTable """

SQL_SECOND="""), 
all_table (knowledge_id,title,cloud_service,product_name,detail,error_message, environment,category,
reference,incident_number,problem_number,user_name,division_name,ts_system_name,registration_date)
AS (
SELECT knowledge_table.knowledge_id, knowledge_table.title, product_mateview.cloud_service, product_mateview.product_name, 
knowledge_table.detail, knowledge_table.error_message, environment_table.environment, 
category_mateview.category, reference_mateview.reference, 
knowledge_table.incident_number, knowledge_table.problem_number, knowledge_table.user_name, 
division_table.division_name, ts_system_table.ts_system_name ,knowledge_table.registration_date 
FROM knowledge_table 
LEFT OUTER JOIN environment_table ON knowledge_table.environment_id = environment_table.environment_id
LEFT OUTER JOIN category_mateview ON knowledge_table.knowledge_id = category_mateview.knowledge_id 
LEFT OUTER JOIN reference_mateview ON knowledge_table.knowledge_id = reference_mateview.knowledge_id 
LEFT OUTER JOIN product_mateview ON knowledge_table.knowledge_id = product_mateview.knowledge_id 
LEFT OUTER JOIN division_table ON knowledge_table.division_id = division_table.division_id 
LEFT OUTER JOIN ts_system_table ON knowledge_table.ts_system_id = ts_system_table.ts_system_id
) 
SELECT all_table.knowledge_id, all_table.title, all_table.cloud_service, all_table.product_name, 
all_table.detail, all_table.error_message, all_table.environment, 
all_table.category, all_table.reference, 
all_table.incident_number, all_table.problem_number, all_table.user_name, 
all_table.division_name, all_table.ts_system_name, all_table.registration_date FROM resultID 
LEFT OUTER JOIN all_table ON all_table.knowledge_id = resultID.knowledge_id 
order by resultID.knowledge_id"""