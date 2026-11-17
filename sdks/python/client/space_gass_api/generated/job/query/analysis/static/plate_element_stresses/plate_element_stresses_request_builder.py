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
    from ......models.plate_stress_query_result import PlateStressQueryResult
    from ......models.result_sort_order import ResultSortOrder
    from .metadata.metadata_request_builder import MetadataRequestBuilder

class PlateElementStressesRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /job/query/analysis/static/plate-element-stresses
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new PlateElementStressesRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/job/query/analysis/static/plate-element-stresses{?distinctBy*,limit*,loadCases*,maxAbsPaBtm*,maxAbsPaTop*,maxAbsPlasticStrain*,maxAbsSvmBtm*,maxAbsSvmMax*,maxAbsSvmTop*,maxAbsSxBtm*,maxAbsSxTop*,maxAbsSxpBtm*,maxAbsSxpTop*,maxAbsSyBtm*,maxAbsSyTop*,maxAbsSypBtm*,maxAbsSypTop*,maxAbsTmaxBtm*,maxAbsTmaxTop*,maxAbsTxyBtm*,maxAbsTxyTop*,maxAbsTxz*,maxAbsTyz*,maxPaBtm*,maxPaTop*,maxPlasticStrain*,maxSvmBtm*,maxSvmMax*,maxSvmTop*,maxSxBtm*,maxSxTop*,maxSxpBtm*,maxSxpTop*,maxSyBtm*,maxSyTop*,maxSypBtm*,maxSypTop*,maxTmaxBtm*,maxTmaxTop*,maxTxyBtm*,maxTxyTop*,maxTxz*,maxTyz*,minAbsPaBtm*,minAbsPaTop*,minAbsPlasticStrain*,minAbsSvmBtm*,minAbsSvmMax*,minAbsSvmTop*,minAbsSxBtm*,minAbsSxTop*,minAbsSxpBtm*,minAbsSxpTop*,minAbsSyBtm*,minAbsSyTop*,minAbsSypBtm*,minAbsSypTop*,minAbsTmaxBtm*,minAbsTmaxTop*,minAbsTxyBtm*,minAbsTxyTop*,minAbsTxz*,minAbsTyz*,minPaBtm*,minPaTop*,minPlasticStrain*,minSvmBtm*,minSvmMax*,minSvmTop*,minSxBtm*,minSxTop*,minSxpBtm*,minSxpTop*,minSyBtm*,minSyTop*,minSypBtm*,minSypTop*,minTmaxBtm*,minTmaxTop*,minTxyBtm*,minTxyTop*,minTxz*,minTyz*,offset*,order*,plates*,sort*}", path_parameters)
    
    # --- @overload added by regen_python_inits.py ---
    @overload
    async def get(
        self,
        *,
        distinct_by: Optional[str] = None,
        limit: Optional[int] = None,
        load_cases: Optional[str] = None,
        max_abs_pa_btm: Optional[float] = None,
        max_abs_pa_top: Optional[float] = None,
        max_abs_plastic_strain: Optional[float] = None,
        max_abs_svm_btm: Optional[float] = None,
        max_abs_svm_max: Optional[float] = None,
        max_abs_svm_top: Optional[float] = None,
        max_abs_sx_btm: Optional[float] = None,
        max_abs_sx_top: Optional[float] = None,
        max_abs_sxp_btm: Optional[float] = None,
        max_abs_sxp_top: Optional[float] = None,
        max_abs_sy_btm: Optional[float] = None,
        max_abs_sy_top: Optional[float] = None,
        max_abs_syp_btm: Optional[float] = None,
        max_abs_syp_top: Optional[float] = None,
        max_abs_tmax_btm: Optional[float] = None,
        max_abs_tmax_top: Optional[float] = None,
        max_abs_txy_btm: Optional[float] = None,
        max_abs_txy_top: Optional[float] = None,
        max_abs_txz: Optional[float] = None,
        max_abs_tyz: Optional[float] = None,
        max_pa_btm: Optional[float] = None,
        max_pa_top: Optional[float] = None,
        max_plastic_strain: Optional[float] = None,
        max_svm_btm: Optional[float] = None,
        max_svm_max: Optional[float] = None,
        max_svm_top: Optional[float] = None,
        max_sx_btm: Optional[float] = None,
        max_sx_top: Optional[float] = None,
        max_sxp_btm: Optional[float] = None,
        max_sxp_top: Optional[float] = None,
        max_sy_btm: Optional[float] = None,
        max_sy_top: Optional[float] = None,
        max_syp_btm: Optional[float] = None,
        max_syp_top: Optional[float] = None,
        max_tmax_btm: Optional[float] = None,
        max_tmax_top: Optional[float] = None,
        max_txy_btm: Optional[float] = None,
        max_txy_top: Optional[float] = None,
        max_txz: Optional[float] = None,
        max_tyz: Optional[float] = None,
        min_abs_pa_btm: Optional[float] = None,
        min_abs_pa_top: Optional[float] = None,
        min_abs_plastic_strain: Optional[float] = None,
        min_abs_svm_btm: Optional[float] = None,
        min_abs_svm_max: Optional[float] = None,
        min_abs_svm_top: Optional[float] = None,
        min_abs_sx_btm: Optional[float] = None,
        min_abs_sx_top: Optional[float] = None,
        min_abs_sxp_btm: Optional[float] = None,
        min_abs_sxp_top: Optional[float] = None,
        min_abs_sy_btm: Optional[float] = None,
        min_abs_sy_top: Optional[float] = None,
        min_abs_syp_btm: Optional[float] = None,
        min_abs_syp_top: Optional[float] = None,
        min_abs_tmax_btm: Optional[float] = None,
        min_abs_tmax_top: Optional[float] = None,
        min_abs_txy_btm: Optional[float] = None,
        min_abs_txy_top: Optional[float] = None,
        min_abs_txz: Optional[float] = None,
        min_abs_tyz: Optional[float] = None,
        min_pa_btm: Optional[float] = None,
        min_pa_top: Optional[float] = None,
        min_plastic_strain: Optional[float] = None,
        min_svm_btm: Optional[float] = None,
        min_svm_max: Optional[float] = None,
        min_svm_top: Optional[float] = None,
        min_sx_btm: Optional[float] = None,
        min_sx_top: Optional[float] = None,
        min_sxp_btm: Optional[float] = None,
        min_sxp_top: Optional[float] = None,
        min_sy_btm: Optional[float] = None,
        min_sy_top: Optional[float] = None,
        min_syp_btm: Optional[float] = None,
        min_syp_top: Optional[float] = None,
        min_tmax_btm: Optional[float] = None,
        min_tmax_top: Optional[float] = None,
        min_txy_btm: Optional[float] = None,
        min_txy_top: Optional[float] = None,
        min_txz: Optional[float] = None,
        min_tyz: Optional[float] = None,
        offset: Optional[int] = None,
        order: Optional[ResultSortOrder] = None,
        plates: Optional[str] = None,
        sort: Optional[str] = None,
    ) -> Optional[PlateStressQueryResult]: ...
    @overload
    async def get(self, request_configuration: Optional[RequestConfiguration[PlateElementStressesRequestBuilderGetQueryParameters]] = None) -> Optional[PlateStressQueryResult]: ...
    # --- end overloads ---
    async def get(self,request_configuration: Optional[RequestConfiguration[PlateElementStressesRequestBuilderGetQueryParameters]] = None, **kwargs) -> Optional[PlateStressQueryResult]:
        """
        Gets element stress results for plates, optionally filtered by load cases and plate Ids.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[PlateStressQueryResult]
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
        from ......models.plate_stress_query_result import PlateStressQueryResult

        return await self.request_adapter.send_async(request_info, PlateStressQueryResult, error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[PlateElementStressesRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        Gets element stress results for plates, optionally filtered by load cases and plate Ids.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def with_url(self,raw_url: str) -> PlateElementStressesRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: PlateElementStressesRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return PlateElementStressesRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def metadata(self) -> MetadataRequestBuilder:
        """
        The metadata property
        """
        from .metadata.metadata_request_builder import MetadataRequestBuilder

        return MetadataRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class PlateElementStressesRequestBuilderGetQueryParameters():
        """
        Gets element stress results for plates, optionally filtered by load cases and plate Ids.
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
            if original_name == "max_abs_pa_btm":
                return "maxAbsPaBtm"
            if original_name == "max_abs_pa_top":
                return "maxAbsPaTop"
            if original_name == "max_abs_plastic_strain":
                return "maxAbsPlasticStrain"
            if original_name == "max_abs_svm_btm":
                return "maxAbsSvmBtm"
            if original_name == "max_abs_svm_max":
                return "maxAbsSvmMax"
            if original_name == "max_abs_svm_top":
                return "maxAbsSvmTop"
            if original_name == "max_abs_sxp_btm":
                return "maxAbsSxpBtm"
            if original_name == "max_abs_sxp_top":
                return "maxAbsSxpTop"
            if original_name == "max_abs_sx_btm":
                return "maxAbsSxBtm"
            if original_name == "max_abs_sx_top":
                return "maxAbsSxTop"
            if original_name == "max_abs_syp_btm":
                return "maxAbsSypBtm"
            if original_name == "max_abs_syp_top":
                return "maxAbsSypTop"
            if original_name == "max_abs_sy_btm":
                return "maxAbsSyBtm"
            if original_name == "max_abs_sy_top":
                return "maxAbsSyTop"
            if original_name == "max_abs_tmax_btm":
                return "maxAbsTmaxBtm"
            if original_name == "max_abs_tmax_top":
                return "maxAbsTmaxTop"
            if original_name == "max_abs_txy_btm":
                return "maxAbsTxyBtm"
            if original_name == "max_abs_txy_top":
                return "maxAbsTxyTop"
            if original_name == "max_abs_txz":
                return "maxAbsTxz"
            if original_name == "max_abs_tyz":
                return "maxAbsTyz"
            if original_name == "max_pa_btm":
                return "maxPaBtm"
            if original_name == "max_pa_top":
                return "maxPaTop"
            if original_name == "max_plastic_strain":
                return "maxPlasticStrain"
            if original_name == "max_svm_btm":
                return "maxSvmBtm"
            if original_name == "max_svm_max":
                return "maxSvmMax"
            if original_name == "max_svm_top":
                return "maxSvmTop"
            if original_name == "max_sxp_btm":
                return "maxSxpBtm"
            if original_name == "max_sxp_top":
                return "maxSxpTop"
            if original_name == "max_sx_btm":
                return "maxSxBtm"
            if original_name == "max_sx_top":
                return "maxSxTop"
            if original_name == "max_syp_btm":
                return "maxSypBtm"
            if original_name == "max_syp_top":
                return "maxSypTop"
            if original_name == "max_sy_btm":
                return "maxSyBtm"
            if original_name == "max_sy_top":
                return "maxSyTop"
            if original_name == "max_tmax_btm":
                return "maxTmaxBtm"
            if original_name == "max_tmax_top":
                return "maxTmaxTop"
            if original_name == "max_txy_btm":
                return "maxTxyBtm"
            if original_name == "max_txy_top":
                return "maxTxyTop"
            if original_name == "max_txz":
                return "maxTxz"
            if original_name == "max_tyz":
                return "maxTyz"
            if original_name == "min_abs_pa_btm":
                return "minAbsPaBtm"
            if original_name == "min_abs_pa_top":
                return "minAbsPaTop"
            if original_name == "min_abs_plastic_strain":
                return "minAbsPlasticStrain"
            if original_name == "min_abs_svm_btm":
                return "minAbsSvmBtm"
            if original_name == "min_abs_svm_max":
                return "minAbsSvmMax"
            if original_name == "min_abs_svm_top":
                return "minAbsSvmTop"
            if original_name == "min_abs_sxp_btm":
                return "minAbsSxpBtm"
            if original_name == "min_abs_sxp_top":
                return "minAbsSxpTop"
            if original_name == "min_abs_sx_btm":
                return "minAbsSxBtm"
            if original_name == "min_abs_sx_top":
                return "minAbsSxTop"
            if original_name == "min_abs_syp_btm":
                return "minAbsSypBtm"
            if original_name == "min_abs_syp_top":
                return "minAbsSypTop"
            if original_name == "min_abs_sy_btm":
                return "minAbsSyBtm"
            if original_name == "min_abs_sy_top":
                return "minAbsSyTop"
            if original_name == "min_abs_tmax_btm":
                return "minAbsTmaxBtm"
            if original_name == "min_abs_tmax_top":
                return "minAbsTmaxTop"
            if original_name == "min_abs_txy_btm":
                return "minAbsTxyBtm"
            if original_name == "min_abs_txy_top":
                return "minAbsTxyTop"
            if original_name == "min_abs_txz":
                return "minAbsTxz"
            if original_name == "min_abs_tyz":
                return "minAbsTyz"
            if original_name == "min_pa_btm":
                return "minPaBtm"
            if original_name == "min_pa_top":
                return "minPaTop"
            if original_name == "min_plastic_strain":
                return "minPlasticStrain"
            if original_name == "min_svm_btm":
                return "minSvmBtm"
            if original_name == "min_svm_max":
                return "minSvmMax"
            if original_name == "min_svm_top":
                return "minSvmTop"
            if original_name == "min_sxp_btm":
                return "minSxpBtm"
            if original_name == "min_sxp_top":
                return "minSxpTop"
            if original_name == "min_sx_btm":
                return "minSxBtm"
            if original_name == "min_sx_top":
                return "minSxTop"
            if original_name == "min_syp_btm":
                return "minSypBtm"
            if original_name == "min_syp_top":
                return "minSypTop"
            if original_name == "min_sy_btm":
                return "minSyBtm"
            if original_name == "min_sy_top":
                return "minSyTop"
            if original_name == "min_tmax_btm":
                return "minTmaxBtm"
            if original_name == "min_tmax_top":
                return "minTmaxTop"
            if original_name == "min_txy_btm":
                return "minTxyBtm"
            if original_name == "min_txy_top":
                return "minTxyTop"
            if original_name == "min_txz":
                return "minTxz"
            if original_name == "min_tyz":
                return "minTyz"
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

        # Keep rows whose paBtm has a magnitude of at most this value (in the field's unit, see GET /job/units).
        max_abs_pa_btm: Optional[float] = None

        # Keep rows whose paTop has a magnitude of at most this value (in the field's unit, see GET /job/units).
        max_abs_pa_top: Optional[float] = None

        # Keep rows whose plasticStrain has a magnitude of at most this value (in the field's unit, see GET /job/units).
        max_abs_plastic_strain: Optional[float] = None

        # Keep rows whose svmBtm has a magnitude of at most this value (in the field's unit, see GET /job/units).
        max_abs_svm_btm: Optional[float] = None

        # Keep rows whose svmMax has a magnitude of at most this value (in the field's unit, see GET /job/units).
        max_abs_svm_max: Optional[float] = None

        # Keep rows whose svmTop has a magnitude of at most this value (in the field's unit, see GET /job/units).
        max_abs_svm_top: Optional[float] = None

        # Keep rows whose sxBtm has a magnitude of at most this value (in the field's unit, see GET /job/units).
        max_abs_sx_btm: Optional[float] = None

        # Keep rows whose sxTop has a magnitude of at most this value (in the field's unit, see GET /job/units).
        max_abs_sx_top: Optional[float] = None

        # Keep rows whose sxpBtm has a magnitude of at most this value (in the field's unit, see GET /job/units).
        max_abs_sxp_btm: Optional[float] = None

        # Keep rows whose sxpTop has a magnitude of at most this value (in the field's unit, see GET /job/units).
        max_abs_sxp_top: Optional[float] = None

        # Keep rows whose syBtm has a magnitude of at most this value (in the field's unit, see GET /job/units).
        max_abs_sy_btm: Optional[float] = None

        # Keep rows whose syTop has a magnitude of at most this value (in the field's unit, see GET /job/units).
        max_abs_sy_top: Optional[float] = None

        # Keep rows whose sypBtm has a magnitude of at most this value (in the field's unit, see GET /job/units).
        max_abs_syp_btm: Optional[float] = None

        # Keep rows whose sypTop has a magnitude of at most this value (in the field's unit, see GET /job/units).
        max_abs_syp_top: Optional[float] = None

        # Keep rows whose tmaxBtm has a magnitude of at most this value (in the field's unit, see GET /job/units).
        max_abs_tmax_btm: Optional[float] = None

        # Keep rows whose tmaxTop has a magnitude of at most this value (in the field's unit, see GET /job/units).
        max_abs_tmax_top: Optional[float] = None

        # Keep rows whose txyBtm has a magnitude of at most this value (in the field's unit, see GET /job/units).
        max_abs_txy_btm: Optional[float] = None

        # Keep rows whose txyTop has a magnitude of at most this value (in the field's unit, see GET /job/units).
        max_abs_txy_top: Optional[float] = None

        # Keep rows whose txz has a magnitude of at most this value (in the field's unit, see GET /job/units).
        max_abs_txz: Optional[float] = None

        # Keep rows whose tyz has a magnitude of at most this value (in the field's unit, see GET /job/units).
        max_abs_tyz: Optional[float] = None

        # Keep rows whose paBtm is at most this value (in the field's unit, see GET /job/units).
        max_pa_btm: Optional[float] = None

        # Keep rows whose paTop is at most this value (in the field's unit, see GET /job/units).
        max_pa_top: Optional[float] = None

        # Keep rows whose plasticStrain is at most this value (in the field's unit, see GET /job/units).
        max_plastic_strain: Optional[float] = None

        # Keep rows whose svmBtm is at most this value (in the field's unit, see GET /job/units).
        max_svm_btm: Optional[float] = None

        # Keep rows whose svmMax is at most this value (in the field's unit, see GET /job/units).
        max_svm_max: Optional[float] = None

        # Keep rows whose svmTop is at most this value (in the field's unit, see GET /job/units).
        max_svm_top: Optional[float] = None

        # Keep rows whose sxBtm is at most this value (in the field's unit, see GET /job/units).
        max_sx_btm: Optional[float] = None

        # Keep rows whose sxTop is at most this value (in the field's unit, see GET /job/units).
        max_sx_top: Optional[float] = None

        # Keep rows whose sxpBtm is at most this value (in the field's unit, see GET /job/units).
        max_sxp_btm: Optional[float] = None

        # Keep rows whose sxpTop is at most this value (in the field's unit, see GET /job/units).
        max_sxp_top: Optional[float] = None

        # Keep rows whose syBtm is at most this value (in the field's unit, see GET /job/units).
        max_sy_btm: Optional[float] = None

        # Keep rows whose syTop is at most this value (in the field's unit, see GET /job/units).
        max_sy_top: Optional[float] = None

        # Keep rows whose sypBtm is at most this value (in the field's unit, see GET /job/units).
        max_syp_btm: Optional[float] = None

        # Keep rows whose sypTop is at most this value (in the field's unit, see GET /job/units).
        max_syp_top: Optional[float] = None

        # Keep rows whose tmaxBtm is at most this value (in the field's unit, see GET /job/units).
        max_tmax_btm: Optional[float] = None

        # Keep rows whose tmaxTop is at most this value (in the field's unit, see GET /job/units).
        max_tmax_top: Optional[float] = None

        # Keep rows whose txyBtm is at most this value (in the field's unit, see GET /job/units).
        max_txy_btm: Optional[float] = None

        # Keep rows whose txyTop is at most this value (in the field's unit, see GET /job/units).
        max_txy_top: Optional[float] = None

        # Keep rows whose txz is at most this value (in the field's unit, see GET /job/units).
        max_txz: Optional[float] = None

        # Keep rows whose tyz is at most this value (in the field's unit, see GET /job/units).
        max_tyz: Optional[float] = None

        # Keep rows whose paBtm has a magnitude of at least this value (in the field's unit, see GET /job/units).
        min_abs_pa_btm: Optional[float] = None

        # Keep rows whose paTop has a magnitude of at least this value (in the field's unit, see GET /job/units).
        min_abs_pa_top: Optional[float] = None

        # Keep rows whose plasticStrain has a magnitude of at least this value (in the field's unit, see GET /job/units).
        min_abs_plastic_strain: Optional[float] = None

        # Keep rows whose svmBtm has a magnitude of at least this value (in the field's unit, see GET /job/units).
        min_abs_svm_btm: Optional[float] = None

        # Keep rows whose svmMax has a magnitude of at least this value (in the field's unit, see GET /job/units).
        min_abs_svm_max: Optional[float] = None

        # Keep rows whose svmTop has a magnitude of at least this value (in the field's unit, see GET /job/units).
        min_abs_svm_top: Optional[float] = None

        # Keep rows whose sxBtm has a magnitude of at least this value (in the field's unit, see GET /job/units).
        min_abs_sx_btm: Optional[float] = None

        # Keep rows whose sxTop has a magnitude of at least this value (in the field's unit, see GET /job/units).
        min_abs_sx_top: Optional[float] = None

        # Keep rows whose sxpBtm has a magnitude of at least this value (in the field's unit, see GET /job/units).
        min_abs_sxp_btm: Optional[float] = None

        # Keep rows whose sxpTop has a magnitude of at least this value (in the field's unit, see GET /job/units).
        min_abs_sxp_top: Optional[float] = None

        # Keep rows whose syBtm has a magnitude of at least this value (in the field's unit, see GET /job/units).
        min_abs_sy_btm: Optional[float] = None

        # Keep rows whose syTop has a magnitude of at least this value (in the field's unit, see GET /job/units).
        min_abs_sy_top: Optional[float] = None

        # Keep rows whose sypBtm has a magnitude of at least this value (in the field's unit, see GET /job/units).
        min_abs_syp_btm: Optional[float] = None

        # Keep rows whose sypTop has a magnitude of at least this value (in the field's unit, see GET /job/units).
        min_abs_syp_top: Optional[float] = None

        # Keep rows whose tmaxBtm has a magnitude of at least this value (in the field's unit, see GET /job/units).
        min_abs_tmax_btm: Optional[float] = None

        # Keep rows whose tmaxTop has a magnitude of at least this value (in the field's unit, see GET /job/units).
        min_abs_tmax_top: Optional[float] = None

        # Keep rows whose txyBtm has a magnitude of at least this value (in the field's unit, see GET /job/units).
        min_abs_txy_btm: Optional[float] = None

        # Keep rows whose txyTop has a magnitude of at least this value (in the field's unit, see GET /job/units).
        min_abs_txy_top: Optional[float] = None

        # Keep rows whose txz has a magnitude of at least this value (in the field's unit, see GET /job/units).
        min_abs_txz: Optional[float] = None

        # Keep rows whose tyz has a magnitude of at least this value (in the field's unit, see GET /job/units).
        min_abs_tyz: Optional[float] = None

        # Keep rows whose paBtm is at least this value (in the field's unit, see GET /job/units).
        min_pa_btm: Optional[float] = None

        # Keep rows whose paTop is at least this value (in the field's unit, see GET /job/units).
        min_pa_top: Optional[float] = None

        # Keep rows whose plasticStrain is at least this value (in the field's unit, see GET /job/units).
        min_plastic_strain: Optional[float] = None

        # Keep rows whose svmBtm is at least this value (in the field's unit, see GET /job/units).
        min_svm_btm: Optional[float] = None

        # Keep rows whose svmMax is at least this value (in the field's unit, see GET /job/units).
        min_svm_max: Optional[float] = None

        # Keep rows whose svmTop is at least this value (in the field's unit, see GET /job/units).
        min_svm_top: Optional[float] = None

        # Keep rows whose sxBtm is at least this value (in the field's unit, see GET /job/units).
        min_sx_btm: Optional[float] = None

        # Keep rows whose sxTop is at least this value (in the field's unit, see GET /job/units).
        min_sx_top: Optional[float] = None

        # Keep rows whose sxpBtm is at least this value (in the field's unit, see GET /job/units).
        min_sxp_btm: Optional[float] = None

        # Keep rows whose sxpTop is at least this value (in the field's unit, see GET /job/units).
        min_sxp_top: Optional[float] = None

        # Keep rows whose syBtm is at least this value (in the field's unit, see GET /job/units).
        min_sy_btm: Optional[float] = None

        # Keep rows whose syTop is at least this value (in the field's unit, see GET /job/units).
        min_sy_top: Optional[float] = None

        # Keep rows whose sypBtm is at least this value (in the field's unit, see GET /job/units).
        min_syp_btm: Optional[float] = None

        # Keep rows whose sypTop is at least this value (in the field's unit, see GET /job/units).
        min_syp_top: Optional[float] = None

        # Keep rows whose tmaxBtm is at least this value (in the field's unit, see GET /job/units).
        min_tmax_btm: Optional[float] = None

        # Keep rows whose tmaxTop is at least this value (in the field's unit, see GET /job/units).
        min_tmax_top: Optional[float] = None

        # Keep rows whose txyBtm is at least this value (in the field's unit, see GET /job/units).
        min_txy_btm: Optional[float] = None

        # Keep rows whose txyTop is at least this value (in the field's unit, see GET /job/units).
        min_txy_top: Optional[float] = None

        # Keep rows whose txz is at least this value (in the field's unit, see GET /job/units).
        min_txz: Optional[float] = None

        # Keep rows whose tyz is at least this value (in the field's unit, see GET /job/units).
        min_tyz: Optional[float] = None

        # Number of items to skip from the start of the result set. Default is 0.
        offset: Optional[int] = None

        # Sort direction: `Asc` (smallest first, default), `Desc` (largest first),`AbsDesc` (largest magnitude first) or `AbsAsc` (smallest magnitude first).Requires `sort`.
        order: Optional[ResultSortOrder] = None

        # Plate Ids in SG list format (e.g. `"1,3-7,10"`). Omit to return all.
        plates: Optional[str] = None

        # Sortable fields: loadCase, plate, sxTop, syTop, txyTop, sxpTop, sypTop, tmaxTop, svmTop, paTop, sxBtm, syBtm, txyBtm, sxpBtm, sypBtm, tmaxBtm, svmBtm, paBtm, txz, tyz, svmMax, plasticStrain. Field to sort the rows by, named as in the response (case-insensitive). Any numeric fieldof the endpoint's rows can be used. An array field (values at member stations, member ends,plate corners or nodes) ranks each row by its extreme value in the requested direction, andthe row is returned whole. Rows with no value for the field sort last. Omit to return rows inthe endpoint's default order: its identity fields in order — the fields `GET …/metadata`flags `distinctBy: true`, e.g. load case then node for node results.
        sort: Optional[str] = None

    
    @dataclass
    class PlateElementStressesRequestBuilderGetRequestConfiguration(RequestConfiguration[PlateElementStressesRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

