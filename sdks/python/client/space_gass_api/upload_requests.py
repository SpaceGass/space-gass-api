"""
Hand-maintained multipart upload request bodies — parity with the C# SDK's
``NewFromTemplateRequest`` / ``ImportTxtRequest``.

These subclass Kiota's ``MultipartBody`` so the multipart file-upload
endpoints can be called by file path instead of assembling a
``MultipartBody`` by hand::

    from space_gass_api import NewFromTemplateRequest, ImportTxtRequest

    await client.job.new_from_template.post(NewFromTemplateRequest("design.sgbase"))
    await client.job.import_.txt.post(ImportTxtRequest("model.txt"))

They live outside ``generated/`` so they survive Kiota's ``--clean-output``.
No request adapter is set here — the request builder attaches it at send
time (Kiota's ``set_content_from_parsable``).
"""

from __future__ import annotations

from pathlib import Path

from kiota_abstractions.multipart_body import MultipartBody


def _add_file(body: MultipartBody, part_name: str, file_path: str) -> None:
    path = Path(file_path)
    if not path.is_file():
        raise FileNotFoundError(f"File not found: {file_path}")
    body.add_or_replace_part(
        part_name, "application/octet-stream", path.read_bytes(), path.name
    )


class NewFromTemplateRequest(MultipartBody):
    """Multipart request body for ``POST /job/new-from-template``.

    Construct from a SPACE GASS template (``.sgbase``/``.SG``) file path::

        await client.job.new_from_template.post(NewFromTemplateRequest(path))
    """

    def __init__(self, file_path: str) -> None:
        super().__init__()
        _add_file(self, "template", file_path)


class ImportTxtRequest(MultipartBody):
    """Multipart request body for ``POST /job/import/txt``.

    Construct from a SPACE GASS text (``.txt``) file path::

        await client.job.import_.txt.post(ImportTxtRequest(path))
    """

    def __init__(self, file_path: str) -> None:
        super().__init__()
        _add_file(self, "file", file_path)
