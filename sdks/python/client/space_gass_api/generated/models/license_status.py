from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .registration_status import RegistrationStatus

@dataclass
class LicenseStatus(Parsable):
    """
    Full licensing status for the API instance.Accessible even when the API is unlicensed (whitelisted in middleware)so clients can diagnose why requests are being refused.
    """
    # Names of module licenses currently active for this API instance.
    active_modules: Optional[list[str]] = None
    # Names of modules this company / user is entitled to (has purchased),whether or not they are currently acquired. Analogous to the SPACEGASS desktop "Help > About" dialog's licensed-module list. Emptyif the backend query failed (see SpaceGassApi.Models.Dtos.License.LicenseStatusDto.ErrorMessage).
    entitlements: Optional[list[str]] = None
    # Last error message when the license is not active; null otherwise.
    error_message: Optional[str] = None
    # Whether a job is currently open (Tier 2 SPACE GASS core held).
    is_job_open: Optional[bool] = None
    # True when the API is currently licensed (Tier 1 API module is held).
    is_licensed: Optional[bool] = None
    # True when this machine has a SPACE GASS registration the API supports(TitanCloud or Titan LM). False indicates either an unsupported locktype (e.g. legacy SGREG.DAT registration) or no registration at all.Always check this before SpaceGassApi.Models.Dtos.License.LicenseStatusDto.IsLicensed: an unregisteredAPI is blocked at the registration step, before any license acquireis attempted.
    is_registered: Optional[bool] = None
    # True when the active Titan LM session is backed by an offlineroaming licence file (no live LM server connection). Always falsefor TitanCloud and for non-roaming Titan LM. Operator-facingsignal so dashboards can tell which path is in use.
    is_roaming: Optional[bool] = None
    # UTC timestamp when the current job was opened (and the SPACE GASSlicence seat became active), or `null` when no job is open.
    job_opened_at: Optional[datetime.datetime] = None
    # License ID from the license server (the company registration number).
    license_id: Optional[int] = None
    # Current API mode. `"readwrite"` means writes and modulecheckout are allowed; `"readonly"` means no modules are heldand only reads + job lifecycle operations are accepted.
    mode: Optional[str] = None
    # Company or organisation name from the license server.
    organization: Optional[str] = None
    # Pending mode transition awaiting job-close commit. `"readonly"`,`"readwrite"`, or `null` when no transition is pending.
    pending: Optional[str] = None
    # Human-readable explanation of the registration state. Alwayspopulated. For TitanCloud / TitanLM it confirms the registrationis active; for Unsupported / Unregistered it explains what theoperator should do to fix it.
    registration_detail: Optional[str] = None
    # Outcome of probing the machine for a SPACE GASS registration.Mirrors the precedence used by desktop SPACE GASS in`NETLicenses/Licenses.vb::RegistrationSetupCheck`: legacy SGREG.DATshort-circuits before any Titan-type probing, then TitanCloud, then Titan LM.
    registration_type: Optional[RegistrationStatus] = None
    
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
        from .registration_status import RegistrationStatus

        from .registration_status import RegistrationStatus

        fields: dict[str, Callable[[Any], None]] = {
            "activeModules": lambda n : setattr(self, 'active_modules', n.get_collection_of_primitive_values(str)),
            "entitlements": lambda n : setattr(self, 'entitlements', n.get_collection_of_primitive_values(str)),
            "errorMessage": lambda n : setattr(self, 'error_message', n.get_str_value()),
            "isJobOpen": lambda n : setattr(self, 'is_job_open', n.get_bool_value()),
            "isLicensed": lambda n : setattr(self, 'is_licensed', n.get_bool_value()),
            "isRegistered": lambda n : setattr(self, 'is_registered', n.get_bool_value()),
            "isRoaming": lambda n : setattr(self, 'is_roaming', n.get_bool_value()),
            "jobOpenedAt": lambda n : setattr(self, 'job_opened_at', n.get_datetime_value()),
            "licenseId": lambda n : setattr(self, 'license_id', n.get_int_value()),
            "mode": lambda n : setattr(self, 'mode', n.get_str_value()),
            "organization": lambda n : setattr(self, 'organization', n.get_str_value()),
            "pending": lambda n : setattr(self, 'pending', n.get_str_value()),
            "registrationDetail": lambda n : setattr(self, 'registration_detail', n.get_str_value()),
            "registrationType": lambda n : setattr(self, 'registration_type', n.get_enum_value(RegistrationStatus)),
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
        writer.write_collection_of_primitive_values("activeModules", self.active_modules)
        writer.write_collection_of_primitive_values("entitlements", self.entitlements)
        writer.write_str_value("errorMessage", self.error_message)
        writer.write_bool_value("isJobOpen", self.is_job_open)
        writer.write_bool_value("isLicensed", self.is_licensed)
        writer.write_bool_value("isRegistered", self.is_registered)
        writer.write_bool_value("isRoaming", self.is_roaming)
        writer.write_datetime_value("jobOpenedAt", self.job_opened_at)
        writer.write_int_value("licenseId", self.license_id)
        writer.write_str_value("mode", self.mode)
        writer.write_str_value("organization", self.organization)
        writer.write_str_value("pending", self.pending)
        writer.write_str_value("registrationDetail", self.registration_detail)
        writer.write_enum_value("registrationType", self.registration_type)
    

