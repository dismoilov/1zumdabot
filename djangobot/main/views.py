from .models import Resume
from datetime import datetime


def save_resume(data):
    data['languages'] = ', '.join(data.get('languages', []))
    data['programms_experience'] = ', '.join(data.get('programms_experience', []))

    try:
        data['birthday'] = datetime.strptime(data['birthday'], "%d.%m.%Y").date()
    except ValueError:
        data['birthday'] = None

    photo_file = data.get('face_photo')

    resume = Resume(
        first_name=data['first_name'],
        last_name=data['last_name'],
        middle_name=data.get('middle_name', ''),
        gender=data['gender'],
        birthday=data['birthday'],
        education=data['education'],
        education_place=data['education_place'],
        family_status=data['family_status'],
        specialty=data['specialty'],
        region=data['region'],
        district=data['district'],
        address=data['address'],
        branch_desire=data['branch_desire'],
        post=data['post'],
        experience=data['experience'],
        worked_before=data['worked_before'],
        phone=data['phone'],
        extra_phone=data.get('extra_phone', ''),
        shirt_size=data['shirt_size'],
        is_studying=data['is_studying'],
        education_type=data['education_type'],
        languages=data['languages'],
        work_experience=data['work_experience'],
        programms_experience=data['programms_experience'],
        about=data['about'],
        salary=data.get('salary', 0),
        is_familiar_works_here=data['is_familiar_works_here'],
        is_uzbek_citizen=data['is_uzbek_citizen'],
        is_working_now=data['is_working_now'],
        from_vacancy_info=data['from_vacancy_info'],
        face_photo=photo_file
    )
    resume.save()
    return resume
