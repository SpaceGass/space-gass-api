using SpaceGassApi.Tests.Support;
using Xunit;

namespace SpaceGassApi.Tests;

public class UploadRequestsTests
{
    [Fact]
    public async Task NewFromTemplateRequest_UploadsFileAsTemplatePart()
    {
        var file = await WriteTempFileAsync("portal.sgbase", "template-bytes");
        try
        {
            var (client, handler) = CapturingHandler.CreateMockedClient();

            await client.Job.NewFromTemplate.PostAsync(new NewFromTemplateRequest(file));

            Assert.Equal("/api/v1/job/new-from-template", handler.Last.Uri.AbsolutePath);
            Assert.StartsWith("multipart/form-data", handler.Last.ContentType);
            Assert.Contains("name=\"template\"", handler.Last.BodyText);
            Assert.Contains("portal.sgbase", handler.Last.BodyText);
            Assert.Contains("template-bytes", handler.Last.BodyText);
        }
        finally
        {
            File.Delete(file);
        }
    }

    [Fact]
    public async Task ImportTxtRequest_UploadsFileAsFilePart()
    {
        var file = await WriteTempFileAsync("model.txt", "import-me");
        try
        {
            var (client, handler) = CapturingHandler.CreateMockedClient();

            await client.Job.Import.Txt.PostAsync(new ImportTxtRequest(file));

            Assert.Equal("/api/v1/job/import/txt", handler.Last.Uri.AbsolutePath);
            Assert.StartsWith("multipart/form-data", handler.Last.ContentType);
            Assert.Contains("name=\"file\"", handler.Last.BodyText);
            Assert.Contains("model.txt", handler.Last.BodyText);
        }
        finally
        {
            File.Delete(file);
        }
    }

    [Fact]
    public void MissingFile_ThrowsFileNotFound()
    {
        var missing = Path.Combine(Path.GetTempPath(), Path.GetRandomFileName(), "missing.sgbase");
        Assert.Throws<FileNotFoundException>(() => new NewFromTemplateRequest(missing));
        Assert.Throws<FileNotFoundException>(() => new ImportTxtRequest(missing));
    }

    private static async Task<string> WriteTempFileAsync(string name, string content)
    {
        var dir = Directory.CreateTempSubdirectory("sg-tests-").FullName;
        var path = Path.Combine(dir, name);
        await File.WriteAllTextAsync(path, content);
        return path;
    }
}
