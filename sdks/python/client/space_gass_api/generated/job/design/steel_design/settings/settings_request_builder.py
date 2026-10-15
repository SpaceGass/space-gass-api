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
    from .....models.steel_member_design_general_settings import SteelMemberDesignGeneralSettings
    from .....models.steel_member_design_general_settings_update import SteelMemberDesignGeneralSettingsUpdate
    from .metadata.metadata_request_builder import MetadataRequestBuilder

class SettingsRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /job/design/steel-design/settings
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new SettingsRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/job/design/steel-design/settings", path_parameters)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[SteelMemberDesignGeneralSettings]:
        """
        Returns the steel member design settings — the code-independent inputs a runexecutes with (design groups, load cases, section availability, limits).Settings are saved with the job. The settings of each design code live atsteel-design/{code}/settings; the default section library a Design runselects new sections from is at /job/settings/default-libraries.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[SteelMemberDesignGeneralSettings]
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
        from .....models.steel_member_design_general_settings import SteelMemberDesignGeneralSettings

        return await self.request_adapter.send_async(request_info, SteelMemberDesignGeneralSettings, error_mapping)
    
    async def patch(self,body: SteelMemberDesignGeneralSettingsUpdate, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[SteelMemberDesignGeneralSettings]:
        """
        Partially updates the steel member design settings. Only fields included inthe request body are updated; omitted fields remain unchanged.
        param body: Update request for the general steel member design settings.Only fields included in the request are updated; omit a field to keep its current value.Used by PATCH /job/design/steel-design/settings and the settings overrides on the run endpoints.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[SteelMemberDesignGeneralSettings]
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
        from .....models.steel_member_design_general_settings import SteelMemberDesignGeneralSettings

        return await self.request_adapter.send_async(request_info, SteelMemberDesignGeneralSettings, error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Returns the steel member design settings — the code-independent inputs a runexecutes with (design groups, load cases, section availability, limits).Settings are saved with the job. The settings of each design code live atsteel-design/{code}/settings; the default section library a Design runselects new sections from is at /job/settings/default-libraries.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_patch_request_information(self,body: SteelMemberDesignGeneralSettingsUpdate, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Partially updates the steel member design settings. Only fields included inthe request body are updated; omitted fields remain unchanged.
        param body: Update request for the general steel member design settings.Only fields included in the request are updated; omit a field to keep its current value.Used by PATCH /job/design/steel-design/settings and the settings overrides on the run endpoints.
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
    
    @property
    def metadata(self) -> MetadataRequestBuilder:
        """
        The metadata property
        """
        from .metadata.metadata_request_builder import MetadataRequestBuilder

        return MetadataRequestBuilder(self.request_adapter, self.path_parameters)
    
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
    

