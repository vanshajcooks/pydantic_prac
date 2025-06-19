from pydantic import BaseModel, Field
from typing import Dict, List, Optional



class Employee(BaseModel):
    id: int
    name: str = Field(
        ...,
        min_length = 3,
        max_length=50,
        description="Employee Name",
        example = "Vanshaj Sharma"
        )
    department: Optional[str] = 'General' #gives default value General
    salary: float = Field(..., ge=10000) # keeps value greater than 10000 that is required field
    