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
    from ......models.error_response import ErrorResponse
    from ......models.node_reaction_query_result import NodeReactionQueryResult
    from ......models.result_sort_order import ResultSortOrder
    from .metadata.metadata_request_builder import MetadataRequestBuilder

class NodeReactionsRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /job/query/analysis/static/node-reactions
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new NodeReactionsRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/job/query/analysis/static/node-reactions{?distinctBy*,limit*,loadCases*,maxAbsFx*,maxAbsFy*,maxAbsFz*,maxAbsMx*,maxAbsMy*,maxAbsMz*,maxFx*,maxFy*,maxFz*,maxMx*,maxMy*,maxMz*,minAbsFx*,minAbsFy*,minAbsFz*,minAbsMx*,minAbsMy*,minAbsMz*,minFx*,minFy*,minFz*,minMx*,minMy*,minMz*,nodes*,offset*,order*,sort*}", path_parameters)
    
    # --- @overload added by regen_python_inits.py ---
    @overload
    async def get(
        self,
        *,
        distinct_by: Optional[str] = None,
        limit: Optional[int] = None,
        load_cases: Optional[str] = None,
        max_abs_fx: Optional[float] = None,
        max_abs_fy: Optional[float] = None,
        max_abs_fz: Optional[float] = None,
        max_abs_mx: Optional[float] = None,
        max_abs_my: Optional[float] = None,
        max_abs_mz: Optional[float] = None,
        max_fx: Optional[float] = None,
        max_fy: Optional[float] = None,
        max_fz: Optional[float] = None,
        max_mx: Optional[float] = None,
        max_my: Optional[float] = None,
        max_mz: Optional[float] = None,
        min_abs_fx: Optional[float] = None,
        min_abs_fy: Optional[float] = None,
        min_abs_fz: Optional[float] = None,
        min_abs_mx: Optional[float] = None,
        min_abs_my: Optional[float] = None,
        min_abs_mz: Optional[float] = None,
        min_fx: Optional[float] = None,
        min_fy: Optional[float] = None,
        min_fz: Optional[float] = None,
        min_mx: Optional[float] = None,
        min_my: Optional[float] = None,
        min_mz: Optional[float] = None,
        nodes: Optional[str] = None,
        offset: Optional[int] = None,
        order: Optional[ResultSortOrder] = None,
        sort: Optional[str] = None,
    ) -> Optional[NodeReactionQueryResult]: ...
    @overload
    async def get(self, request_configuration: Optional[RequestConfiguration[NodeReactionsRequestBuilderGetQueryParameters]] = None) -> Optional[NodeReactionQueryResult]: ...
    # --- end overloads ---
    async def get(self,request_configuration: Optional[RequestConfiguration[NodeReactionsRequestBuilderGetQueryParameters]] = None, **kwargs) -> Optional[NodeReactionQueryResult]:
        """
        Gets reaction results at restrained nodes, optionally filtered by load cases and node Ids.Returns per-node reactions only — the per-load-case equilibrium totals (sum of loads,sum of reactions, maximum residuals) are available from `GET reaction-summary`.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[NodeReactionQueryResult]
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
        from ......models.node_reaction_query_result import NodeReactionQueryResult

        return await self.request_adapter.send_async(request_info, NodeReactionQueryResult, error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[NodeReactionsRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        Gets reaction results at restrained nodes, optionally filtered by load cases and node Ids.Returns per-node reactions only — the per-load-case equilibrium totals (sum of loads,sum of reactions, maximum residuals) are available from `GET reaction-summary`.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def with_url(self,raw_url: str) -> NodeReactionsRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: NodeReactionsRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return NodeReactionsRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def metadata(self) -> MetadataRequestBuilder:
        """
        The metadata property
        """
        from .metadata.metadata_request_builder import MetadataRequestBuilder

        return MetadataRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class NodeReactionsRequestBuilderGetQueryParameters():
        """
        Gets reaction results at restrained nodes, optionally filtered by load cases and node Ids.Returns per-node reactions only — the per-load-case equilibrium totals (sum of loads,sum of reactions, maximum residuals) are available from `GET reaction-summary`.
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
            if original_name == "max_abs_fx":
                return "maxAbsFx"
            if original_name == "max_abs_fy":
                return "maxAbsFy"
            if original_name == "max_abs_fz":
                return "maxAbsFz"
            if original_name == "max_abs_mx":
                return "maxAbsMx"
            if original_name == "max_abs_my":
                return "maxAbsMy"
            if original_name == "max_abs_mz":
                return "maxAbsMz"
            if original_name == "max_fx":
                return "maxFx"
            if original_name == "max_fy":
                return "maxFy"
            if original_name == "max_fz":
                return "maxFz"
            if original_name == "max_mx":
                return "maxMx"
            if original_name == "max_my":
                return "maxMy"
            if original_name == "max_mz":
                return "maxMz"
            if original_name == "min_abs_fx":
                return "minAbsFx"
            if original_name == "min_abs_fy":
                return "minAbsFy"
            if original_name == "min_abs_fz":
                return "minAbsFz"
            if original_name == "min_abs_mx":
                return "minAbsMx"
            if original_name == "min_abs_my":
                return "minAbsMy"
            if original_name == "min_abs_mz":
                return "minAbsMz"
            if original_name == "min_fx":
                return "minFx"
            if original_name == "min_fy":
                return "minFy"
            if original_name == "min_fz":
                return "minFz"
            if original_name == "min_mx":
                return "minMx"
            if original_name == "min_my":
                return "minMy"
            if original_name == "min_mz":
                return "minMz"
            if original_name == "limit":
                return "limit"
            if original_name == "nodes":
                return "nodes"
            if original_name == "offset":
                return "offset"
            if original_name == "order":
                return "order"
            if original_name == "sort":
                return "sort"
            return original_name
        
        # Identity fields: loadCase, node. One row per value of this identity field: the first row in sort order, i.e. the governingone. `sort=fy&order=AbsDesc&distinctBy=node` returns each node's governingreaction with its load case; `distinctBy=loadCase` each case's governing row. Theidentity fields are the row's Ids (load case, node, member, plate, mode, steel member) orthe reaction summary's `summaryType`, named as in the response and flagged`distinctBy: true` in `GET …/metadata`. Rows come back whole; the count headeris the number of distinct values. Requires `sort`.
        distinct_by: Optional[str] = None

        # Maximum number of items to return. Default is null (return all).
        limit: Optional[int] = None

        # Load case Ids in SG list format (e.g. `"1,3-7,10"`). Omit to return all.
        load_cases: Optional[str] = None

        # Keep rows whose fx has a magnitude of at most this value (in the field's unit, see GET /job/units).
        max_abs_fx: Optional[float] = None

        # Keep rows whose fy has a magnitude of at most this value (in the field's unit, see GET /job/units).
        max_abs_fy: Optional[float] = None

        # Keep rows whose fz has a magnitude of at most this value (in the field's unit, see GET /job/units).
        max_abs_fz: Optional[float] = None

        # Keep rows whose mx has a magnitude of at most this value (in the field's unit, see GET /job/units).
        max_abs_mx: Optional[float] = None

        # Keep rows whose my has a magnitude of at most this value (in the field's unit, see GET /job/units).
        max_abs_my: Optional[float] = None

        # Keep rows whose mz has a magnitude of at most this value (in the field's unit, see GET /job/units).
        max_abs_mz: Optional[float] = None

        # Keep rows whose fx is at most this value (in the field's unit, see GET /job/units).
        max_fx: Optional[float] = None

        # Keep rows whose fy is at most this value (in the field's unit, see GET /job/units).
        max_fy: Optional[float] = None

        # Keep rows whose fz is at most this value (in the field's unit, see GET /job/units).
        max_fz: Optional[float] = None

        # Keep rows whose mx is at most this value (in the field's unit, see GET /job/units).
        max_mx: Optional[float] = None

        # Keep rows whose my is at most this value (in the field's unit, see GET /job/units).
        max_my: Optional[float] = None

        # Keep rows whose mz is at most this value (in the field's unit, see GET /job/units).
        max_mz: Optional[float] = None

        # Keep rows whose fx has a magnitude of at least this value (in the field's unit, see GET /job/units).
        min_abs_fx: Optional[float] = None

        # Keep rows whose fy has a magnitude of at least this value (in the field's unit, see GET /job/units).
        min_abs_fy: Optional[float] = None

        # Keep rows whose fz has a magnitude of at least this value (in the field's unit, see GET /job/units).
        min_abs_fz: Optional[float] = None

        # Keep rows whose mx has a magnitude of at least this value (in the field's unit, see GET /job/units).
        min_abs_mx: Optional[float] = None

        # Keep rows whose my has a magnitude of at least this value (in the field's unit, see GET /job/units).
        min_abs_my: Optional[float] = None

        # Keep rows whose mz has a magnitude of at least this value (in the field's unit, see GET /job/units).
        min_abs_mz: Optional[float] = None

        # Keep rows whose fx is at least this value (in the field's unit, see GET /job/units).
        min_fx: Optional[float] = None

        # Keep rows whose fy is at least this value (in the field's unit, see GET /job/units).
        min_fy: Optional[float] = None

        # Keep rows whose fz is at least this value (in the field's unit, see GET /job/units).
        min_fz: Optional[float] = None

        # Keep rows whose mx is at least this value (in the field's unit, see GET /job/units).
        min_mx: Optional[float] = None

        # Keep rows whose my is at least this value (in the field's unit, see GET /job/units).
        min_my: Optional[float] = None

        # Keep rows whose mz is at least this value (in the field's unit, see GET /job/units).
        min_mz: Optional[float] = None

        # Node Ids in SG list format (e.g. `"1,5-10"`). Omit to return all.
        nodes: Optional[str] = None

        # Number of items to skip from the start of the result set. Default is 0.
        offset: Optional[int] = None

        # Sort direction: `Asc` (smallest first, default), `Desc` (largest first),`AbsDesc` (largest magnitude first) or `AbsAsc` (smallest magnitude first).Requires `sort`.
        order: Optional[ResultSortOrder] = None

        # Sortable fields: loadCase, node, fx, fy, fz, mx, my, mz. Field to sort the rows by, named as in the response (case-insensitive). Any numeric fieldof the endpoint's rows can be used. An array field (values at member stations, member ends,plate corners or nodes) ranks each row by its extreme value in the requested direction, andthe row is returned whole. Rows with no value for the field sort last. Omit to return rows inthe endpoint's default order: its identity fields in order — the fields `GET …/metadata`flags `distinctBy: true`, e.g. load case then node for node results.
        sort: Optional[str] = None

    
    @dataclass
    class NodeReactionsRequestBuilderGetRequestConfiguration(RequestConfiguration[NodeReactionsRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

