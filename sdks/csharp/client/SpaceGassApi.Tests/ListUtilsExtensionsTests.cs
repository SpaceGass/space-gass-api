using SpaceGassApi.Utils;
using Xunit;

namespace SpaceGassApi.Tests;

public class ListUtilsExtensionsTests
{
    [Theory]
    [InlineData(new[] { 1, 2, 3, 4, 5 }, "1-5")]
    [InlineData(new[] { 1, 2 }, "1,2")]
    [InlineData(new[] { 5, 3, 1, 4, 2 }, "1-5")]
    [InlineData(new[] { 1, 3, 4, 5, 8, 10 }, "1,3-5,8,10")]
    [InlineData(new[] { 7, 7, 7 }, "7")]
    [InlineData(new[] { -3, 0, 2 }, "2")]
    public void ToFilterString_FormatsSortedDedupedRuns(int[] ids, string expected)
        => Assert.Equal(expected, ids.ToFilterString());

    [Fact]
    public void ToFilterString_TwoConsecutive_StaysExplicitPair()
        => Assert.Equal("3,4", new[] { 4, 3 }.ToFilterString());

    [Fact]
    public void ToFilterString_EmptyInput_ReturnsEmpty()
        => Assert.Equal(string.Empty, Array.Empty<int>().ToFilterString());

    [Fact]
    public void ToFilterString_NullInput_ReturnsEmpty()
        => Assert.Equal(string.Empty, ((IEnumerable<int>)null!).ToFilterString());

    [Fact]
    public void ToFilterString_AllNonPositive_ReturnsEmpty()
        => Assert.Equal(string.Empty, new[] { -1, 0 }.ToFilterString());

    [Theory]
    [InlineData("1-5", new[] { 1, 2, 3, 4, 5 })]
    [InlineData("1,3-5,8", new[] { 1, 3, 4, 5, 8 })]
    [InlineData("7-3", new[] { 3, 4, 5, 6, 7 })]
    [InlineData(" 1 , 2 - 4 ", new[] { 1, 2, 3, 4 })]
    [InlineData("5,1,5", new[] { 1, 5 })]
    [InlineData("", new int[0])]
    [InlineData("   ", new int[0])]
    public void ToIdArray_ParsesRangesAndSingles(string filter, int[] expected)
        => Assert.Equal(expected, filter.ToIdArray());

    [Theory]
    [InlineData("all")]
    [InlineData("ALL")]
    [InlineData("1,x")]
    [InlineData("1-b")]
    [InlineData("0")]
    [InlineData("-5")]
    public void ToIdArray_InvalidInput_ThrowsFormatException(string filter)
        => Assert.Throws<FormatException>(() => filter.ToIdArray());

    [Fact]
    public void ToIdList_MatchesToIdArray()
        => Assert.Equal(new List<int> { 1, 2, 3 }, "1-3".ToIdList());

    [Fact]
    public void FilterString_RoundTrips()
    {
        var ids = new[] { 1, 2, 3, 7, 9, 10, 11, 12, 40 };
        Assert.Equal(ids, ids.ToFilterString().ToIdArray());
    }
}
