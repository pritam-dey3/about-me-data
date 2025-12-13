from typing import List, Optional, Any
from pydantic import BaseModel, Field

class EducationItem(BaseModel):
    institution: str
    degree: str
    duration: str
    marks: str

class CourseItem(BaseModel):
    name: str
    platform: str
    certificate: Optional[str]
    year: str

class EducationData(BaseModel):
    education: List[EducationItem]
    courses: List[CourseItem]

class ExperienceDuration(BaseModel):
    start: str
    end: str

class ExperienceItem(BaseModel):
    company: str
    role: str
    duration: ExperienceDuration
    responsibilities: List[str]

ExperienceData = List[ExperienceItem]

class OpenSourceItem(BaseModel):
    name: str
    description: str
    link: str

OpenSourceData = List[OpenSourceItem]

class ContactInformation(BaseModel):
    Email: str
    Phone_number: Optional[str] = Field(None, alias="Phone number")

class SocialMediaProfiles(BaseModel):
    LinkedIn: str
    GitHub: str
    Twitter: Optional[str] = None

class PersonalInformation(BaseModel):
    Name: str
    DOB: str
    Age: int
    Residing_location: str = Field(alias="Residing location")
    Nationality: str
    Languages: List[str]
    Hobbies: Optional[List[str]] = None
    family: Optional[Any] = None
    Contact_information: ContactInformation = Field(alias="Contact information")
    Social_media_profiles: SocialMediaProfiles = Field(alias="Social media profiles")
    Professional_summary: str = Field(alias="Professional summary")
    Skills_and_competencies: List[str] = Field(alias="Skills and competencies")

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
    key_points: List[str]
    tech_stack: List[str]
    tags: List[str]
    organization: str
    duration: str

ProjectsData = List[ProjectItem]
