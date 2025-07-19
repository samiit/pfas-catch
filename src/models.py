"""Data models for the PFAS Catch application."""

from pydantic import BaseModel, Field
from fastapi.responses import FileResponse


class FileResponseModel(BaseModel):
    """Model for file response."""

    images_2d: list[FileResponse] = Field(..., description="List of 2D image files")
    images_3d: list[FileResponse] = Field(..., description="List of 3D image files")
