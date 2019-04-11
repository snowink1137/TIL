from mton.models import Student, Lecture, Enrollment

create_student = Student.object.create
s1 = create_student(name='이종화')
s2 = create_student(name='고재두')
s3 = create_student(name='박병준')

l1 = Lecture.objects.create(title='컴개')
l2 = Lecture.objects.create(title='자료구조')
l3 = Lecture.objects.create(title='알고리즘')

Enrollment.objects.create(lecture=l1, student=s1)
Enrollment.objects.create(lecture=l1, student=s2)
Enrollment.objects.create(lecture=l1, student=s3)

이종화 = Student.objects.get(id=1)
이종화의_수강신청_목록 = 이종화.enrollment_set.all()
for 수강신청 in 이종화의_수강신청_목록:
    print(수강신청.lecture.title)



