from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from kiota_abstractions.default_query_parameters import QueryParameters
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.request_adapter import RequestAdapter
from kiota_abstractions.request_information import RequestInformation
from kiota_abstractions.request_option import RequestOption
from kiota_abstractions.serialization import Parsable, ParsableFactory
from typing import Any, Optional, TYPE_CHECKING, Union
from warnings import warn

if TYPE_CHECKING:
    from .....models.error_response import ErrorResponse
    from .....models.ifc_export_settings import IfcExportSettings
    from .....models.ifc_export_settings_update import IfcExportSettingsUpdate

class SettingsRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /job/export/ifc/settings
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new SettingsRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/job/export/ifc/settings", path_parameters)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[IfcExportSettings]:
        """
        Returns the settings that apply to an IFC export when the export request leavesthem out. Every setting is always returned.            These are the same settings the SPACE GASS export dialog uses, read from the file thatdialog stores them in. A setting changed in the dialog is returned here, and thesettings outlive a restart of this service.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[IfcExportSettings]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from .....models.error_response import ErrorResponse

        error_mapping: dict[str, type[ParsableFactory]] = {
            "403": ErrorResponse,
            "404": ErrorResponse,
            "500": ErrorResponse,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .....models.ifc_export_settings import IfcExportSettings

        return await self.request_adapter.send_async(request_info, IfcExportSettings, error_mapping)
    
    async def patch(self,body: IfcExportSettingsUpdate, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[IfcExportSettings]:
        """
        Changes only the settings present in the body; every setting left out keeps its currentvalue.            The change is written to the settings file SPACE GASS reads, so it also changes what thedesktop export dialog opens showing. Settings passed on an export request instead applyto that one export and change nothing stored.            Example request:                PATCH /api/v1/job/export/ifc/settings    {      "analyticalModel": false    }
        param body: Request body for `PATCH job/export/ifc/settings`. Only the settings present in thebody are changed; every setting left out keeps its current value. The change is written tothe settings file SPACE GASS reads.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[IfcExportSettings]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_patch_request_information(
            body, request_configuration
        )
        from .....models.error_response import ErrorResponse

        error_mapping: dict[str, type[ParsableFactory]] = {
            "400": ErrorResponse,
            "403": ErrorResponse,
            "404": ErrorResponse,
            "500": ErrorResponse,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .....models.ifc_export_settings import IfcExportSettings

        return await self.request_adapter.send_async(request_info, IfcExportSettings, error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Returns the settings that apply to an IFC export when the export request leavesthem out. Every setting is always returned.            These are the same settings the SPACE GASS export dialog uses, read from the file thatdialog stores them in. A setting changed in the dialog is returned here, and thesettings outlive a restart of this service.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_patch_request_information(self,body: IfcExportSettingsUpdate, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Changes only the settings present in the body; every setting left out keeps its currentvalue.            The change is written to the settings file SPACE GASS reads, so it also changes what thedesktop export dialog opens showing. Settings passed on an export request instead applyto that one export and change nothing stored.            Example request:                PATCH /api/v1/job/export/ifc/settings    {      "analyticalModel": false    }
        param body: Request body for `PATCH job/export/ifc/settings`. Only the settings present in thebody are changed; every setting left out keeps its current value. The change is written tothe settings file SPACE GASS reads.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = RequestInformation(Method.PATCH, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    def with_url(self,raw_url: str) -> SettingsRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: SettingsRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return SettingsRequestBuilder(self.request_adapter, raw_url)
    
    @dataclass
    class SettingsRequestBuilderGetRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class SettingsRequestBuilderPatchRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

