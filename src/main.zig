const std = @import("std");
const scramble = @import("scramble");

const allocator = std.heap.page_allocator;
pub fn main() !void {
    var WordsInJobDescriptions = scramble.WordCounter().init(allocator);
    defer WordsInJobDescriptions.deinit();

    var dir = try std.fs.cwd().openDir("data", .{ .iterate = true });
    defer dir.close();

    var iter = dir.iterate();
    while (try iter.next()) |entry| {
        if (entry.kind == .file) {
            var file = try dir.openFile("Business Intelligence Analyst - Diamond4Jobs.txt", .{});
            defer file.close();

            const content = try file.readToEndAlloc(allocator, 10000);
            defer allocator.free(content);

            try WordsInJobDescriptions.countwords(content);
        }
    }

    try WordsInJobDescriptions.printorderedwordlist();
}
