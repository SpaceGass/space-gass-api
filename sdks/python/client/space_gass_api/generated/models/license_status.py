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
    # True when a validated licence session is active. Independent of theread/write seat — `true` even in ReadOnly / session-only mode.
    is_licensed: Optional[bool] = None
    # True when this machine has a SPACE GASS registration the API supports(Cloud licence or Titan Softlock). False indicates either an unsupportedlock type (e.g. legacy SGREG.DAT registration) or no registration at all.Always check this before SpaceGassApi.Models.Dtos.License.LicenseStatusDto.IsLicensed: an unregisteredAPI is blocked at the registration step, before any license acquireis attempted.
    is_registered: Optional[bool] = None
    # True when the active Titan Softlock session is backed by an offlineroaming licence file (no live licence-server connection). Always falsefor the Cloud licence and for non-roaming Titan Softlock. Operator-facingsignal so dashboards can tell which path is in use.
    is_roaming: Optional[bool] = None
    # UTC timestamp when the current job was opened (and the SPACE GASSlicence seat became active), or `null` when no job is open.
    job_opened_at: Optional[datetime.datetime] = None
    # License ID from the license server (the company registration number).
    license_id: Optional[int] = None
    # Company or organisation name from the license server.
    organization: Optional[str] = None
    # Human-readable explanation of the registration state. Alwayspopulated. For `TitanCloud` / `TitanLM` it reports whether theregistration is usable; for `Unsupported` / `Unregistered` itexplains what the operator should do to fix it. A Cloud licenceregistration whose login file holds no usable credentials stays`TitanCloud` here but says so in this field.
    registration_detail: Optional[str] = None
    # Outcome of probing the machine for a SPACE GASS registration, in the sameprecedence desktop SPACE GASS uses: a legacy SGREG.DAT lock short-circuitsfirst, then the Cloud licence, then Titan Softlock.
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
            "organization": lambda n : setattr(self, 'organization', n.get_str_value()),
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
        writer.write_str_value("organization", self.organization)
        writer.write_str_value("registrationDetail", self.registration_detail)
        writer.write_enum_value("registrationType", self.registration_type)
    

