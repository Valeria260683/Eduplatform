from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class UserAnnotation:
    password: str
    first_name: str
    last_name: str
    email: str


@dataclass(frozen=True, slots=True)
class TeacherAnnotation:
    user: UserAnnotation
    experience: int


@dataclass(frozen=True, slots=True)
class StudentAnnotation:
    user: UserAnnotation
    rating: int
    age: int


@dataclass(frozen=True, slots=True)
class CourseAnnotation:
    name: str
    teacher: TeacherAnnotation
    price: int


@dataclass(frozen=True, slots=True)
class GroupAnnotation:
    group_name: str
    teacher: TeacherAnnotation
    student: list[StudentAnnotation]
    course: CourseAnnotation


@dataclass(frozen=True, slots=True)
class TopicAnnotation:
    name: str
    course: CourseAnnotation
    content: str


@dataclass(frozen=True, slots=True)
class ArticleAnnotation:
    title: str
    topic: TopicAnnotation
    teacher: TeacherAnnotation
    content: str
