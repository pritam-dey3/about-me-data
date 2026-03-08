from pydantic import BaseModel, Field


class EducationItem(BaseModel):
    institution: str
    degree: str
    duration: str
    marks: str


class CourseItem(BaseModel):
    name: str
    platform: str
    certificate: str | None
    year: str


class EducationData(BaseModel):
    education: list[EducationItem]
    courses: list[CourseItem]


class ExperienceDuration(BaseModel):
    start: str
    end: str


class ExperienceItem(BaseModel):
    company: str
    role: str
    duration: ExperienceDuration
    responsibilities: list[str]


ExperienceData = list[ExperienceItem]


class OpenSourceItem(BaseModel):
    name: str
    description: str
    link: str


OpenSourceData = list[OpenSourceItem]


class ContactInformation(BaseModel):
    Email: str
    Phone_number: str | None = Field(None, alias="Phone number")


class SocialMediaProfiles(BaseModel):
    LinkedIn: str
    GitHub: str
    Twitter: str | None = None


class PersonalInformation(BaseModel):
    Name: str
    DOB: str
    Residing_location: str = Field(alias="Residing location")
    Nationality: str
    Languages: list[str]
    Hobbies: list[str] | None = None
    family: dict | None = None
    Contact_information: ContactInformation = Field(alias="Contact information")
    Social_media_profiles: SocialMediaProfiles = Field(alias="Social media profiles")
    Professional_summary: str = Field(alias="Professional summary")
    Skills_and_competencies: list[str] = Field(alias="Skills and competencies")


class Publication(BaseModel):
    description: str
    link: str


class PersonalData(BaseModel):
    description: str
    personal_information: PersonalInformation
    publications: Publication


class ProjectItem(BaseModel):
    project_id: str
    project_name: str
    description: str
    key_points: list[str]
    tech_stack: list[str]
    tags: list[str]
    organization: str
    duration: str


ProjectsData = list[ProjectItem]


class BlogItem(BaseModel):
    headline: str
    description: str
    link: str


BlogsData = list[BlogItem]
