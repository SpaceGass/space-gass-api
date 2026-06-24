from __future__ import annotations
from collections.abc import Callable
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.request_adapter import RequestAdapter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .member_end_forces.member_end_forces_request_builder import MemberEndForcesRequestBuilder
    from .member_intermediate_displacements.member_intermediate_displacements_request_builder import MemberIntermediateDisplacementsRequestBuilder
    from .member_intermediate_forces.member_intermediate_forces_request_builder import MemberIntermediateForcesRequestBuilder
    from .member_stresses.member_stresses_request_builder import MemberStressesRequestBuilder
    from .node_displacements.node_displacements_request_builder import NodeDisplacementsRequestBuilder
    from .node_reactions.node_reactions_request_builder import NodeReactionsRequestBuilder
    from .plate_element_forces.plate_element_forces_request_builder import PlateElementForcesRequestBuilder
    from .plate_element_stresses.plate_element_stresses_request_builder import PlateElementStressesRequestBuilder
    from .plate_nodal_forces.plate_nodal_forces_request_builder import PlateNodalForcesRequestBuilder
    from .reaction_summary.reaction_summary_request_builder import ReactionSummaryRequestBuilder

class StaticRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /job/query/analysis/static
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new StaticRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/job/query/analysis/static", path_parameters)
    
    @property
    def member_end_forces(self) -> MemberEndForcesRequestBuilder:
        """
        The memberEndForces property
        """
        from .member_end_forces.member_end_forces_request_builder import MemberEndForcesRequestBuilder

        return MemberEndForcesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def member_intermediate_displacements(self) -> MemberIntermediateDisplacementsRequestBuilder:
        """
        The memberIntermediateDisplacements property
        """
        from .member_intermediate_displacements.member_intermediate_displacements_request_builder import MemberIntermediateDisplacementsRequestBuilder

        return MemberIntermediateDisplacementsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def member_intermediate_forces(self) -> MemberIntermediateForcesRequestBuilder:
        """
        The memberIntermediateForces property
        """
        from .member_intermediate_forces.member_intermediate_forces_request_builder import MemberIntermediateForcesRequestBuilder

        return MemberIntermediateForcesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def member_stresses(self) -> MemberStressesRequestBuilder:
        """
        The memberStresses property
        """
        from .member_stresses.member_stresses_request_builder import MemberStressesRequestBuilder

        return MemberStressesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def node_displacements(self) -> NodeDisplacementsRequestBuilder:
        """
        The nodeDisplacements property
        """
        from .node_displacements.node_displacements_request_builder import NodeDisplacementsRequestBuilder

        return NodeDisplacementsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def node_reactions(self) -> NodeReactionsRequestBuilder:
        """
        The nodeReactions property
        """
        from .node_reactions.node_reactions_request_builder import NodeReactionsRequestBuilder

        return NodeReactionsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def plate_element_forces(self) -> PlateElementForcesRequestBuilder:
        """
        The plateElementForces property
        """
        from .plate_element_forces.plate_element_forces_request_builder import PlateElementForcesRequestBuilder

        return PlateElementForcesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def plate_element_stresses(self) -> PlateElementStressesRequestBuilder:
        """
        The plateElementStresses property
        """
        from .plate_element_stresses.plate_element_stresses_request_builder import PlateElementStressesRequestBuilder

        return PlateElementStressesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def plate_nodal_forces(self) -> PlateNodalForcesRequestBuilder:
        """
        The plateNodalForces property
        """
        from .plate_nodal_forces.plate_nodal_forces_request_builder import PlateNodalForcesRequestBuilder

        return PlateNodalForcesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def reaction_summary(self) -> ReactionSummaryRequestBuilder:
        """
        The reactionSummary property
        """
        from .reaction_summary.reaction_summary_request_builder import ReactionSummaryRequestBuilder

        return ReactionSummaryRequestBuilder(self.request_adapter, self.path_parameters)
    

