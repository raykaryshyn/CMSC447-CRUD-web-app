from app import Student, db, app

with app.app_context():
    db.drop_all()
    db.create_all()

    '''
    Steve Smith	211	80
    Jian Wong	122	92
    Chris Peterson	213	91
    Sai Patel	524	94
    Andrew Whitehead	425	99
    Lynn Roberts	626	90
    Robert Sanders	287	75
    '''

    students = [
        {'name': 'Steven Smith', 'id': 211, 'score': 80},
        {'name': 'Jian Wong', 'id': 122, 'score': 92},
        {'name': 'Chris Peterson', 'id': 213, 'score': 91},
        {'name': 'Sai Patel', 'id': 524, 'score': 94},
        {'name': 'Andrew Whitehead', 'id': 425, 'score': 99},
        {'name': 'Lynn Roberts', 'id': 626, 'score': 90},
        {'name': 'Robert Sanders', 'id': 287, 'score': 75}
    ]

    db.session.bulk_save_objects([Student(student) for student in students])
    db.session.commit()
