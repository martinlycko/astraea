const std = @import("std");
const scramble = @import("scramble");

const allocator = std.heap.page_allocator;
pub fn main() !void {
    var dir = try std.fs.cwd().openDir("data", .{});
    defer dir.close();

    var file = try dir.openFile("Business Intelligence Analyst - Diamond4Jobs.txt", .{});
    defer file.close();

    const content = try file.readToEndAlloc(allocator, 10000);
    defer allocator.free(content);

    var WordsInJobDescriptions = scramble.WordCounter().init(allocator);
    defer WordsInJobDescriptions.deinit();

    try WordsInJobDescriptions.countwords(content);

    try WordsInJobDescriptions.printorderedwordlist();
}
