import aiosqlite

DATABASE = 'djangobot/db.sqlite3'
MEDIA_FOLDER = 'djangobot/media'


async def save_resume_data(data):
    async with aiosqlite.connect(DATABASE) as db:
        await db.execute(
            """
            INSERT INTO main_resume (
                first_name, last_name, middle_name, gender, birthday, education, 
                education_place, family_status, specialty, region, district, address, 
                branch_desire, post, experience, worked_before, phone, extra_phone, 
                shirt_size, is_studying, education_type, languages, work_experience, 
                programms_experience, about, salary, is_familiar_works_here, 
                is_uzbek_citizen, is_working_now, from_vacancy_info, face_photo
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                data.get('first_name'), data.get('last_name'), data.get('middle_name'), data.get('gender'),
                data.get('birthday'), data.get('education'), data.get('education_place'), data.get('family_status'),
                data.get('specialty'), data.get('region'), data.get('district'), data.get('address'),
                data.get('branch_desire'), data.get('post'), data.get('experience'), data.get('worked_before'),
                data.get('phone'), data.get('extra_phone'), data.get('shirt_size'), data.get('is_studying'),
                data.get('education_type'), ",".join(data.get('languages', [])), data.get('work_experience'),
                ",".join(data.get('programms_experience', [])), data.get('about'), data.get('salary'),
                data.get('is_familiar_works_here'), data.get('is_uzbek_citizen'), data.get('is_working_now'),
                data.get('from_vacancy_info'), data.get('face_photo').replace('djangobot/media/', '')
            )
        )
        await db.commit()


async def get_branch():
    async with aiosqlite.connect(DATABASE) as db:
        async with db.execute("SELECT name FROM main_branch") as cursor:
            names = await cursor.fetchall()
            return [name[0] for name in names]


async def get_post():
    async with aiosqlite.connect(DATABASE) as db:
        async with db.execute("SELECT name FROM main_post") as cursor:
            names = await cursor.fetchall()
            return [name[0] for name in names]


async def get_vacancy_info():
    async with aiosqlite.connect(DATABASE) as db:
        async with db.execute("SELECT name FROM main_vacancyinfo") as cursor:
            names = await cursor.fetchall()
            return [name[0] for name in names]


async def get_chat_ids():
    async with aiosqlite.connect(DATABASE) as db:
        async with db.execute("SELECT chat_id FROM main_chat") as cursor:
            names = await cursor.fetchall()
            return [name[0] for name in names]
