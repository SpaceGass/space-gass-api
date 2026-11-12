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
    from .....models.section_geometry import SectionGeometry
    from .item.sections_item_request_builder import SectionsItemRequestBuilder
    from .metadata.metadata_request_builder import MetadataRequestBuilder

class SectionsRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /job/query/geometry/sections
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new SectionsRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/job/query/geometry/sections{?limit*,offset*,sections*}", path_parameters)
    
    def by_id(self,id: int) -> SectionsItemRequestBuilder:
        """
        Gets an item from the space_gass_api.generated.job.query.geometry.sections.item collection
        param id: The section Id
        Returns: SectionsItemRequestBuilder
        """
        if id is None:
            raise TypeError("id cannot be null.")
        from .item.sections_item_request_builder import SectionsItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["id"] = id
        return SectionsItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    # --- @overload added by regen_python_inits.py ---
    @overload
    async def get(
        self,
        *,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        sections: Optional[str] = None,
    ) -> Optional[list[SectionGeometry]]: ...
    @overload
    async def get(self, request_configuration: Optional[RequestConfiguration[SectionsRequestBuilderGetQueryParameters]] = None) -> Optional[list[SectionGeometry]]: ...
    # --- end overloads ---
    async def get(self,request_configuration: Optional[RequestConfiguration[SectionsRequestBuilderGetQueryParameters]] = None, **kwargs) -> Optional[list[SectionGeometry]]:
        """
        Lists the cross-section geometry of each section: the extent of the whole section andthe outlines of each shape (each an outer polygon plus any holes), in the member's localY-Z plane with the origin at the section centroid and in the job'ssection-properties unit. Sweeping a section's outlines from a member's `pointA` to`pointB` along its `localAxes` (GET geometry/members) gives the member's solid.Supports the standard section filter and offset/limit pagination; results are sorted bysection Id ascending and pagination metadata is returned in response headers(Total-Count, Offset, Limit). Sections without shape geometry are returned with an empty`shapes` list and no `bounds`.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[list[SectionGeometry]]
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
        from .....models.section_geometry import SectionGeometry

        return await self.request_adapter.send_collection_async(request_info, SectionGeometry, error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[SectionsRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        Lists the cross-section geometry of each section: the extent of the whole section andthe outlines of each shape (each an outer polygon plus any holes), in the member's localY-Z plane with the origin at the section centroid and in the job'ssection-properties unit. Sweeping a section's outlines from a member's `pointA` to`pointB` along its `localAxes` (GET geometry/members) gives the member's solid.Supports the standard section filter and offset/limit pagination; results are sorted bysection Id ascending and pagination metadata is returned in response headers(Total-Count, Offset, Limit). Sections without shape geometry are returned with an empty`shapes` list and no `bounds`.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def with_url(self,raw_url: str) -> SectionsRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: SectionsRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return SectionsRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def metadata(self) -> MetadataRequestBuilder:
        """
        The metadata property
        """
        from .metadata.metadata_request_builder import MetadataRequestBuilder

        return MetadataRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class SectionsRequestBuilderGetQueryParameters():
        """
        Lists the cross-section geometry of each section: the extent of the whole section andthe outlines of each shape (each an outer polygon plus any holes), in the member's localY-Z plane with the origin at the section centroid and in the job'ssection-properties unit. Sweeping a section's outlines from a member's `pointA` to`pointB` along its `localAxes` (GET geometry/members) gives the member's solid.Supports the standard section filter and offset/limit pagination; results are sorted bysection Id ascending and pagination metadata is returned in response headers(Total-Count, Offset, Limit). Sections without shape geometry are returned with an empty`shapes` list and no `bounds`.
        """
        # Maximum number of items to return. Default is null (return all).
        limit: Optional[int] = None

        # Number of items to skip from the start of the result set. Default is 0.
        offset: Optional[int] = None

        # Section Ids to filter by, in SG list format (e.g. `"1,3-7,10"`).Omit to return all sections.
        sections: Optional[str] = None

    
    @dataclass
    class SectionsRequestBuilderGetRequestConfiguration(RequestConfiguration[SectionsRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

