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
    from .....models.plate_geometry import PlateGeometry
    from .....models.plate_theory import PlateTheory
    from .item.plates_item_request_builder import PlatesItemRequestBuilder

class PlatesRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /job/query/geometry/plates
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new PlatesRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/job/query/geometry/plates{?limit*,material*,offset*,plates*,theory*}", path_parameters)
    
    def by_id(self,id: int) -> PlatesItemRequestBuilder:
        """
        Gets an item from the space_gass_api.generated.job.query.geometry.plates.item collection
        param id: The plate Id
        Returns: PlatesItemRequestBuilder
        """
        if id is None:
            raise TypeError("id cannot be null.")
        from .item.plates_item_request_builder import PlatesItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["id"] = id
        return PlatesItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    # --- @overload added by regen_python_inits.py ---
    @overload
    async def get(
        self,
        *,
        limit: Optional[int] = None,
        material: Optional[int] = None,
        offset: Optional[int] = None,
        plates: Optional[str] = None,
        theory: Optional[PlateTheory] = None,
    ) -> Optional[list[PlateGeometry]]: ...
    @overload
    async def get(self, request_configuration: Optional[RequestConfiguration[PlatesRequestBuilderGetQueryParameters]] = None) -> Optional[list[PlateGeometry]]: ...
    # --- end overloads ---
    async def get(self,request_configuration: Optional[RequestConfiguration[PlatesRequestBuilderGetQueryParameters]] = None, **kwargs) -> Optional[list[PlateGeometry]]:
        """
        Lists derived geometry for plates: corner nodes (analytical), physical (offset-shifted)corner points, area, perimeter, centroid and the local coordinate system. Supports thestandard plate filters and offset/limit pagination; results are sorted by plate Idascending and pagination metadata is returned in response headers (Total-Count, Offset,Limit). Plates whose corner nodes are missing, or whose frame cannot be computed(degenerate geometry), are omitted from the response.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[list[PlateGeometry]]
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
        from .....models.plate_geometry import PlateGeometry

        return await self.request_adapter.send_collection_async(request_info, PlateGeometry, error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[PlatesRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        Lists derived geometry for plates: corner nodes (analytical), physical (offset-shifted)corner points, area, perimeter, centroid and the local coordinate system. Supports thestandard plate filters and offset/limit pagination; results are sorted by plate Idascending and pagination metadata is returned in response headers (Total-Count, Offset,Limit). Plates whose corner nodes are missing, or whose frame cannot be computed(degenerate geometry), are omitted from the response.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def with_url(self,raw_url: str) -> PlatesRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: PlatesRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return PlatesRequestBuilder(self.request_adapter, raw_url)
    
    @dataclass
    class PlatesRequestBuilderGetQueryParameters():
        """
        Lists derived geometry for plates: corner nodes (analytical), physical (offset-shifted)corner points, area, perimeter, centroid and the local coordinate system. Supports thestandard plate filters and offset/limit pagination; results are sorted by plate Idascending and pagination metadata is returned in response headers (Total-Count, Offset,Limit). Plates whose corner nodes are missing, or whose frame cannot be computed(degenerate geometry), are omitted from the response.
        """
        # Maximum number of items to return. Default is null (return all).
        limit: Optional[int] = None

        # Filter by material number.
        material: Optional[int] = None

        # Number of items to skip from the start of the result set. Default is 0.
        offset: Optional[int] = None

        # Plate Ids to filter by, in SG list format (e.g. `"1,3-7,10"`).Omit to return all plates.
        plates: Optional[str] = None

        # Filter by plate theory (Kirchoff or Mindlin).
        theory: Optional[PlateTheory] = None

    
    @dataclass
    class PlatesRequestBuilderGetRequestConfiguration(RequestConfiguration[PlatesRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

