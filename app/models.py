from pydantic import BaseModel, EmailStr, Field, HttpUrl
from typing import List, Optional
from enum import Enum

class Languages(str, Enum):
    solidity = "Solidity"
    rust = "Rust"
    nodejs = "Node.js"
    typescript = "Typescript"
    javascript = "Javascript"
    c = "C"
    cpp = "C++"
    csharp = "C#"
    sql = "SQL"
    python = "Python"
    assembly = "Assembly Language"
    haskell = "Haskell"
    r = "R"
    dotnet = ".NET"
    other = "Other"

class ExperienceLevel(str, Enum):
    no_experience = "No experience (I have never programmed before.)"
    beginner = "Beginner (I have played with some introductory coding lessons and tutorials.)"
    intermediate = "Intermediate (I have completed some coding classes or tutorials.)"
    advanced = "Advanced (I can build applications)"
    professional = "Professional (I am an experienced software engineer)"

class Compensation(str, Enum):
    less_than_30k = "<$30,000"
    from_30k_to_50k = "$30,000 - $50,000"
    from_50k_to_80k = "$50,000 - $80,000"
    from_80k_to_120k = "$80,000 - $120,000"
    from_120k_to_250k = "$120,000 - $250,000"
    more_than_250k = "$250,000 or more"

class CertifyingStatement(str, Enum):
    accept = "I accept"
    dont_care = "I don't care"

class FormData(BaseModel):
    first_name: str = Field(..., example="John")
    last_name: str = Field(..., example="Smith")
    email: EmailStr = Field(..., example="name@example.com")
    country: str = Field(..., example="USA")
    phone_number: str = Field(..., example="+1234567890")
    languages: List[Languages]
    experience_level: ExperienceLevel
    compensation: Optional[Compensation] = None
    certifying_statement: CertifyingStatement
    linkedin_url: Optional[HttpUrl] = Field(None, example="https://www.linkedin.com/in/johnsmith")

class FormResponse(BaseModel):
    id: str
    first_name: str
    last_name: str
    email: str
    country: str
    phone_number: str
    languages: List[Languages]
    experience_level: ExperienceLevel
    compensation: Optional[Compensation]
    certifying_statement: CertifyingStatement
    linkedin_url: Optional[HttpUrl]
