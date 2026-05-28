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
from typing import Any, Optional, TYPE_CHECKING, Union, overload
from warnings import warn

if TYPE_CHECKING:
    from .....models.error_response import ErrorResponse
    from .....models.expand_option import ExpandOption
    from .....models.section import Section
    from .....models.section_update import SectionUpdate
    from .library.library_request_builder import LibraryRequestBuilder

class SectionsItemRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /job/structure/sections/{id}
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new SectionsItemRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/job/structure/sections/{id}{?Expand*}", path_parameters)
    
    async def delete(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> None:
        """
        Deletes the entity with the supplied Id. Returns 204 on success, 404 if no entitywith that Id exists.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: None
        """
        request_info = self.to_delete_request_information(
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
        return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)
    
    # --- @overload added by regen_python_inits.py ---
    @overload
    async def get(
        self,
        *,
        expand: Optional[ExpandOption] = None,
    ) -> Optional[Section]: ...
    @overload
    async def get(self, request_configuration: Optional[RequestConfiguration[SectionsItemRequestBuilderGetQueryParameters]] = None) -> Optional[Section]: ...
    # --- end overloads ---
    async def get(self,request_configuration: Optional[RequestConfiguration[SectionsItemRequestBuilderGetQueryParameters]] = None, **kwargs) -> Optional[Section]:
        """
        `Expand` defaults to `all` on the single-item endpoint; pass `Expand=none`            to suppress sub-resource hydration. Sub-resource expansion is opt-in per resource type —            resources that don't define sub-resources ignore the parameter.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[Section]
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
        from .....models.section import Section

        return await self.request_adapter.send_async(request_info, Section, error_mapping)
    
    async def patch(self,body: SectionUpdate, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[Section]:
        """
        Updates an existing item. If a validator is registered, the update is validated first.
        param body: DTO for partially updating an existing section. All fields are optional — only fieldspresent on the request are updated.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[Section]
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
        from .....models.section import Section

        return await self.request_adapter.send_async(request_info, Section, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Deletes the entity with the supplied Id. Returns 204 on success, 404 if no entitywith that Id exists.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.DELETE, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[SectionsItemRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        `Expand` defaults to `all` on the single-item endpoint; pass `Expand=none`            to suppress sub-resource hydration. Sub-resource expansion is opt-in per resource type —            resources that don't define sub-resources ignore the parameter.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_patch_request_information(self,body: SectionUpdate, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Updates an existing item. If a validator is registered, the update is validated first.
        param body: DTO for partially updating an existing section. All fields are optional — only fieldspresent on the request are updated.
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
    
    def with_url(self,raw_url: str) -> SectionsItemRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: SectionsItemRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return SectionsItemRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def library(self) -> LibraryRequestBuilder:
        """
        The library property
        """
        from .library.library_request_builder import LibraryRequestBuilder

        return LibraryRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class SectionsItemRequestBuilderDeleteRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class SectionsItemRequestBuilderGetQueryParameters():
        """
        `Expand` defaults to `all` on the single-item endpoint; pass `Expand=none`            to suppress sub-resource hydration. Sub-resource expansion is opt-in per resource type —            resources that don't define sub-resources ignore the parameter.
        """
        def get_query_parameter(self,original_name: str) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            param original_name: The original query parameter name in the class.
            Returns: str
            """
            if original_name is None:
                raise TypeError("original_name cannot be null.")
            if original_name == "expand":
                return "Expand"
            return original_name
        
        # Sub-resource expansion. Defaults to `all`; pass `none` to suppress sub-resource hydration.
        expand: Optional[ExpandOption] = None

    
    @dataclass
    class SectionsItemRequestBuilderGetRequestConfiguration(RequestConfiguration[SectionsItemRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class SectionsItemRequestBuilderPatchRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

