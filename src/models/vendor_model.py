from pydantic import AliasChoices, BaseModel, Field
from typing import Optional

class VendorModel(BaseModel):
    VendorID: Optional[int] = Field(
        None,
        description="Primary key, auto-incremented",
        validation_alias=AliasChoices("VendorID", "VendorId", "vendorID", "vendorId"),
        serialization_alias="vendorId",
    )
    VendorName: str = Field(
        ...,
        max_length=50,
        validation_alias=AliasChoices("VendorName", "vendorName"),
        serialization_alias="vendorName",
    )
    VendorPhone: str = Field(
        ...,
        max_length=10,
        validation_alias=AliasChoices("VendorPhone", "vendorPhone"),
        serialization_alias="vendorPhone",
    )
    Email: Optional[str] = Field(
        None,
        max_length=50,
        validation_alias=AliasChoices("Email", "email"),
        serialization_alias="email",
    )