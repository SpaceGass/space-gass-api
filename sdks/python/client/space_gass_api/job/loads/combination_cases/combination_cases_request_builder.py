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
    from ....models.combination_item import CombinationItem
    from ....models.problem_details import ProblemDetails
    from .bulk.bulk_request_builder import BulkRequestBuilder
    from .item.with_combination_case_item_request_builder import WithCombinationCaseItemRequestBuilder
    from .metadata.metadata_request_builder import MetadataRequestBuilder

class CombinationCasesRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /job/loads/combination-cases
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new CombinationCasesRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/job/loads/combination-cases{?combinationCases*}", path_parameters)
    
    def by_combination_case(self,combination_case: int) -> WithCombinationCaseItemRequestBuilder:
        """
        Gets an item from the space_gass_api.job.loads.combinationCases.item collection
        param combination_case: The combination case Id
        Returns: WithCombinationCaseItemRequestBuilder
        """
        if combination_case is None:
            raise TypeError("combination_case cannot be null.")
        from .item.with_combination_case_item_request_builder import WithCombinationCaseItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["combinationCase"] = combination_case
        return WithCombinationCaseItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[CombinationCasesRequestBuilderGetQueryParameters]] = None) -> Optional[list[CombinationItem]]:
        """
        Returns a flat list of every combination item across every combination case.Each row includes the owning combination case, the component case, and its multiplying factor.Optionally filter by a comma-separated list of combination-case numbers.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[list[CombinationItem]]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ....models.problem_details import ProblemDetails

        error_mapping: dict[str, type[ParsableFactory]] = {
            "401": ProblemDetails,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ....models.combination_item import CombinationItem

        return await self.request_adapter.send_collection_async(request_info, CombinationItem, error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[CombinationCasesRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        Returns a flat list of every combination item across every combination case.Each row includes the owning combination case, the component case, and its multiplying factor.Optionally filter by a comma-separated list of combination-case numbers.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def with_url(self,raw_url: str) -> CombinationCasesRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: CombinationCasesRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return CombinationCasesRequestBuilder(self.request_adapter, raw_url)
    
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
    
    @dataclass
    class CombinationCasesRequestBuilderGetQueryParameters():
        """
        Returns a flat list of every combination item across every combination case.Each row includes the owning combination case, the component case, and its multiplying factor.Optionally filter by a comma-separated list of combination-case numbers.
        """
        def get_query_parameter(self,original_name: str) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            param original_name: The original query parameter name in the class.
            Returns: str
            """
            if original_name is None:
                raise TypeError("original_name cannot be null.")
            if original_name == "combination_cases":
                return "combinationCases"
            return original_name
        
        # Combination case Ids in SG list format (e.g. `"101,103-105"`). Omit to return all.
        combination_cases: Optional[str] = None

    
    @dataclass
    class CombinationCasesRequestBuilderGetRequestConfiguration(RequestConfiguration[CombinationCasesRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

