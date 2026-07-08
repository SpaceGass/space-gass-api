using System.Net;
using System.Text.Json;
using SpaceGassApi.Models;
using SpaceGassApi.Tests.Support;
using Xunit;

namespace SpaceGassApi.Tests;

/// <summary>
/// Asserts what actually goes on the wire — URLs, query strings, verbs,
/// serialized bodies — and how error responses map back to typed exceptions.
/// </summary>
public class WireTests
{
    [Fact]
    public async Task Get_WithoutConfiguration_HasNoQueryString()
    {
        var (client, handler) = CapturingHandler.CreateMockedClient(_ => CapturingHandler.Json("[]"));

        await client.Job.Structure.Nodes.GetAsync();

        Assert.Equal(HttpMethod.Get, handler.Last.Method);
        Assert.Equal(string.Empty, handler.Last.Uri.Query);
        Assert.Equal("/api/v1/job/structure/nodes", handler.Last.Uri.AbsolutePath);
    }

    [Fact]
    public async Task Get_WithQueryParameters_PutsThemInTheUrl()
    {
        var (client, handler) = CapturingHandler.CreateMockedClient(_ => CapturingHandler.Json("[]"));

        await client.Job.Structure.Nodes.GetAsync(c =>
            c.QueryParameters.NodeTypeAsNodeTypeFilter = NodeTypeFilter.Restrained);

        Assert.Contains("nodeType=Restrained", handler.Last.Uri.Query);
    }

    [Fact]
    public async Task BulkPost_WithContinueOnError_AddsQueryParameterAndSerializesBody()
    {
        var (client, handler) = CapturingHandler.CreateMockedClient();
        var body = new List<NodeCreate> { new() { X = 1.5, Y = 2.0, Z = 3.0 } };

        await client.Job.Structure.Nodes.Bulk.PostAsync(body, c =>
            c.QueryParameters.ContinueOnError = true);

        Assert.Equal(HttpMethod.Post, handler.Last.Method);
        Assert.Contains("continueOnError=true", handler.Last.Uri.Query);

        using var json = JsonDocument.Parse(handler.Last.BodyText);
        Assert.Equal(1.5, json.RootElement[0].GetProperty("x").GetDouble());
    }

    [Fact]
    public async Task BulkDelete_SendsIdListBody()
    {
        var (client, handler) = CapturingHandler.CreateMockedClient();

        await client.Job.Structure.Nodes.Bulk.DeleteAsync([1, 2, 3]);

        Assert.Equal(HttpMethod.Delete, handler.Last.Method);
        using var json = JsonDocument.Parse(handler.Last.BodyText);
        Assert.Equal(3, json.RootElement.GetArrayLength());
    }

    [Fact]
    public async Task Post_SerializesRequestBodyProperties()
    {
        var (client, handler) = CapturingHandler.CreateMockedClient();

        await client.Job.Open.PostAsync(new OpenJobRequest { FilePath = @"C:\Projects\MyStructure.sg" });

        Assert.Equal("/api/v1/job/open", handler.Last.Uri.AbsolutePath);
        using var json = JsonDocument.Parse(handler.Last.BodyText);
        Assert.Equal(@"C:\Projects\MyStructure.sg", json.RootElement.GetProperty("filePath").GetString());
    }

    [Fact]
    public async Task ErrorBody_SurfacesAsTypedErrorResponseException()
    {
        var (client, _) = CapturingHandler.CreateMockedClient(_ => CapturingHandler.Json(
            """{"title":"Not Found","status":404,"detail":"Node 999 not found","errorCode":"NOT_FOUND"}""",
            HttpStatusCode.NotFound));

        var err = await Assert.ThrowsAsync<ErrorResponse>(
            () => client.Job.Structure.Nodes[999].GetAsync());

        Assert.Equal(404, err.Status);
        Assert.Equal("Node 999 not found", err.Detail);
        Assert.Equal("NOT_FOUND", err.ErrorCode);
    }
}
