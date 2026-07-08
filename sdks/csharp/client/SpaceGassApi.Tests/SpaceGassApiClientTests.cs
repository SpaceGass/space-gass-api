using System.Reflection;
using Microsoft.Kiota.Abstractions;
using Xunit;

namespace SpaceGassApi.Tests;

public class SpaceGassApiClientTests
{
    [Fact]
    public void CreateClient_Default_AppendsApiPathToLocalhost()
        => Assert.Equal("http://localhost:34560/api/v1", BaseUrlOf(SpaceGassApiClient.CreateClient()));

    [Fact]
    public void CreateClient_CustomBaseUrl_TrimsTrailingSlash()
        => Assert.Equal(
            "https://localhost:53484/api/v1",
            BaseUrlOf(SpaceGassApiClient.CreateClient("https://localhost:53484/")));

    private static string BaseUrlOf(SpaceGassApiClient client)
    {
        // RequestAdapter sits on Kiota's BaseRequestBuilder; visibility has
        // changed between Kiota versions, so resolve it reflectively.
        var property = typeof(BaseRequestBuilder).GetProperty(
            "RequestAdapter",
            BindingFlags.Instance | BindingFlags.Public | BindingFlags.NonPublic);
        Assert.NotNull(property);
        var adapter = (IRequestAdapter)property!.GetValue(client)!;
        return adapter.BaseUrl!;
    }
}
