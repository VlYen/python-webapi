from pydantic import AliasChoices, BaseModel, Field
from typing import Optional

class SchoolClassModel(BaseModel):
    Id: Optional[int] = Field(
        None,
        description="Primary key, auto-incremented",
        validation_alias=AliasChoices("ID", "Id", "id"),
        serialization_alias="id",
    )
    ClassName: str = Field(
        ...,
        max_length=50,
        validation_alias=AliasChoices("ClassName", "className"),
        serialization_alias="className",
    )
    Description: Optional[str] = Field(
        None,
        max_length=150,
        validation_alias=AliasChoices("Description", "description"),
        serialization_alias="description",
    )
    Instructor: Optional[str] = Field(
        None,
        max_length=100,
        validation_alias=AliasChoices("Instructor", "instructor"),
        serialization_alias="instructor",
    )
    StartDate: Optional[str] = Field(
        None,
        max_length=100,
        validation_alias=AliasChoices("StartDate", "startDate"),
        serialization_alias="startDate",
    )  
    EndDate: Optional[str] = Field(
        None,
        max_length=100,
        validation_alias=AliasChoices("EndDate", "endDate"),
        serialization_alias="endDate",
    )    
    Capacity: Optional[int] = Field(
        None,
        ge=0,  # Capacity should be a non-negative integer
        validation_alias=AliasChoices("Capacity", "capacity"),
        serialization_alias="capacity",
    )             
    IsActive: int = Field(
        1,
        ge=0,
        le=1,  # SQLite boolean: 0 = inactive, 1 = active
        validation_alias=AliasChoices("IsActive", "isActive"),
        serialization_alias="isActive",
    )
    CreatedAt: Optional[str] = Field(
        None,
        description="Set by the database (CURRENT_TIMESTAMP)",
        validation_alias=AliasChoices("CreatedAt", "createdAt"),
        serialization_alias="createdAt",
    )
