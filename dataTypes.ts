export interface EducationItem {
    institution: string;
    degree: string;
    duration: string;
    marks: string;
}

export interface CourseItem {
    name: string;
    platform: string;
    certificate: string | null;
    year: string;
}

export interface EducationData {
    education: EducationItem[];
    courses: CourseItem[];
}

export interface ExperienceItem {
    company: string;
    role: string;
    duration: {
        start: string;
        end: string;
    };
    responsibilities: string[];
}

export type ExperienceData = ExperienceItem[];

export interface OpenSourceItem {
    name: string;
    description: string;
    link: string;
}

export type OpenSourceData = OpenSourceItem[];

export interface PersonalInformation {
    Name: string;
    DOB: string;
    "Residing location": string;
    Nationality: string;
    Languages: string[];
    Hobbies: string[] | null;
    family: any | null;
    "Contact information": {
        Email: string;
        "Phone number": string | null;
    };
    "Social media profiles": {
        LinkedIn: string;
        GitHub: string;
        Twitter: string | null;
    };
    "Professional summary": string;
    "Skills and competencies": string[];
}

export interface Publication {
    description: string;
    link: string;
}

export interface PersonalData {
    description: string;
    personal_information: PersonalInformation;
    publications: Publication;
}

export interface ProjectItem {
    project_id: string;
    project_name: string;
    description: string;
    key_points: string[];
    tech_stack: string[];
    tags: string[];
    organization: string;
    duration: string;
}

export type ProjectsData = ProjectItem[];
