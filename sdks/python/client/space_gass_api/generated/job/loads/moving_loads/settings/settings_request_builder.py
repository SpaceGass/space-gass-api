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
    from .....models.moving_load_settings import MovingLoadSettings
    from .....models.moving_load_settings_update import MovingLoadSettingsUpdate
    from .metadata.metadata_request_builder import MetadataRequestBuilder

class SettingsRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /job/loads/moving-loads/settings
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new SettingsRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/job/loads/moving-loads/settings", path_parameters)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[MovingLoadSettings]:
        """
        Gets the collection-level moving-load settings — generation flags, vertical-proximitytolerance, the loaded-area polygon, and the read-only length/force units.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[MovingLoadSettings]
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
        from .....models.moving_load_settings import MovingLoadSettings

        return await self.request_adapter.send_async(request_info, MovingLoadSettings, error_mapping)
    
    async def patch(self,body: MovingLoadSettingsUpdate, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[MovingLoadSettings]:
        """
        Partially updates the collection-level settings (flags, vertical proximity, and theloaded-area polygon); omitted fields keep their current value. Units are read-only —change them via `POST /job/units`.
        param body: Partial update for SpaceGassApi.Models.Dtos.MovingLoads.MovingLoadSettingsDto. All properties are optional;omitted properties keep their current value.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[MovingLoadSettings]
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
        from .....models.moving_load_settings import MovingLoadSettings

        return await self.request_adapter.send_async(request_info, MovingLoadSettings, error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Gets the collection-level moving-load settings — generation flags, vertical-proximitytolerance, the loaded-area polygon, and the read-only length/force units.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_patch_request_information(self,body: MovingLoadSettingsUpdate, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Partially updates the collection-level settings (flags, vertical proximity, and theloaded-area polygon); omitted fields keep their current value. Units are read-only —change them via `POST /job/units`.
        param body: Partial update for SpaceGassApi.Models.Dtos.MovingLoads.MovingLoadSettingsDto. All properties are optional;omitted properties keep their current value.
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
    

