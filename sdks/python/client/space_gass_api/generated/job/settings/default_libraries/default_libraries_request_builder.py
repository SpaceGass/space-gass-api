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
    from ....models.default_libraries_update import DefaultLibrariesUpdate
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
        Returns the default library for every library type nominated in SPACE GASS(Preferences, Default Libraries), each in its installed spelling, so a sections,materials or vehicles name can be passed straight to that type's search endpoint as itslibrary parameter. A type is null when no default is recorded or the nominated libraryis not installed. The values are the API's own SPACE GASS default library names: readfrom SG.INI when the API starts and changed by PATCH. A default changed in the desktop(a separate process) is seen after the API restarts.
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
    
    async def patch(self,body: DefaultLibrariesUpdate, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[DefaultLibraries]:
        """
        Partially updates the default library for each library type: only the names includedin the request body are changed. The names are the API's own SPACE GASS defaultlibraries; they are saved to SG.INI, so they apply to every job and survive a restart.Each name must be an installed library of its type, as in the desktop's DefaultLibraries dialog; it is matched without regard to case and stored in the installedspelling. A name that is not installed (including an empty one) is a 400 with codeREFERENCE_NOT_FOUND on that field, and nothing is changed.
        param body: A partial update of the default library for each library type(`PATCH job/settings/default-libraries`).
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[DefaultLibraries]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_patch_request_information(
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
        from ....models.default_libraries import DefaultLibraries

        return await self.request_adapter.send_async(request_info, DefaultLibraries, error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Returns the default library for every library type nominated in SPACE GASS(Preferences, Default Libraries), each in its installed spelling, so a sections,materials or vehicles name can be passed straight to that type's search endpoint as itslibrary parameter. A type is null when no default is recorded or the nominated libraryis not installed. The values are the API's own SPACE GASS default library names: readfrom SG.INI when the API starts and changed by PATCH. A default changed in the desktop(a separate process) is seen after the API restarts.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_patch_request_information(self,body: DefaultLibrariesUpdate, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Partially updates the default library for each library type: only the names includedin the request body are changed. The names are the API's own SPACE GASS defaultlibraries; they are saved to SG.INI, so they apply to every job and survive a restart.Each name must be an installed library of its type, as in the desktop's DefaultLibraries dialog; it is matched without regard to case and stored in the installedspelling. A name that is not installed (including an empty one) is a 400 with codeREFERENCE_NOT_FOUND on that field, and nothing is changed.
        param body: A partial update of the default library for each library type(`PATCH job/settings/default-libraries`).
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
    
    @dataclass
    class DefaultLibrariesRequestBuilderPatchRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

