curl -X POST --user roy:1234 `
-H 'Content-Type: multipart/form-data' `
-F 'name=roy'`
-F 'project=25'`
-F 'data=@C:\Users\Roy\djangoProjects\djangoApi\myapi\scripts_requests\api_get_list.py' `
http://localhost:8000/api/mlmodels/