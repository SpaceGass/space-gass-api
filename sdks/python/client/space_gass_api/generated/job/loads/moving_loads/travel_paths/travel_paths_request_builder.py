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
    from .....models.moving_load_travel_path import MovingLoadTravelPath
    from .....models.moving_load_travel_path_create import MovingLoadTravelPathCreate
    from .bulk.bulk_request_builder import BulkRequestBuilder
    from .item.travel_paths_item_request_builder import TravelPathsItemRequestBuilder
    from .metadata.metadata_request_builder import MetadataRequestBuilder
    from .stations.stations_request_builder import StationsRequestBuilder

class TravelPathsRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /job/loads/moving-loads/travel-paths
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new TravelPathsRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/job/loads/moving-loads/travel-paths{?Expand*}", path_parameters)
    
    def by_id(self,id: int) -> TravelPathsItemRequestBuilder:
        """
        Gets an item from the space_gass_api.generated.job.loads.movingLoads.travelPaths.item collection
        param id: The item Id
        Returns: TravelPathsItemRequestBuilder
        """
        if id is None:
            raise TypeError("id cannot be null.")
        from .item.travel_paths_item_request_builder import TravelPathsItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["id"] = id
        return TravelPathsItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    # --- @overload added by regen_python_inits.py ---
    @overload
    async def get(
        self,
        *,
        expand: Optional[ExpandOption] = None,
    ) -> Optional[list[MovingLoadTravelPath]]: ...
    @overload
    async def get(self, request_configuration: Optional[RequestConfiguration[TravelPathsRequestBuilderGetQueryParameters]] = None) -> Optional[list[MovingLoadTravelPath]]: ...
    # --- end overloads ---
    async def get(self,request_configuration: Optional[RequestConfiguration[TravelPathsRequestBuilderGetQueryParameters]] = None, **kwargs) -> Optional[list[MovingLoadTravelPath]]:
        """
        Lists all items in this catalog for the current job, ordered by Id.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[list[MovingLoadTravelPath]]
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
        from .....models.moving_load_travel_path import MovingLoadTravelPath

        return await self.request_adapter.send_collection_async(request_info, MovingLoadTravelPath, error_mapping)
    
    async def post(self,body: MovingLoadTravelPathCreate, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[MovingLoadTravelPath]:
        """
        Creates a new catalog item.
        param body: Creates a new travel-path header. Stations are set via `PUT moving-loads/travel-paths/{id}/stations`.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[MovingLoadTravelPath]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_post_request_information(
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
        from .....models.moving_load_travel_path import MovingLoadTravelPath

        return await self.request_adapter.send_async(request_info, MovingLoadTravelPath, error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[TravelPathsRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        Lists all items in this catalog for the current job, ordered by Id.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_post_request_information(self,body: MovingLoadTravelPathCreate, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Creates a new catalog item.
        param body: Creates a new travel-path header. Stations are set via `PUT moving-loads/travel-paths/{id}/stations`.
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
    
    def with_url(self,raw_url: str) -> TravelPathsRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: TravelPathsRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return TravelPathsRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def bulk(self) -> BulkRequestBuilder:
        """
        The bulk property
        """
        from .bulk.bulk_request_builder import BulkRequestBuilder

        return BulkRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def metadata(self) -> MetadataRequestBuilder:
        """
        The metadata property
        """
        from .metadata.metadata_request_builder import MetadataRequestBuilder

        return MetadataRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def stations(self) -> StationsRequestBuilder:
        """
        The stations property
        """
        from .stations.stations_request_builder import StationsRequestBuilder

        return StationsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class TravelPathsRequestBuilderGetQueryParameters():
        """
        Lists all items in this catalog for the current job, ordered by Id.
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
        
        # Whether to hydrate each item's sub-resources inline. Defaults to None for the list.
        expand: Optional[ExpandOption] = None

    
    @dataclass
    class TravelPathsRequestBuilderGetRequestConfiguration(RequestConfiguration[TravelPathsRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class TravelPathsRequestBuilderPostRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

