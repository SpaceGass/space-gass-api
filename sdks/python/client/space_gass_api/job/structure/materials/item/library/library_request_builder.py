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
    from ......models.material import Material
    from ......models.material_library_create import MaterialLibraryCreate
    from ......models.problem_details import ProblemDetails

class LibraryRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /job/structure/materials/{id}/library
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new LibraryRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/job/structure/materials/{id}/library", path_parameters)
    
    async def put(self,body: MaterialLibraryCreate, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[Material]:
        """
        Replaces the material at the given Id with a library-sourced material. The existing rowis deleted and a new row is created at the same Id, resolved from the SPACE GASSmaterial library by (name, library). Use this to convert a User material to a Librarymaterial, or to re-resolve an existing Library material against a different libraryentry. Any `id` in the request body is ignored — the route Id wins.
        param body: DTO for creating a new library-sourced material.All material properties (Young's modulus, Poisson's ratio, etc.) are resolved from thelibrary — the caller provides only the material name and library.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[Material]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_put_request_information(
            body, request_configuration
        )
        from ......models.problem_details import ProblemDetails

        error_mapping: dict[str, type[ParsableFactory]] = {
            "400": ProblemDetails,
            "404": ProblemDetails,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ......models.material import Material

        return await self.request_adapter.send_async(request_info, Material, error_mapping)
    
    def to_put_request_information(self,body: MaterialLibraryCreate, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Replaces the material at the given Id with a library-sourced material. The existing rowis deleted and a new row is created at the same Id, resolved from the SPACE GASSmaterial library by (name, library). Use this to convert a User material to a Librarymaterial, or to re-resolve an existing Library material against a different libraryentry. Any `id` in the request body is ignored — the route Id wins.
        param body: DTO for creating a new library-sourced material.All material properties (Young's modulus, Poisson's ratio, etc.) are resolved from thelibrary — the caller provides only the material name and library.
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
    

