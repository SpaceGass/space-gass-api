import pytest

from space_gass_api import ImportTxtRequest, NewFromTemplateRequest


async def test_new_from_template_uploads_multipart_template_part(client, recorded, tmp_path):
    template = tmp_path / "portal.sgbase"
    template.write_bytes(b"template-bytes")

    await client.job.new_from_template.post(NewFromTemplateRequest(str(template)))

    assert recorded.last.url.path.endswith("/job/new-from-template")
    assert recorded.last.headers["content-type"].startswith("multipart/form-data")
    assert b'name="template"' in recorded.last.content
    assert b"portal.sgbase" in recorded.last.content
    assert b"template-bytes" in recorded.last.content


async def test_import_txt_uploads_multipart_file_part(client, recorded, tmp_path):
    txt = tmp_path / "model.txt"
    txt.write_text("import-me")

    await client.job.import_.txt.post(ImportTxtRequest(str(txt)))

    assert recorded.last.url.path.endswith("/job/import/txt")
    assert recorded.last.headers["content-type"].startswith("multipart/form-data")
    assert b'name="file"' in recorded.last.content
    assert b"model.txt" in recorded.last.content


def test_missing_file_raises(tmp_path):
    missing = str(tmp_path / "missing.sgbase")
    with pytest.raises(FileNotFoundError):
        NewFromTemplateRequest(missing)
    with pytest.raises(FileNotFoundError):
        ImportTxtRequest(missing)
