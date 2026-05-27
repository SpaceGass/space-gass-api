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
    from ......models.error_response import ErrorResponse
    from ......models.section import Section
    from ......models.section_library_create import SectionLibraryCreate

class LibraryRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /job/structure/sections/{id}/library
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new LibraryRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/job/structure/sections/{id}/library", path_parameters)
    
    async def put(self,body: SectionLibraryCreate, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[Section]:
        """
        Replaces the section at the given Id with a library-sourced section. The existing rowis deleted and a new row is created at the same Id, resolved from the SPACE GASSsection library by (name, library). Use this to convert a User section to a Librarysection, or to re-resolve an existing Library section against a different libraryentry. Any `id` in the request body is ignored — the route Id wins.
        param body: DTO for creating a library-sourced section. Structural properties (A, J, Iy, Iz, etc.)and cross-section shape data are resolved from the SPACE GASS section library by(name, library).
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[Section]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_put_request_information(
            body, request_configuration
        )
        from ......models.error_response import ErrorResponse

        error_mapping: dict[str, type[ParsableFactory]] = {
            "400": ErrorResponse,
            "403": ErrorResponse,
            "404": ErrorResponse,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ......models.section import Section

        return await self.request_adapter.send_async(request_info, Section, error_mapping)
    
    def to_put_request_information(self,body: SectionLibraryCreate, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Replaces the section at the given Id with a library-sourced section. The existing rowis deleted and a new row is created at the same Id, resolved from the SPACE GASSsection library by (name, library). Use this to convert a User section to a Librarysection, or to re-resolve an existing Library section against a different libraryentry. Any `id` in the request body is ignored — the route Id wins.
        param body: DTO for creating a library-sourced section. Structural properties (A, J, Iy, Iz, etc.)and cross-section shape data are resolved from the SPACE GASS section library by(name, library).
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = RequestInformation(Method.PUT, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    def with_url(self,raw_url: str) -> LibraryRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: LibraryRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return LibraryRequestBuilder(self.request_adapter, raw_url)
    
    @dataclass
    class LibraryRequestBuilderPutRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

