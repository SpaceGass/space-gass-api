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
    from ......models.mode_shape_query_result import ModeShapeQueryResult
    from ......models.result_sort_order import ResultSortOrder
    from .metadata.metadata_request_builder import MetadataRequestBuilder

class ModeShapesRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /job/query/analysis/dynamic/mode-shapes
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new ModeShapesRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/job/query/analysis/dynamic/mode-shapes{?distinctBy*,limit*,loadCases*,maxAbsRx*,maxAbsRy*,maxAbsRz*,maxAbsTx*,maxAbsTy*,maxAbsTz*,maxNode*,maxRx*,maxRy*,maxRz*,maxTx*,maxTy*,maxTz*,minAbsRx*,minAbsRy*,minAbsRz*,minAbsTx*,minAbsTy*,minAbsTz*,minNode*,minRx*,minRy*,minRz*,minTx*,minTy*,minTz*,modes*,nodes*,normalization*,offset*,order*,sort*}", path_parameters)
    
    # --- @overload added by regen_python_inits.py ---
    @overload
    async def get(
        self,
        *,
        distinct_by: Optional[str] = None,
        limit: Optional[int] = None,
        load_cases: Optional[str] = None,
        max_abs_rx: Optional[float] = None,
        max_abs_ry: Optional[float] = None,
        max_abs_rz: Optional[float] = None,
        max_abs_tx: Optional[float] = None,
        max_abs_ty: Optional[float] = None,
        max_abs_tz: Optional[float] = None,
        max_node: Optional[float] = None,
        max_rx: Optional[float] = None,
        max_ry: Optional[float] = None,
        max_rz: Optional[float] = None,
        max_tx: Optional[float] = None,
        max_ty: Optional[float] = None,
        max_tz: Optional[float] = None,
        min_abs_rx: Optional[float] = None,
        min_abs_ry: Optional[float] = None,
        min_abs_rz: Optional[float] = None,
        min_abs_tx: Optional[float] = None,
        min_abs_ty: Optional[float] = None,
        min_abs_tz: Optional[float] = None,
        min_node: Optional[float] = None,
        min_rx: Optional[float] = None,
        min_ry: Optional[float] = None,
        min_rz: Optional[float] = None,
        min_tx: Optional[float] = None,
        min_ty: Optional[float] = None,
        min_tz: Optional[float] = None,
        modes: Optional[str] = None,
        nodes: Optional[str] = None,
        normalization: Optional[str] = None,
        offset: Optional[int] = None,
        order: Optional[ResultSortOrder] = None,
        sort: Optional[str] = None,
    ) -> Optional[ModeShapeQueryResult]: ...
    @overload
    async def get(self, request_configuration: Optional[RequestConfiguration[ModeShapesRequestBuilderGetQueryParameters]] = None) -> Optional[ModeShapeQueryResult]: ...
    # --- end overloads ---
    async def get(self,request_configuration: Optional[RequestConfiguration[ModeShapesRequestBuilderGetQueryParameters]] = None, **kwargs) -> Optional[ModeShapeQueryResult]:
        """
        Gets mode shape results grouped by load case and mode.Each result contains displacement values at each node.Optionally filtered by load cases, modes and node Ids.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[ModeShapeQueryResult]
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
        from ......models.mode_shape_query_result import ModeShapeQueryResult

        return await self.request_adapter.send_async(request_info, ModeShapeQueryResult, error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[ModeShapesRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        Gets mode shape results grouped by load case and mode.Each result contains displacement values at each node.Optionally filtered by load cases, modes and node Ids.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def with_url(self,raw_url: str) -> ModeShapesRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: ModeShapesRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return ModeShapesRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def metadata(self) -> MetadataRequestBuilder:
        """
        The metadata property
        """
        from .metadata.metadata_request_builder import MetadataRequestBuilder

        return MetadataRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class ModeShapesRequestBuilderGetQueryParameters():
        """
        Gets mode shape results grouped by load case and mode.Each result contains displacement values at each node.Optionally filtered by load cases, modes and node Ids.
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
            if original_name == "max_abs_rx":
                return "maxAbsRx"
            if original_name == "max_abs_ry":
                return "maxAbsRy"
            if original_name == "max_abs_rz":
                return "maxAbsRz"
            if original_name == "max_abs_tx":
                return "maxAbsTx"
            if original_name == "max_abs_ty":
                return "maxAbsTy"
            if original_name == "max_abs_tz":
                return "maxAbsTz"
            if original_name == "max_node":
                return "maxNode"
            if original_name == "max_rx":
                return "maxRx"
            if original_name == "max_ry":
                return "maxRy"
            if original_name == "max_rz":
                return "maxRz"
            if original_name == "max_tx":
                return "maxTx"
            if original_name == "max_ty":
                return "maxTy"
            if original_name == "max_tz":
                return "maxTz"
            if original_name == "min_abs_rx":
                return "minAbsRx"
            if original_name == "min_abs_ry":
                return "minAbsRy"
            if original_name == "min_abs_rz":
                return "minAbsRz"
            if original_name == "min_abs_tx":
                return "minAbsTx"
            if original_name == "min_abs_ty":
                return "minAbsTy"
            if original_name == "min_abs_tz":
                return "minAbsTz"
            if original_name == "min_node":
                return "minNode"
            if original_name == "min_rx":
                return "minRx"
            if original_name == "min_ry":
                return "minRy"
            if original_name == "min_rz":
                return "minRz"
            if original_name == "min_tx":
                return "minTx"
            if original_name == "min_ty":
                return "minTy"
            if original_name == "min_tz":
                return "minTz"
            if original_name == "limit":
                return "limit"
            if original_name == "modes":
                return "modes"
            if original_name == "nodes":
                return "nodes"
            if original_name == "normalization":
                return "normalization"
            if original_name == "offset":
                return "offset"
            if original_name == "order":
                return "order"
            if original_name == "sort":
                return "sort"
            return original_name
        
        # Identity fields: loadCase, mode. One row per value of this identity field: the first row in sort order, i.e. the governingone. `sort=fy&order=AbsDesc&distinctBy=node` returns each node's governingreaction with its load case; `distinctBy=loadCase` each case's governing row. Theidentity fields are the row's Ids (load case, node, member, plate, mode, steel member) orthe reaction summary's `summaryType`, named as in the response and flagged`distinctBy: true` in `GET …/metadata`. Rows come back whole; the count headeris the number of distinct values. Requires `sort`.
        distinct_by: Optional[str] = None

        # Maximum number of items to return. Default is null (return all).
        limit: Optional[int] = None

        # Load case Ids in SG list format (e.g. `"1,3-7,10"`). Omit to return all.
        load_cases: Optional[str] = None

        # Keep rows whose rx has a magnitude of at most this value (in the field's unit, see GET /job/units). Evaluated per station, member end, plate corner or node together with the other range filters: a row is kept when one of its values satisfies them all, and the row is returned whole. Filters select existing values; nothing is interpolated.
        max_abs_rx: Optional[float] = None

        # Keep rows whose ry has a magnitude of at most this value (in the field's unit, see GET /job/units). Evaluated per station, member end, plate corner or node together with the other range filters: a row is kept when one of its values satisfies them all, and the row is returned whole. Filters select existing values; nothing is interpolated.
        max_abs_ry: Optional[float] = None

        # Keep rows whose rz has a magnitude of at most this value (in the field's unit, see GET /job/units). Evaluated per station, member end, plate corner or node together with the other range filters: a row is kept when one of its values satisfies them all, and the row is returned whole. Filters select existing values; nothing is interpolated.
        max_abs_rz: Optional[float] = None

        # Keep rows whose tx has a magnitude of at most this value (in the field's unit, see GET /job/units). Evaluated per station, member end, plate corner or node together with the other range filters: a row is kept when one of its values satisfies them all, and the row is returned whole. Filters select existing values; nothing is interpolated.
        max_abs_tx: Optional[float] = None

        # Keep rows whose ty has a magnitude of at most this value (in the field's unit, see GET /job/units). Evaluated per station, member end, plate corner or node together with the other range filters: a row is kept when one of its values satisfies them all, and the row is returned whole. Filters select existing values; nothing is interpolated.
        max_abs_ty: Optional[float] = None

        # Keep rows whose tz has a magnitude of at most this value (in the field's unit, see GET /job/units). Evaluated per station, member end, plate corner or node together with the other range filters: a row is kept when one of its values satisfies them all, and the row is returned whole. Filters select existing values; nothing is interpolated.
        max_abs_tz: Optional[float] = None

        # Keep rows whose node is at most this value (in the field's unit, see GET /job/units). Evaluated per station, member end, plate corner or node together with the other range filters: a row is kept when one of its values satisfies them all, and the row is returned whole. Filters select existing values; nothing is interpolated.
        max_node: Optional[float] = None

        # Keep rows whose rx is at most this value (in the field's unit, see GET /job/units). Evaluated per station, member end, plate corner or node together with the other range filters: a row is kept when one of its values satisfies them all, and the row is returned whole. Filters select existing values; nothing is interpolated.
        max_rx: Optional[float] = None

        # Keep rows whose ry is at most this value (in the field's unit, see GET /job/units). Evaluated per station, member end, plate corner or node together with the other range filters: a row is kept when one of its values satisfies them all, and the row is returned whole. Filters select existing values; nothing is interpolated.
        max_ry: Optional[float] = None

        # Keep rows whose rz is at most this value (in the field's unit, see GET /job/units). Evaluated per station, member end, plate corner or node together with the other range filters: a row is kept when one of its values satisfies them all, and the row is returned whole. Filters select existing values; nothing is interpolated.
        max_rz: Optional[float] = None

        # Keep rows whose tx is at most this value (in the field's unit, see GET /job/units). Evaluated per station, member end, plate corner or node together with the other range filters: a row is kept when one of its values satisfies them all, and the row is returned whole. Filters select existing values; nothing is interpolated.
        max_tx: Optional[float] = None

        # Keep rows whose ty is at most this value (in the field's unit, see GET /job/units). Evaluated per station, member end, plate corner or node together with the other range filters: a row is kept when one of its values satisfies them all, and the row is returned whole. Filters select existing values; nothing is interpolated.
        max_ty: Optional[float] = None

        # Keep rows whose tz is at most this value (in the field's unit, see GET /job/units). Evaluated per station, member end, plate corner or node together with the other range filters: a row is kept when one of its values satisfies them all, and the row is returned whole. Filters select existing values; nothing is interpolated.
        max_tz: Optional[float] = None

        # Keep rows whose rx has a magnitude of at least this value (in the field's unit, see GET /job/units). Evaluated per station, member end, plate corner or node together with the other range filters: a row is kept when one of its values satisfies them all, and the row is returned whole. Filters select existing values; nothing is interpolated.
        min_abs_rx: Optional[float] = None

        # Keep rows whose ry has a magnitude of at least this value (in the field's unit, see GET /job/units). Evaluated per station, member end, plate corner or node together with the other range filters: a row is kept when one of its values satisfies them all, and the row is returned whole. Filters select existing values; nothing is interpolated.
        min_abs_ry: Optional[float] = None

        # Keep rows whose rz has a magnitude of at least this value (in the field's unit, see GET /job/units). Evaluated per station, member end, plate corner or node together with the other range filters: a row is kept when one of its values satisfies them all, and the row is returned whole. Filters select existing values; nothing is interpolated.
        min_abs_rz: Optional[float] = None

        # Keep rows whose tx has a magnitude of at least this value (in the field's unit, see GET /job/units). Evaluated per station, member end, plate corner or node together with the other range filters: a row is kept when one of its values satisfies them all, and the row is returned whole. Filters select existing values; nothing is interpolated.
        min_abs_tx: Optional[float] = None

        # Keep rows whose ty has a magnitude of at least this value (in the field's unit, see GET /job/units). Evaluated per station, member end, plate corner or node together with the other range filters: a row is kept when one of its values satisfies them all, and the row is returned whole. Filters select existing values; nothing is interpolated.
        min_abs_ty: Optional[float] = None

        # Keep rows whose tz has a magnitude of at least this value (in the field's unit, see GET /job/units). Evaluated per station, member end, plate corner or node together with the other range filters: a row is kept when one of its values satisfies them all, and the row is returned whole. Filters select existing values; nothing is interpolated.
        min_abs_tz: Optional[float] = None

        # Keep rows whose node is at least this value (in the field's unit, see GET /job/units). Evaluated per station, member end, plate corner or node together with the other range filters: a row is kept when one of its values satisfies them all, and the row is returned whole. Filters select existing values; nothing is interpolated.
        min_node: Optional[float] = None

        # Keep rows whose rx is at least this value (in the field's unit, see GET /job/units). Evaluated per station, member end, plate corner or node together with the other range filters: a row is kept when one of its values satisfies them all, and the row is returned whole. Filters select existing values; nothing is interpolated.
        min_rx: Optional[float] = None

        # Keep rows whose ry is at least this value (in the field's unit, see GET /job/units). Evaluated per station, member end, plate corner or node together with the other range filters: a row is kept when one of its values satisfies them all, and the row is returned whole. Filters select existing values; nothing is interpolated.
        min_ry: Optional[float] = None

        # Keep rows whose rz is at least this value (in the field's unit, see GET /job/units). Evaluated per station, member end, plate corner or node together with the other range filters: a row is kept when one of its values satisfies them all, and the row is returned whole. Filters select existing values; nothing is interpolated.
        min_rz: Optional[float] = None

        # Keep rows whose tx is at least this value (in the field's unit, see GET /job/units). Evaluated per station, member end, plate corner or node together with the other range filters: a row is kept when one of its values satisfies them all, and the row is returned whole. Filters select existing values; nothing is interpolated.
        min_tx: Optional[float] = None

        # Keep rows whose ty is at least this value (in the field's unit, see GET /job/units). Evaluated per station, member end, plate corner or node together with the other range filters: a row is kept when one of its values satisfies them all, and the row is returned whole. Filters select existing values; nothing is interpolated.
        min_ty: Optional[float] = None

        # Keep rows whose tz is at least this value (in the field's unit, see GET /job/units). Evaluated per station, member end, plate corner or node together with the other range filters: a row is kept when one of its values satisfies them all, and the row is returned whole. Filters select existing values; nothing is interpolated.
        min_tz: Optional[float] = None

        # Mode numbers in SG list format (e.g. `"1-3"`). Omit to return all.
        modes: Optional[str] = None

        # Node Ids in SG list format (e.g. `"1,5-10"`). Omit to return all.
        nodes: Optional[str] = None

        # Keep rows whose normalization is one of the given values. One or more of: Unknown, Mass, Unit, None (comma-separated, case-insensitive).
        normalization: Optional[str] = None

        # Number of items to skip from the start of the result set. Default is 0.
        offset: Optional[int] = None

        # Sort direction: `Asc` (smallest first, default), `Desc` (largest first),`AbsDesc` (largest magnitude first) or `AbsAsc` (smallest magnitude first).Requires `sort`.
        order: Optional[ResultSortOrder] = None

        # Sortable fields: loadCase, mode, node, tx, ty, tz, rx, ry, rz. Field to sort the rows by, named as in the response (case-insensitive). Any numeric fieldof the endpoint's rows can be used. An array field (values at member stations, member ends,plate corners or nodes) ranks each row by its extreme value in the requested direction, andthe row is returned whole. Rows with no value for the field sort last. Omit to return rows inthe endpoint's default order: its identity fields in order — the fields `GET …/metadata`flags `distinctBy: true`, e.g. load case then node for node results.
        sort: Optional[str] = None

    
    @dataclass
    class ModeShapesRequestBuilderGetRequestConfiguration(RequestConfiguration[ModeShapesRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

