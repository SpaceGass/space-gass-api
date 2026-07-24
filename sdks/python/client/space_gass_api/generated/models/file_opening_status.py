from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .job_file_opening_status import JobFileOpeningStatus
    from .job_force_access_option import JobForceAccessOption

@dataclass
class FileOpeningStatus(Parsable):
    """
    Status information about a SPACE GASS file's readiness for opening.
    """
    # The recovery options that can be supplied as `forceOption` on `POST job/open`for this file's current status.
    available_recovery_options: Optional[list[JobForceAccessOption]] = None
    # Whether the file can be opened safely without force options
    can_open_safely: Optional[bool] = None
    # Human-readable description of the status
    description: Optional[str] = None
    # The file path that was checked
    file_path: Optional[str] = None
    # Recommended action to take based on the status
    recommended_action: Optional[str] = None
    # Openability of a SPACE GASS job file, as returned by `GET file/status`.Only `ReadyToOpen` opens without a `forceOption`; `Locked`,`UnsavedChanges` and `LockedWithUnsavedChanges` require one on`POST job/open`. `NotFound` and `RecoveryFilesOnly` cannot beopened at the checked path — no .sg file exists there.
    status: Optional[JobFileOpeningStatus] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> FileOpeningStatus:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: FileOpeningStatus
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return FileOpeningStatus()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .job_file_opening_status import JobFileOpeningStatus
        from .job_force_access_option import JobForceAccessOption

        from .job_file_opening_status import JobFileOpeningStatus
        from .job_force_access_option import JobForceAccessOption

        fields: dict[str, Callable[[Any], None]] = {
            "availableRecoveryOptions": lambda n : setattr(self, 'available_recovery_options', n.get_collection_of_enum_values(JobForceAccessOption)),
            "canOpenSafely": lambda n : setattr(self, 'can_open_safely', n.get_bool_value()),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "filePath": lambda n : setattr(self, 'file_path', n.get_str_value()),
            "recommendedAction": lambda n : setattr(self, 'recommended_action', n.get_str_value()),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(JobFileOpeningStatus)),
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
        writer.write_collection_of_enum_values("availableRecoveryOptions", self.available_recovery_options)
        writer.write_bool_value("canOpenSafely", self.can_open_safely)
        writer.write_str_value("description", self.description)
        writer.write_str_value("filePath", self.file_path)
        writer.write_str_value("recommendedAction", self.recommended_action)
        writer.write_enum_value("status", self.status)
    

