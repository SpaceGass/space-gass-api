"""
Hand-maintained helpers for the steel member design surface — parity with
the C# SDK's ``Utils/SteelDesignExtensions.cs``.

The per-code settings (AS 4100, NZS 3404, ...) are a oneOf in the spec, so
Kiota wraps them in composed types — one per place they appear:

- ``SteelDesignRunCheckRequest_codeSettings``  (``run-check`` body)
- ``SteelDesignRunDesignRequest_codeSettings`` (``run-design`` body)
- ``SettingsPatchRequestBody`` / ``SettingsGetResponse`` (``{code}/settings``)

Raw usage means nesting the code's update object inside the wrapper and
repeating the discriminator (``code="As4100"``). These helpers take the
code's own settings object directly and fill the discriminator in::

    from space_gass_api import steel_design
    import space_gass_api.models as models

    run = await client.job.design.steel_design.by_code(steel_design.AS4100).run_check.post(
        steel_design.run_check_request(
            code_settings=models.SteelMemberDesignSettingsAS4100Update(slenderness_ratio_check=True)))

    settings = await steel_design.patch_as4100(
        client.job.design.steel_design.by_code(steel_design.AS4100).settings,
        models.SteelMemberDesignSettingsAS4100Update(use_kt_factor_for_tension=True))

Lives outside ``generated/`` so it survives Kiota's ``--clean-output``.
"""

from __future__ import annotations

from typing import Optional, Union

from .generated.job.design.steel_design.item.settings.settings_patch_request_body import (
    SettingsPatchRequestBody,
)
from .generated.job.design.steel_design.item.settings.settings_request_builder import (
    SettingsRequestBuilder,
)
from .generated.models.steel_design_run_check_request import SteelDesignRunCheckRequest
from .generated.models.steel_design_run_check_request_code_settings import (
    SteelDesignRunCheckRequest_codeSettings,
)
from .generated.models.steel_design_run_design_request import SteelDesignRunDesignRequest
from .generated.models.steel_design_run_design_request_code_settings import (
    SteelDesignRunDesignRequest_codeSettings,
)
from .generated.models.steel_member_design_general_settings_update import (
    SteelMemberDesignGeneralSettingsUpdate,
)
from .generated.models.steel_member_design_iteration_settings_update import (
    SteelMemberDesignIterationSettingsUpdate,
)
from .generated.models.steel_member_design_settings_a_s4100 import SteelMemberDesignSettingsAS4100
from .generated.models.steel_member_design_settings_a_s4100_update import (
    SteelMemberDesignSettingsAS4100Update,
)
from .generated.models.steel_member_design_settings_n_z_s3404 import SteelMemberDesignSettingsNZS3404
from .generated.models.steel_member_design_settings_n_z_s3404_update import (
    SteelMemberDesignSettingsNZS3404Update,
)

#: Route segment for AS 4100 — ``client.job.design.steel_design.by_code(AS4100)``.
AS4100 = "As4100"
#: Route segment for NZS 3404 — ``client.job.design.steel_design.by_code(NZS3404)``.
NZS3404 = "Nzs3404"

CodeSettingsUpdate = Union[SteelMemberDesignSettingsAS4100Update, SteelMemberDesignSettingsNZS3404Update]

__all__ = [
    "AS4100",
    "NZS3404",
    "CodeSettingsUpdate",
    "code_settings_body",
    "get_as4100",
    "get_nzs3404",
    "patch_as4100",
    "patch_nzs3404",
    "run_check_request",
    "run_design_request",
]


def _with_code(update: CodeSettingsUpdate) -> CodeSettingsUpdate:
    """Fill in the discriminator when the caller didn't — it is fixed per type."""
    if update.code is None:
        update.code = (
            AS4100 if isinstance(update, SteelMemberDesignSettingsAS4100Update) else NZS3404
        )
    return update


def _wrap(wrapper_cls, update: Optional[CodeSettingsUpdate]):
    if update is None:
        return None
    update = _with_code(update)
    if isinstance(update, SteelMemberDesignSettingsAS4100Update):
        return wrapper_cls(steel_member_design_settings_a_s4100_update=update)
    if isinstance(update, SteelMemberDesignSettingsNZS3404Update):
        return wrapper_cls(steel_member_design_settings_n_z_s3404_update=update)
    raise TypeError(
        "code_settings must be a SteelMemberDesignSettingsAS4100Update or "
        f"SteelMemberDesignSettingsNZS3404Update, not {type(update).__name__}"
    )


def run_check_request(
    *,
    settings: Optional[SteelMemberDesignGeneralSettingsUpdate] = None,
    code_settings: Optional[CodeSettingsUpdate] = None,
) -> SteelDesignRunCheckRequest:
    """Body for ``POST /job/design/steel-design/{code}/run-check``.

    ``code_settings`` is the design code's own update object; it is wrapped
    in Kiota's ``SteelDesignRunCheckRequest_codeSettings`` for you.
    """
    return SteelDesignRunCheckRequest(
        settings=settings,
        code_settings=_wrap(SteelDesignRunCheckRequest_codeSettings, code_settings),
    )


def run_design_request(
    *,
    update_sections: Optional[bool] = None,
    design_iteration_settings: Optional[SteelMemberDesignIterationSettingsUpdate] = None,
    settings: Optional[SteelMemberDesignGeneralSettingsUpdate] = None,
    code_settings: Optional[CodeSettingsUpdate] = None,
) -> SteelDesignRunDesignRequest:
    """Body for ``POST /job/design/steel-design/{code}/run-design``.

    ``code_settings`` is the design code's own update object; it is wrapped
    in Kiota's ``SteelDesignRunDesignRequest_codeSettings`` for you.
    """
    return SteelDesignRunDesignRequest(
        update_sections=update_sections,
        design_iteration_settings=design_iteration_settings,
        settings=settings,
        code_settings=_wrap(SteelDesignRunDesignRequest_codeSettings, code_settings),
    )


def code_settings_body(update: CodeSettingsUpdate) -> SettingsPatchRequestBody:
    """Body for ``PATCH /job/design/steel-design/{code}/settings`` from the code's own update object."""
    return _wrap(SettingsPatchRequestBody, update)


async def get_as4100(settings: SettingsRequestBuilder) -> Optional[SteelMemberDesignSettingsAS4100]:
    """Reads the AS 4100 settings from ``client.job.design.steel_design.by_code(AS4100).settings``."""
    response = await settings.get()
    return response.steel_member_design_settings_a_s4100 if response else None


async def get_nzs3404(settings: SettingsRequestBuilder) -> Optional[SteelMemberDesignSettingsNZS3404]:
    """Reads the NZS 3404 settings from ``client.job.design.steel_design.by_code(NZS3404).settings``."""
    response = await settings.get()
    return response.steel_member_design_settings_n_z_s3404 if response else None


async def patch_as4100(
    settings: SettingsRequestBuilder, update: SteelMemberDesignSettingsAS4100Update
) -> Optional[SteelMemberDesignSettingsAS4100]:
    """Partially updates the AS 4100 settings and returns the updated settings."""
    response = await settings.patch(code_settings_body(update))
    return response.steel_member_design_settings_a_s4100 if response else None


async def patch_nzs3404(
    settings: SettingsRequestBuilder, update: SteelMemberDesignSettingsNZS3404Update
) -> Optional[SteelMemberDesignSettingsNZS3404]:
    """Partially updates the NZS 3404 settings and returns the updated settings."""
    response = await settings.patch(code_settings_body(update))
    return response.steel_member_design_settings_n_z_s3404 if response else None
