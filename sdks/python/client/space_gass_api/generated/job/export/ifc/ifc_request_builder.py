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
    from ....models.error_response import ErrorResponse
    from ....models.ifc_export_request import IfcExportRequest
    from .settings.settings_request_builder import SettingsRequestBuilder

class IfcRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /job/export/ifc
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new IfcRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/job/export/ifc", path_parameters)
    
    async def post(self,body: IfcExportRequest, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[bytes]:
        """
        Exports the current job to IFC and returns the file itself as a download. The job is notmodified and nothing is written to a server-side path.            The request body is optional. Every setting it carries applies to this exportonly and changes nothing stored; a setting left out falls back to the stored exportsettings (`GET job/export/ifc/settings`), which are the settings SPACE GASS itselfexports with. An empty body exports entirely from those settings.            `physicalModel` and `analyticalModel` each cover everything in that model —members and plates for both, plus loads and load combinations for the analytical model.When `schema` is `Ifc2x3`, no loads or load combinations are written, so ananalytical model in that schema carries its members and plates only. Analysis resultsare never exported.            The number of warnings the exporter raised is returned in the`Export-Warning-Count` response header.            Export runs synchronously, so the request blocks for the duration of the export.            Example request:                POST /api/v1/job/export/ifc    {      "schema": "Ifc4",      "analyticalModel": false,      "convertTo": "RevitStructure"    }
        param body: Optional request body for `POST job/export/ifc`. Every setting is optional: asetting supplied here applies to this export only and changes nothing stored, and a settingleft out falls back to the stored export settings (`GET job/export/ifc/settings`),which are shared with SPACE GASS. An empty body exports entirely from the stored settings.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: bytes
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_post_request_information(
            body, request_configuration
        )
        from ....models.error_response import ErrorResponse

        error_mapping: dict[str, type[ParsableFactory]] = {
            "400": ErrorResponse,
            "403": ErrorResponse,
            "404": ErrorResponse,
            "500": ErrorResponse,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_primitive_async(request_info, "bytes", error_mapping)
    
    def to_post_request_information(self,body: IfcExportRequest, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Exports the current job to IFC and returns the file itself as a download. The job is notmodified and nothing is written to a server-side path.            The request body is optional. Every setting it carries applies to this exportonly and changes nothing stored; a setting left out falls back to the stored exportsettings (`GET job/export/ifc/settings`), which are the settings SPACE GASS itselfexports with. An empty body exports entirely from those settings.            `physicalModel` and `analyticalModel` each cover everything in that model —members and plates for both, plus loads and load combinations for the analytical model.When `schema` is `Ifc2x3`, no loads or load combinations are written, so ananalytical model in that schema carries its members and plates only. Analysis resultsare never exported.            The number of warnings the exporter raised is returned in the`Export-Warning-Count` response header.            Export runs synchronously, so the request blocks for the duration of the export.            Example request:                POST /api/v1/job/export/ifc    {      "schema": "Ifc4",      "analyticalModel": false,      "convertTo": "RevitStructure"    }
        param body: Optional request body for `POST job/export/ifc`. Every setting is optional: asetting supplied here applies to this export only and changes nothing stored, and a settingleft out falls back to the stored export settings (`GET job/export/ifc/settings`),which are shared with SPACE GASS. An empty body exports entirely from the stored settings.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = RequestInformation(Method.POST, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    def with_url(self,raw_url: str) -> IfcRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: IfcRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return IfcRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def settings(self) -> SettingsRequestBuilder:
        """
        The settings property
        """
        from .settings.settings_request_builder import SettingsRequestBuilder

        return SettingsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class IfcRequestBuilderPostRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

