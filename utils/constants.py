from fastapi.security import OAuth2PasswordBearer
#constants here

users = 'users'
users_description = 'User routes'

areas = 'areas'
areas_description = 'Area routes'

survey = 'survey'
survey_description = 'Survey routes'

survey_area = 'survey_area'
survey_area_description = 'Survey area routes'

survey_answer = 'survey_answer'
survey_answer_description = 'Survey answer routes'

#OAuth2
ouath2_scheme = OAuth2PasswordBearer(tokenUrl="token")