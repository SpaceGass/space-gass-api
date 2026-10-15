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
    from ....models.default_libraries import DefaultLibraries
    from ....models.error_response import ErrorResponse

class DefaultLibrariesRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /job/settings/default-libraries
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new DefaultLibrariesRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/job/settings/default-libraries", path_parameters)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[DefaultLibraries]:
        """
        Returns the default library for every library type nominated in SPACE GASS(Preferences, Default Libraries). sections, materials and vehicles are keyed by theirroute segment under /libraries, returned in installed spelling so the name can be passedstraight to that type's search endpoint as its library parameter, and null when nodefault is recorded or the nominated library is not installed. bolts, plates, welds,spectralCurves and reinforcingBars have no catalogue endpoint and are reported asrecorded, null when none is recorded. The values are read when the API starts; a defaultchanged in SPACE GASS while the API is running is seen after the API restarts.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[DefaultLibraries]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ....models.error_response import ErrorResponse

        error_mapping: dict[str, type[ParsableFactory]] = {
            "403": ErrorResponse,
            "404": ErrorResponse,
            "500": ErrorResponse,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ....models.default_libraries import DefaultLibraries

        return await self.request_adapter.send_async(request_info, DefaultLibraries, error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Returns the default library for every library type nominated in SPACE GASS(Preferences, Default Libraries). sections, materials and vehicles are keyed by theirroute segment under /libraries, returned in installed spelling so the name can be passedstraight to that type's search endpoint as its library parameter, and null when nodefault is recorded or the nominated library is not installed. bolts, plates, welds,spectralCurves and reinforcingBars have no catalogue endpoint and are reported asrecorded, null when none is recorded. The values are read when the API starts; a defaultchanged in SPACE GASS while the API is running is seen after the API restarts.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def with_url(self,raw_url: str) -> DefaultLibrariesRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: DefaultLibrariesRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return DefaultLibrariesRequestBuilder(self.request_adapter, raw_url)
    
    @dataclass
    class DefaultLibrariesRequestBuilderGetRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

