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
    from ......models.buckling_load_factor_query_result import BucklingLoadFactorQueryResult
    from ......models.error_response import ErrorResponse
    from ......models.result_sort_order import ResultSortOrder
    from .metadata.metadata_request_builder import MetadataRequestBuilder

class LoadFactorsRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /job/query/analysis/buckling/load-factors
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new LoadFactorsRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/job/query/analysis/buckling/load-factors{?distinctBy*,limit*,loadCases*,maxAbsLoadFactor*,maxAbsTolerance*,maxIterations*,maxLoadFactor*,maxNodeAtMaxRotn*,maxNodeAtMaxTrans*,maxTolerance*,minAbsLoadFactor*,minAbsTolerance*,minIterations*,minLoadFactor*,minNodeAtMaxRotn*,minNodeAtMaxTrans*,minTolerance*,modes*,offset*,order*,rotnAxis*,sort*,status*,transAxis*,warning*}", path_parameters)
    
    # --- @overload added by regen_python_inits.py ---
    @overload
    async def get(
        self,
        *,
        distinct_by: Optional[str] = None,
        limit: Optional[int] = None,
        load_cases: Optional[str] = None,
        max_abs_load_factor: Optional[float] = None,
        max_abs_tolerance: Optional[float] = None,
        max_iterations: Optional[float] = None,
        max_load_factor: Optional[float] = None,
        max_node_at_max_rotn: Optional[float] = None,
        max_node_at_max_trans: Optional[float] = None,
        max_tolerance: Optional[float] = None,
        min_abs_load_factor: Optional[float] = None,
        min_abs_tolerance: Optional[float] = None,
        min_iterations: Optional[float] = None,
        min_load_factor: Optional[float] = None,
        min_node_at_max_rotn: Optional[float] = None,
        min_node_at_max_trans: Optional[float] = None,
        min_tolerance: Optional[float] = None,
        modes: Optional[str] = None,
        offset: Optional[int] = None,
        order: Optional[ResultSortOrder] = None,
        rotn_axis: Optional[str] = None,
        sort: Optional[str] = None,
        status: Optional[str] = None,
        trans_axis: Optional[str] = None,
        warning: Optional[str] = None,
    ) -> Optional[BucklingLoadFactorQueryResult]: ...
    @overload
    async def get(self, request_configuration: Optional[RequestConfiguration[LoadFactorsRequestBuilderGetQueryParameters]] = None) -> Optional[BucklingLoadFactorQueryResult]: ...
    # --- end overloads ---
    async def get(self,request_configuration: Optional[RequestConfiguration[LoadFactorsRequestBuilderGetQueryParameters]] = None, **kwargs) -> Optional[BucklingLoadFactorQueryResult]:
        """
        Gets buckling load factor results, optionally filtered by load cases and modes.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[BucklingLoadFactorQueryResult]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ......models.error_response import ErrorResponse

        error_mapping: dict[str, type[ParsableFactory]] = {
            "400": ErrorResponse,
            "403": ErrorResponse,
            "404": ErrorResponse,
            "409": ErrorResponse,
            "500": ErrorResponse,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ......models.buckling_load_factor_query_result import BucklingLoadFactorQueryResult

        return await self.request_adapter.send_async(request_info, BucklingLoadFactorQueryResult, error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[LoadFactorsRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        Gets buckling load factor results, optionally filtered by load cases and modes.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def with_url(self,raw_url: str) -> LoadFactorsRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: LoadFactorsRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return LoadFactorsRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def metadata(self) -> MetadataRequestBuilder:
        """
        The metadata property
        """
        from .metadata.metadata_request_builder import MetadataRequestBuilder

        return MetadataRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class LoadFactorsRequestBuilderGetQueryParameters():
        """
        Gets buckling load factor results, optionally filtered by load cases and modes.
        """
        def get_query_parameter(self,original_name: str) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            param original_name: The original query parameter name in the class.
            Returns: str
            """
            if original_name is None:
                raise TypeError("original_name cannot be null.")
            if original_name == "distinct_by":
                return "distinctBy"
            if original_name == "load_cases":
                return "loadCases"
            if original_name == "max_abs_load_factor":
                return "maxAbsLoadFactor"
            if original_name == "max_abs_tolerance":
                return "maxAbsTolerance"
            if original_name == "max_iterations":
                return "maxIterations"
            if original_name == "max_load_factor":
                return "maxLoadFactor"
            if original_name == "max_node_at_max_rotn":
                return "maxNodeAtMaxRotn"
            if original_name == "max_node_at_max_trans":
                return "maxNodeAtMaxTrans"
            if original_name == "max_tolerance":
                return "maxTolerance"
            if original_name == "min_abs_load_factor":
                return "minAbsLoadFactor"
            if original_name == "min_abs_tolerance":
                return "minAbsTolerance"
            if original_name == "min_iterations":
                return "minIterations"
            if original_name == "min_load_factor":
                return "minLoadFactor"
            if original_name == "min_node_at_max_rotn":
                return "minNodeAtMaxRotn"
            if original_name == "min_node_at_max_trans":
                return "minNodeAtMaxTrans"
            if original_name == "min_tolerance":
                return "minTolerance"
            if original_name == "rotn_axis":
                return "rotnAxis"
            if original_name == "trans_axis":
                return "transAxis"
            if original_name == "limit":
                return "limit"
            if original_name == "modes":
                return "modes"
            if original_name == "offset":
                return "offset"
            if original_name == "order":
                return "order"
            if original_name == "sort":
                return "sort"
            if original_name == "status":
                return "status"
            if original_name == "warning":
                return "warning"
            return original_name
        
        # Identity fields: loadCase, mode. One row per value of this identity field: the first row in sort order, i.e. the governingone. `sort=fy&order=AbsDesc&distinctBy=node` returns each node's governingreaction with its load case; `distinctBy=loadCase` each case's governing row. Theidentity fields are the row's Ids (load case, node, member, plate, mode, steel member) orthe reaction summary's `summaryType`, named as in the response and flagged`distinctBy: true` in `GET …/metadata`. Rows come back whole; the count headeris the number of distinct values. Requires `sort`.
        distinct_by: Optional[str] = None

        # Maximum number of items to return. Default is null (return all).
        limit: Optional[int] = None

        # Load case Ids in SG list format (e.g. `"1,3-7,10"`). Omit to return all.
        load_cases: Optional[str] = None

        # Keep rows whose loadFactor has a magnitude of at most this value (in the field's unit, see GET /job/units).
        max_abs_load_factor: Optional[float] = None

        # Keep rows whose tolerance has a magnitude of at most this value (in the field's unit, see GET /job/units).
        max_abs_tolerance: Optional[float] = None

        # Keep rows whose iterations is at most this value (in the field's unit, see GET /job/units).
        max_iterations: Optional[float] = None

        # Keep rows whose loadFactor is at most this value (in the field's unit, see GET /job/units).
        max_load_factor: Optional[float] = None

        # Keep rows whose nodeAtMaxRotn is at most this value (in the field's unit, see GET /job/units).
        max_node_at_max_rotn: Optional[float] = None

        # Keep rows whose nodeAtMaxTrans is at most this value (in the field's unit, see GET /job/units).
        max_node_at_max_trans: Optional[float] = None

        # Keep rows whose tolerance is at most this value (in the field's unit, see GET /job/units).
        max_tolerance: Optional[float] = None

        # Keep rows whose loadFactor has a magnitude of at least this value (in the field's unit, see GET /job/units).
        min_abs_load_factor: Optional[float] = None

        # Keep rows whose tolerance has a magnitude of at least this value (in the field's unit, see GET /job/units).
        min_abs_tolerance: Optional[float] = None

        # Keep rows whose iterations is at least this value (in the field's unit, see GET /job/units).
        min_iterations: Optional[float] = None

        # Keep rows whose loadFactor is at least this value (in the field's unit, see GET /job/units).
        min_load_factor: Optional[float] = None

        # Keep rows whose nodeAtMaxRotn is at least this value (in the field's unit, see GET /job/units).
        min_node_at_max_rotn: Optional[float] = None

        # Keep rows whose nodeAtMaxTrans is at least this value (in the field's unit, see GET /job/units).
        min_node_at_max_trans: Optional[float] = None

        # Keep rows whose tolerance is at least this value (in the field's unit, see GET /job/units).
        min_tolerance: Optional[float] = None

        # Buckling mode numbers in SG list format (e.g. `"1-3"`). Omit to return all.
        modes: Optional[str] = None

        # Number of items to skip from the start of the result set. Default is 0.
        offset: Optional[int] = None

        # Sort direction: `Asc` (smallest first, default), `Desc` (largest first),`AbsDesc` (largest magnitude first) or `AbsAsc` (smallest magnitude first).Requires `sort`.
        order: Optional[ResultSortOrder] = None

        # Keep rows whose rotnAxis is one of the given values. One or more values, comma-separated, matched case-insensitively.
        rotn_axis: Optional[str] = None

        # Sortable fields: loadCase, mode, loadFactor, tolerance, iterations, nodeAtMaxTrans, nodeAtMaxRotn. Field to sort the rows by, named as in the response (case-insensitive). Any numeric fieldof the endpoint's rows can be used. An array field (values at member stations, member ends,plate corners or nodes) ranks each row by its extreme value in the requested direction, andthe row is returned whole. Rows with no value for the field sort last. Omit to return rows inthe endpoint's default order: its identity fields in order — the fields `GET …/metadata`flags `distinctBy: true`, e.g. load case then node for node results.
        sort: Optional[str] = None

        # Keep rows whose status is one of the given values. One or more of: Reported, AboveUpperLimit, BelowLowerLimit, Unstable (comma-separated, case-insensitive).
        status: Optional[str] = None

        # Keep rows whose transAxis is one of the given values. One or more values, comma-separated, matched case-insensitively.
        trans_axis: Optional[str] = None

        # Keep rows whose warning is one of the given values. One or more values, comma-separated, matched case-insensitively.
        warning: Optional[str] = None

    
    @dataclass
    class LoadFactorsRequestBuilderGetRequestConfiguration(RequestConfiguration[LoadFactorsRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

