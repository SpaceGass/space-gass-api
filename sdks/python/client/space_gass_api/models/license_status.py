from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .held_module import HeldModule

@dataclass
class LicenseStatus(Parsable):
    """
    Full licensing status for the API instance.Accessible even when the API is unlicensed (whitelisted in middleware)so clients can diagnose why requests are being refused.
    """
    # The licensing backend in use ("TitanCloud" or "TitanSoftlock").Empty when the machine is not registered for a supported backend.
    backend_type: Optional[str] = None
    # Timestamp when the SPACE GASS core module was acquired, if any.
    core_module_acquired_at: Optional[datetime.datetime] = None
    # Modules this company / user is entitled to (has purchased), whether or notthey are currently acquired. Analogous to the SPACE GASS desktop"Help > About" dialog's licensed-module list. Empty if the backendquery failed (see SpaceGassApi.Models.Dtos.License.LicenseStatusDto.ErrorMessage).
    entitlements: Optional[list[HeldModule]] = None
    # Last error message when the license is not active; null otherwise.
    error_message: Optional[str] = None
    # All module licenses currently held by this API instance.
    held_modules: Optional[list[HeldModule]] = None
    # Whether a job is currently open (Tier 2 SPACE GASS core held).
    is_job_open: Optional[bool] = None
    # True when the API is currently licensed (Tier 1 API module is held).
    is_licensed: Optional[bool] = None
    # True when this machine has a SPACE GASS registration the API supports(TitanCloud or Titan LM). False indicates either an unsupported locktype (e.g. legacy SGREG.DAT registration) or no registration at all.Always check this before SpaceGassApi.Models.Dtos.License.LicenseStatusDto.IsLicensed: an unregisteredAPI is blocked at the registration step, before any license acquireis attempted.
    is_registered: Optional[bool] = None
    # True when the active Titan LM session is backed by an offlineroaming licence file (no live LM server connection). Always falsefor TitanCloud and for non-roaming Titan LM. Operator-facingsignal so dashboards can tell which path is in use.
    is_roaming: Optional[bool] = None
    # Company registration / lock ID from the license server.
    lock_id: Optional[int] = None
    # Company or organisation name from the license server.
    organization: Optional[str] = None
    # Human-readable explanation of the registration state — what wasdetected, and what the operator should do if registration is missingor unsupported.
    registration_detail: Optional[str] = None
    # Detected registration status: "TitanCloud", "TitanLm", "Unsupported",or "Unregistered".
    registration_status: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> LicenseStatus:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: LicenseStatus
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return LicenseStatus()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .held_module import HeldModule

        from .held_module import HeldModule

        fields: dict[str, Callable[[Any], None]] = {
            "backendType": lambda n : setattr(self, 'backend_type', n.get_str_value()),
            "coreModuleAcquiredAt": lambda n : setattr(self, 'core_module_acquired_at', n.get_datetime_value()),
            "entitlements": lambda n : setattr(self, 'entitlements', n.get_collection_of_object_values(HeldModule)),
            "errorMessage": lambda n : setattr(self, 'error_message', n.get_str_value()),
            "heldModules": lambda n : setattr(self, 'held_modules', n.get_collection_of_object_values(HeldModule)),
            "isJobOpen": lambda n : setattr(self, 'is_job_open', n.get_bool_value()),
            "isLicensed": lambda n : setattr(self, 'is_licensed', n.get_bool_value()),
            "isRegistered": lambda n : setattr(self, 'is_registered', n.get_bool_value()),
            "isRoaming": lambda n : setattr(self, 'is_roaming', n.get_bool_value()),
            "lockId": lambda n : setattr(self, 'lock_id', n.get_int_value()),
            "organization": lambda n : setattr(self, 'organization', n.get_str_value()),
            "registrationDetail": lambda n : setattr(self, 'registration_detail', n.get_str_value()),
            "registrationStatus": lambda n : setattr(self, 'registration_status', n.get_str_value()),
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
        writer.write_str_value("backendType", self.backend_type)
        writer.write_datetime_value("coreModuleAcquiredAt", self.core_module_acquired_at)
        writer.write_collection_of_object_values("entitlements", self.entitlements)
        writer.write_str_value("errorMessage", self.error_message)
        writer.write_collection_of_object_values("heldModules", self.held_modules)
        writer.write_bool_value("isJobOpen", self.is_job_open)
        writer.write_bool_value("isLicensed", self.is_licensed)
        writer.write_bool_value("isRegistered", self.is_registered)
        writer.write_bool_value("isRoaming", self.is_roaming)
        writer.write_int_value("lockId", self.lock_id)
        writer.write_str_value("organization", self.organization)
        writer.write_str_value("registrationDetail", self.registration_detail)
        writer.write_str_value("registrationStatus", self.registration_status)
    

