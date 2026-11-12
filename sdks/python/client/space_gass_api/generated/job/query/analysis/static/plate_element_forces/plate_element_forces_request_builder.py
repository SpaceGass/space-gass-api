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
    from ......models.plate_element_force_query_result import PlateElementForceQueryResult
    from ......models.result_sort_order import ResultSortOrder
    from .metadata.metadata_request_builder import MetadataRequestBuilder

class PlateElementForcesRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /job/query/analysis/static/plate-element-forces
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new PlateElementForcesRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/job/query/analysis/static/plate-element-forces{?distinctBy*,limit*,loadCases*,maxAbsFx*,maxAbsFxy*,maxAbsFy*,maxAbsMx*,maxAbsMxBtm*,maxAbsMxTop*,maxAbsMxy*,maxAbsMy*,maxAbsMyBtm*,maxAbsMyTop*,maxAbsVxz*,maxAbsVyz*,maxFx*,maxFxy*,maxFy*,maxMx*,maxMxBtm*,maxMxTop*,maxMxy*,maxMy*,maxMyBtm*,maxMyTop*,maxVxz*,maxVyz*,minAbsFx*,minAbsFxy*,minAbsFy*,minAbsMx*,minAbsMxBtm*,minAbsMxTop*,minAbsMxy*,minAbsMy*,minAbsMyBtm*,minAbsMyTop*,minAbsVxz*,minAbsVyz*,minFx*,minFxy*,minFy*,minMx*,minMxBtm*,minMxTop*,minMxy*,minMy*,minMyBtm*,minMyTop*,minVxz*,minVyz*,offset*,order*,plates*,sort*}", path_parameters)
    
    # --- @overload added by regen_python_inits.py ---
    @overload
    async def get(
        self,
        *,
        distinct_by: Optional[str] = None,
        limit: Optional[int] = None,
        load_cases: Optional[str] = None,
        max_abs_fx: Optional[float] = None,
        max_abs_fxy: Optional[float] = None,
        max_abs_fy: Optional[float] = None,
        max_abs_mx: Optional[float] = None,
        max_abs_mx_btm: Optional[float] = None,
        max_abs_mx_top: Optional[float] = None,
        max_abs_mxy: Optional[float] = None,
        max_abs_my: Optional[float] = None,
        max_abs_my_btm: Optional[float] = None,
        max_abs_my_top: Optional[float] = None,
        max_abs_vxz: Optional[float] = None,
        max_abs_vyz: Optional[float] = None,
        max_fx: Optional[float] = None,
        max_fxy: Optional[float] = None,
        max_fy: Optional[float] = None,
        max_mx: Optional[float] = None,
        max_mx_btm: Optional[float] = None,
        max_mx_top: Optional[float] = None,
        max_mxy: Optional[float] = None,
        max_my: Optional[float] = None,
        max_my_btm: Optional[float] = None,
        max_my_top: Optional[float] = None,
        max_vxz: Optional[float] = None,
        max_vyz: Optional[float] = None,
        min_abs_fx: Optional[float] = None,
        min_abs_fxy: Optional[float] = None,
        min_abs_fy: Optional[float] = None,
        min_abs_mx: Optional[float] = None,
        min_abs_mx_btm: Optional[float] = None,
        min_abs_mx_top: Optional[float] = None,
        min_abs_mxy: Optional[float] = None,
        min_abs_my: Optional[float] = None,
        min_abs_my_btm: Optional[float] = None,
        min_abs_my_top: Optional[float] = None,
        min_abs_vxz: Optional[float] = None,
        min_abs_vyz: Optional[float] = None,
        min_fx: Optional[float] = None,
        min_fxy: Optional[float] = None,
        min_fy: Optional[float] = None,
        min_mx: Optional[float] = None,
        min_mx_btm: Optional[float] = None,
        min_mx_top: Optional[float] = None,
        min_mxy: Optional[float] = None,
        min_my: Optional[float] = None,
        min_my_btm: Optional[float] = None,
        min_my_top: Optional[float] = None,
        min_vxz: Optional[float] = None,
        min_vyz: Optional[float] = None,
        offset: Optional[int] = None,
        order: Optional[ResultSortOrder] = None,
        plates: Optional[str] = None,
        sort: Optional[str] = None,
    ) -> Optional[PlateElementForceQueryResult]: ...
    @overload
    async def get(self, request_configuration: Optional[RequestConfiguration[PlateElementForcesRequestBuilderGetQueryParameters]] = None) -> Optional[PlateElementForceQueryResult]: ...
    # --- end overloads ---
    async def get(self,request_configuration: Optional[RequestConfiguration[PlateElementForcesRequestBuilderGetQueryParameters]] = None, **kwargs) -> Optional[PlateElementForceQueryResult]:
        """
        Gets element force results for plates, optionally filtered by load cases and plate Ids.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[PlateElementForceQueryResult]
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
        from ......models.plate_element_force_query_result import PlateElementForceQueryResult

        return await self.request_adapter.send_async(request_info, PlateElementForceQueryResult, error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[PlateElementForcesRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        Gets element force results for plates, optionally filtered by load cases and plate Ids.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def with_url(self,raw_url: str) -> PlateElementForcesRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: PlateElementForcesRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return PlateElementForcesRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def metadata(self) -> MetadataRequestBuilder:
        """
        The metadata property
        """
        from .metadata.metadata_request_builder import MetadataRequestBuilder

        return MetadataRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class PlateElementForcesRequestBuilderGetQueryParameters():
        """
        Gets element force results for plates, optionally filtered by load cases and plate Ids.
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
            if original_name == "max_abs_fxy":
                return "maxAbsFxy"
            if original_name == "max_abs_fy":
                return "maxAbsFy"
            if original_name == "max_abs_mx":
                return "maxAbsMx"
            if original_name == "max_abs_mxy":
                return "maxAbsMxy"
            if original_name == "max_abs_mx_btm":
                return "maxAbsMxBtm"
            if original_name == "max_abs_mx_top":
                return "maxAbsMxTop"
            if original_name == "max_abs_my":
                return "maxAbsMy"
            if original_name == "max_abs_my_btm":
                return "maxAbsMyBtm"
            if original_name == "max_abs_my_top":
                return "maxAbsMyTop"
            if original_name == "max_abs_vxz":
                return "maxAbsVxz"
            if original_name == "max_abs_vyz":
                return "maxAbsVyz"
            if original_name == "max_fx":
                return "maxFx"
            if original_name == "max_fxy":
                return "maxFxy"
            if original_name == "max_fy":
                return "maxFy"
            if original_name == "max_mx":
                return "maxMx"
            if original_name == "max_mxy":
                return "maxMxy"
            if original_name == "max_mx_btm":
                return "maxMxBtm"
            if original_name == "max_mx_top":
                return "maxMxTop"
            if original_name == "max_my":
                return "maxMy"
            if original_name == "max_my_btm":
                return "maxMyBtm"
            if original_name == "max_my_top":
                return "maxMyTop"
            if original_name == "max_vxz":
                return "maxVxz"
            if original_name == "max_vyz":
                return "maxVyz"
            if original_name == "min_abs_fx":
                return "minAbsFx"
            if original_name == "min_abs_fxy":
                return "minAbsFxy"
            if original_name == "min_abs_fy":
                return "minAbsFy"
            if original_name == "min_abs_mx":
                return "minAbsMx"
            if original_name == "min_abs_mxy":
                return "minAbsMxy"
            if original_name == "min_abs_mx_btm":
                return "minAbsMxBtm"
            if original_name == "min_abs_mx_top":
                return "minAbsMxTop"
            if original_name == "min_abs_my":
                return "minAbsMy"
            if original_name == "min_abs_my_btm":
                return "minAbsMyBtm"
            if original_name == "min_abs_my_top":
                return "minAbsMyTop"
            if original_name == "min_abs_vxz":
                return "minAbsVxz"
            if original_name == "min_abs_vyz":
                return "minAbsVyz"
            if original_name == "min_fx":
                return "minFx"
            if original_name == "min_fxy":
                return "minFxy"
            if original_name == "min_fy":
                return "minFy"
            if original_name == "min_mx":
                return "minMx"
            if original_name == "min_mxy":
                return "minMxy"
            if original_name == "min_mx_btm":
                return "minMxBtm"
            if original_name == "min_mx_top":
                return "minMxTop"
            if original_name == "min_my":
                return "minMy"
            if original_name == "min_my_btm":
                return "minMyBtm"
            if original_name == "min_my_top":
                return "minMyTop"
            if original_name == "min_vxz":
                return "minVxz"
            if original_name == "min_vyz":
                return "minVyz"
            if original_name == "limit":
                return "limit"
            if original_name == "offset":
                return "offset"
            if original_name == "order":
                return "order"
            if original_name == "plates":
                return "plates"
            if original_name == "sort":
                return "sort"
            return original_name
        
        # Identity fields: loadCase, plate. One row per value of this identity field: the first row in sort order, i.e. the governingone. `sort=fy&order=AbsDesc&distinctBy=node` returns each node's governingreaction with its load case; `distinctBy=loadCase` each case's governing row. Theidentity fields are the row's Ids (load case, node, member, plate, mode, steel member) orthe reaction summary's `summaryType`, named as in the response and flagged`distinctBy: true` in `GET …/metadata`. Rows come back whole; the count headeris the number of distinct values. Requires `sort`.
        distinct_by: Optional[str] = None

        # Maximum number of items to return. Default is null (return all).
        limit: Optional[int] = None

        # Load case Ids in SG list format (e.g. `"1,3-7,10"`). Omit to return all.
        load_cases: Optional[str] = None

        # Keep rows whose fx has a magnitude of at most this value (in the field's unit, see GET /job/units).
        max_abs_fx: Optional[float] = None

        # Keep rows whose fxy has a magnitude of at most this value (in the field's unit, see GET /job/units).
        max_abs_fxy: Optional[float] = None

        # Keep rows whose fy has a magnitude of at most this value (in the field's unit, see GET /job/units).
        max_abs_fy: Optional[float] = None

        # Keep rows whose mx has a magnitude of at most this value (in the field's unit, see GET /job/units).
        max_abs_mx: Optional[float] = None

        # Keep rows whose mxBtm has a magnitude of at most this value (in the field's unit, see GET /job/units).
        max_abs_mx_btm: Optional[float] = None

        # Keep rows whose mxTop has a magnitude of at most this value (in the field's unit, see GET /job/units).
        max_abs_mx_top: Optional[float] = None

        # Keep rows whose mxy has a magnitude of at most this value (in the field's unit, see GET /job/units).
        max_abs_mxy: Optional[float] = None

        # Keep rows whose my has a magnitude of at most this value (in the field's unit, see GET /job/units).
        max_abs_my: Optional[float] = None

        # Keep rows whose myBtm has a magnitude of at most this value (in the field's unit, see GET /job/units).
        max_abs_my_btm: Optional[float] = None

        # Keep rows whose myTop has a magnitude of at most this value (in the field's unit, see GET /job/units).
        max_abs_my_top: Optional[float] = None

        # Keep rows whose vxz has a magnitude of at most this value (in the field's unit, see GET /job/units).
        max_abs_vxz: Optional[float] = None

        # Keep rows whose vyz has a magnitude of at most this value (in the field's unit, see GET /job/units).
        max_abs_vyz: Optional[float] = None

        # Keep rows whose fx is at most this value (in the field's unit, see GET /job/units).
        max_fx: Optional[float] = None

        # Keep rows whose fxy is at most this value (in the field's unit, see GET /job/units).
        max_fxy: Optional[float] = None

        # Keep rows whose fy is at most this value (in the field's unit, see GET /job/units).
        max_fy: Optional[float] = None

        # Keep rows whose mx is at most this value (in the field's unit, see GET /job/units).
        max_mx: Optional[float] = None

        # Keep rows whose mxBtm is at most this value (in the field's unit, see GET /job/units).
        max_mx_btm: Optional[float] = None

        # Keep rows whose mxTop is at most this value (in the field's unit, see GET /job/units).
        max_mx_top: Optional[float] = None

        # Keep rows whose mxy is at most this value (in the field's unit, see GET /job/units).
        max_mxy: Optional[float] = None

        # Keep rows whose my is at most this value (in the field's unit, see GET /job/units).
        max_my: Optional[float] = None

        # Keep rows whose myBtm is at most this value (in the field's unit, see GET /job/units).
        max_my_btm: Optional[float] = None

        # Keep rows whose myTop is at most this value (in the field's unit, see GET /job/units).
        max_my_top: Optional[float] = None

        # Keep rows whose vxz is at most this value (in the field's unit, see GET /job/units).
        max_vxz: Optional[float] = None

        # Keep rows whose vyz is at most this value (in the field's unit, see GET /job/units).
        max_vyz: Optional[float] = None

        # Keep rows whose fx has a magnitude of at least this value (in the field's unit, see GET /job/units).
        min_abs_fx: Optional[float] = None

        # Keep rows whose fxy has a magnitude of at least this value (in the field's unit, see GET /job/units).
        min_abs_fxy: Optional[float] = None

        # Keep rows whose fy has a magnitude of at least this value (in the field's unit, see GET /job/units).
        min_abs_fy: Optional[float] = None

        # Keep rows whose mx has a magnitude of at least this value (in the field's unit, see GET /job/units).
        min_abs_mx: Optional[float] = None

        # Keep rows whose mxBtm has a magnitude of at least this value (in the field's unit, see GET /job/units).
        min_abs_mx_btm: Optional[float] = None

        # Keep rows whose mxTop has a magnitude of at least this value (in the field's unit, see GET /job/units).
        min_abs_mx_top: Optional[float] = None

        # Keep rows whose mxy has a magnitude of at least this value (in the field's unit, see GET /job/units).
        min_abs_mxy: Optional[float] = None

        # Keep rows whose my has a magnitude of at least this value (in the field's unit, see GET /job/units).
        min_abs_my: Optional[float] = None

        # Keep rows whose myBtm has a magnitude of at least this value (in the field's unit, see GET /job/units).
        min_abs_my_btm: Optional[float] = None

        # Keep rows whose myTop has a magnitude of at least this value (in the field's unit, see GET /job/units).
        min_abs_my_top: Optional[float] = None

        # Keep rows whose vxz has a magnitude of at least this value (in the field's unit, see GET /job/units).
        min_abs_vxz: Optional[float] = None

        # Keep rows whose vyz has a magnitude of at least this value (in the field's unit, see GET /job/units).
        min_abs_vyz: Optional[float] = None

        # Keep rows whose fx is at least this value (in the field's unit, see GET /job/units).
        min_fx: Optional[float] = None

        # Keep rows whose fxy is at least this value (in the field's unit, see GET /job/units).
        min_fxy: Optional[float] = None

        # Keep rows whose fy is at least this value (in the field's unit, see GET /job/units).
        min_fy: Optional[float] = None

        # Keep rows whose mx is at least this value (in the field's unit, see GET /job/units).
        min_mx: Optional[float] = None

        # Keep rows whose mxBtm is at least this value (in the field's unit, see GET /job/units).
        min_mx_btm: Optional[float] = None

        # Keep rows whose mxTop is at least this value (in the field's unit, see GET /job/units).
        min_mx_top: Optional[float] = None

        # Keep rows whose mxy is at least this value (in the field's unit, see GET /job/units).
        min_mxy: Optional[float] = None

        # Keep rows whose my is at least this value (in the field's unit, see GET /job/units).
        min_my: Optional[float] = None

        # Keep rows whose myBtm is at least this value (in the field's unit, see GET /job/units).
        min_my_btm: Optional[float] = None

        # Keep rows whose myTop is at least this value (in the field's unit, see GET /job/units).
        min_my_top: Optional[float] = None

        # Keep rows whose vxz is at least this value (in the field's unit, see GET /job/units).
        min_vxz: Optional[float] = None

        # Keep rows whose vyz is at least this value (in the field's unit, see GET /job/units).
        min_vyz: Optional[float] = None

        # Number of items to skip from the start of the result set. Default is 0.
        offset: Optional[int] = None

        # Sort direction: `Asc` (smallest first, default), `Desc` (largest first),`AbsDesc` (largest magnitude first) or `AbsAsc` (smallest magnitude first).Requires `sort`.
        order: Optional[ResultSortOrder] = None

        # Plate Ids in SG list format (e.g. `"1,3-7,10"`). Omit to return all.
        plates: Optional[str] = None

        # Sortable fields: loadCase, plate, fx, fy, fxy, mx, my, mxy, vxz, vyz, mxTop, myTop, mxBtm, myBtm. Field to sort the rows by, named as in the response (case-insensitive). Any numeric fieldof the endpoint's rows can be used. An array field (values at member stations, member ends,plate corners or nodes) ranks each row by its extreme value in the requested direction, andthe row is returned whole. Rows with no value for the field sort last. Omit to return rows inthe endpoint's default order: its identity fields in order — the fields `GET …/metadata`flags `distinctBy: true`, e.g. load case then node for node results.
        sort: Optional[str] = None

    
    @dataclass
    class PlateElementForcesRequestBuilderGetRequestConfiguration(RequestConfiguration[PlateElementForcesRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

