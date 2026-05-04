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
    from .....models.combination_case_update import CombinationCaseUpdate
    from .....models.expand_option import ExpandOption
    from .....models.load_case import LoadCase
    from .....models.problem_details import ProblemDetails
    from .items.items_request_builder import ItemsRequestBuilder

class CombinationCaseItemRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /job/loads/combination-load-cases/{combinationCase-id}
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new CombinationCaseItemRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/job/loads/combination-load-cases/{combinationCase%2Did}{?Expand*}", path_parameters)
    
    async def delete(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> None:
        """
        Deletes the combination load case and all of its component items atomically.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: None
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        from .....models.problem_details import ProblemDetails

        error_mapping: dict[str, type[ParsableFactory]] = {
            "401": ProblemDetails,
            "404": ProblemDetails,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[CombinationCaseItemRequestBuilderGetQueryParameters]] = None) -> Optional[LoadCase]:
        """
        Gets a single combination load case by Id. Returns 404 if no case exists with that Idor if the case is not of type `Combination` (Primary, Step and Unused cases arenot exposed by this endpoint — use `GET /load-cases/{id}` for those).`Expand` defaults to `all`, which hydrates `combinationItems`;pass `Expand=none` to suppress.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[LoadCase]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from .....models.problem_details import ProblemDetails

        error_mapping: dict[str, type[ParsableFactory]] = {
            "401": ProblemDetails,
            "404": ProblemDetails,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .....models.load_case import LoadCase

        return await self.request_adapter.send_async(request_info, LoadCase, error_mapping)
    
    async def patch(self,body: CombinationCaseUpdate, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[LoadCase]:
        """
        Partially updates a combination load case. Only fields supplied in the body arechanged; omitted fields are left as-is. The optional `combinationItems` field isa full-replace when provided — it must be a non-empty list, and the same item rulesfrom create apply (existence, type, no self-reference, no duplicates). Omit`combinationItems` to leave the existing items untouched. To remove all items,delete the case (`DELETE /{id}`).
        param body: Request payload for updating a combination load case.Inherits Id, Title and Notes from SpaceGassApi.Models.Dtos.Entity.Loads.LoadCaseUpdateDto (each optional forpartial update) and adds an optional `combinationItems` list.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[LoadCase]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_patch_request_information(
            body, request_configuration
        )
        from .....models.problem_details import ProblemDetails

        error_mapping: dict[str, type[ParsableFactory]] = {
            "400": ProblemDetails,
            "401": ProblemDetails,
            "404": ProblemDetails,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .....models.load_case import LoadCase

        return await self.request_adapter.send_async(request_info, LoadCase, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Deletes the combination load case and all of its component items atomically.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.DELETE, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[CombinationCaseItemRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        Gets a single combination load case by Id. Returns 404 if no case exists with that Idor if the case is not of type `Combination` (Primary, Step and Unused cases arenot exposed by this endpoint — use `GET /load-cases/{id}` for those).`Expand` defaults to `all`, which hydrates `combinationItems`;pass `Expand=none` to suppress.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_patch_request_information(self,body: CombinationCaseUpdate, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Partially updates a combination load case. Only fields supplied in the body arechanged; omitted fields are left as-is. The optional `combinationItems` field isa full-replace when provided — it must be a non-empty list, and the same item rulesfrom create apply (existence, type, no self-reference, no duplicates). Omit`combinationItems` to leave the existing items untouched. To remove all items,delete the case (`DELETE /{id}`).
        param body: Request payload for updating a combination load case.Inherits Id, Title and Notes from SpaceGassApi.Models.Dtos.Entity.Loads.LoadCaseUpdateDto (each optional forpartial update) and adds an optional `combinationItems` list.
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
    
    def with_url(self,raw_url: str) -> CombinationCaseItemRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: CombinationCaseItemRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return CombinationCaseItemRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def items(self) -> ItemsRequestBuilder:
        """
        The items property
        """
        from .items.items_request_builder import ItemsRequestBuilder

        return ItemsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class CombinationCaseItemRequestBuilderDeleteRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class CombinationCaseItemRequestBuilderGetQueryParameters():
        """
        Gets a single combination load case by Id. Returns 404 if no case exists with that Idor if the case is not of type `Combination` (Primary, Step and Unused cases arenot exposed by this endpoint — use `GET /load-cases/{id}` for those).`Expand` defaults to `all`, which hydrates `combinationItems`;pass `Expand=none` to suppress.
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
        
        # Sub-resource expansion. Defaults to `all`.
        expand: Optional[ExpandOption] = None

    
    @dataclass
    class CombinationCaseItemRequestBuilderGetRequestConfiguration(RequestConfiguration[CombinationCaseItemRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class CombinationCaseItemRequestBuilderPatchRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

