from pydantic import AliasChoices, BaseModel, Field
from typing import Optional

class StudentModel(BaseModel):
    Id: Optional[int] = Field(
        None,
        description="Primary key, auto-incremented",
        validation_alias=AliasChoices("ID", "Id", "id"),
        serialization_alias="id",
    )
    FirstName: str = Field(
        ...,
        max_length=50,
        validation_alias=AliasChoices("FirstName", "firstName"),
        serialization_alias="firstName",
    )
    LastName: str = Field(
        ...,
        max_length=50,
        validation_alias=AliasChoices("LastName", "lastName"),
        serialization_alias="lastName",
    )
    SSN: Optional[str] = Field(
        None,
        max_length=100,
        validation_alias=AliasChoices("SSN", "ssn"),
        serialization_alias="ssn",
    )