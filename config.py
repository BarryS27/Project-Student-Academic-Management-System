FILES = {
    'G9': 'G9.csv',
    'G10': 'G10.csv',
    'G11': 'G11.csv',
    'G12': 'G12.csv',
    'Self_Dev': 'Self_Dev.csv',
    'Dream_Schools': 'Dream_Schools.csv',
    'Dream_Majors': 'Dream_Majors.csv'
}



COLUMNS = {
    'Grades': ['Sem', 'Level', 'Code', 'Course', 'Weight', 'Q1_Points', 'Q2_Points', 'Q3_Points', 'Q4_Points'],
    'Self_Dev': ['Course', 'From', 'Skill', 'Status', 'Proficiency'],
    'Dream_Schools': ['University', 'School'],
    'Dream_Majors': ['Major']
}



TABLE_MAPPING = {
    'G9': 'Grades',
    'G10': 'Grades',
    'G11': 'Grades',
    'G12': 'Grades',
    'Self_Dev': 'Self_Dev',
    'Dream_Schools': 'Dream_Schools',
    'Dream_Majors': 'Dream_Majors'
}



NUMERIC_COLS = [
    'Weight', 'Q1_Points', 'Q2_Points', 'Q3_Points', 'Q4_Points', 'Proficiency'
]