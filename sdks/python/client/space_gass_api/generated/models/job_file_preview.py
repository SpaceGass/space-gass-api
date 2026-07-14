from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class JobFilePreview(Parsable):
    """
    Information extracted from a SPACE GASS job file (.sg or .sgbase).Contains metadata appended to the file when saved.
    """
    # Compression type used when saving the file
    compression: Optional[str] = None
    # Computer name where the file was saved
    computer_name: Optional[str] = None
    # Date and time the file was saved
    date_saved: Optional[str] = None
    # The designer name when the file was saved
    designer: Optional[str] = None
    # The file name without path
    file_name: Optional[str] = None
    # The file path that was queried
    file_path: Optional[str] = None
    # File size in bytes
    file_size_bytes: Optional[int] = None
    # Whether a preview image is available
    has_preview_image: Optional[bool] = None
    # The job heading/title
    job_heading: Optional[str] = None
    # Last modified date of the file
    last_modified: Optional[datetime.datetime] = None
    # The licensee name that was used when saving the file
    licensee_name: Optional[str] = None
    # Job notes
    notes: Optional[str] = None
    # The preview image as a base64-encoded PNG string.Only populated if includeImage parameter is true.
    preview_image_base64: Optional[str] = None
    # The preview image as a Data URL (data:image/png;base64,...).Can be used directly in HTML img src attribute.Only available if includeImage parameter is true and image exists.
    preview_image_data_url: Optional[str] = None
    # The project heading/title
    project_heading: Optional[str] = None
    # User name who saved the file
    user_name: Optional[str] = None
    # The SPACE GASS version that was used to save the file
    version: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> JobFilePreview:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: JobFilePreview
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return JobFilePreview()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "compression": lambda n : setattr(self, 'compression', n.get_str_value()),
            "computerName": lambda n : setattr(self, 'computer_name', n.get_str_value()),
            "dateSaved": lambda n : setattr(self, 'date_saved', n.get_str_value()),
            "designer": lambda n : setattr(self, 'designer', n.get_str_value()),
            "fileName": lambda n : setattr(self, 'file_name', n.get_str_value()),
            "filePath": lambda n : setattr(self, 'file_path', n.get_str_value()),
            "fileSizeBytes": lambda n : setattr(self, 'file_size_bytes', n.get_int_value()),
            "hasPreviewImage": lambda n : setattr(self, 'has_preview_image', n.get_bool_value()),
            "jobHeading": lambda n : setattr(self, 'job_heading', n.get_str_value()),
            "lastModified": lambda n : setattr(self, 'last_modified', n.get_datetime_value()),
            "licenseeName": lambda n : setattr(self, 'licensee_name', n.get_str_value()),
            "notes": lambda n : setattr(self, 'notes', n.get_str_value()),
            "previewImageBase64": lambda n : setattr(self, 'preview_image_base64', n.get_str_value()),
            "previewImageDataUrl": lambda n : setattr(self, 'preview_image_data_url', n.get_str_value()),
            "projectHeading": lambda n : setattr(self, 'project_heading', n.get_str_value()),
            "userName": lambda n : setattr(self, 'user_name', n.get_str_value()),
            "version": lambda n : setattr(self, 'version', n.get_str_value()),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        writer.write_str_value("compression", self.compression)
        writer.write_str_value("computerName", self.computer_name)
        writer.write_str_value("dateSaved", self.date_saved)
        writer.write_str_value("designer", self.designer)
        writer.write_str_value("fileName", self.file_name)
        writer.write_str_value("filePath", self.file_path)
        writer.write_int_value("fileSizeBytes", self.file_size_bytes)
        writer.write_bool_value("hasPreviewImage", self.has_preview_image)
        writer.write_str_value("jobHeading", self.job_heading)
        writer.write_datetime_value("lastModified", self.last_modified)
        writer.write_str_value("licenseeName", self.licensee_name)
        writer.write_str_value("notes", self.notes)
        writer.write_str_value("previewImageBase64", self.preview_image_base64)
        writer.write_str_value("projectHeading", self.project_heading)
        writer.write_str_value("userName", self.user_name)
        writer.write_str_value("version", self.version)
    

