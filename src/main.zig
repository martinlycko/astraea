const std = @import("std");
const scramble = @import("scramble");

const allocator = std.heap.page_allocator;
pub fn main() !void {
    var WordsInJobDescriptions = scramble.WordCounter().init(allocator);
    defer WordsInJobDescriptions.deinit();

    var dir = try std.fs.cwd().openDir("data/textfiles", .{ .iterate = true });
    defer dir.close();

    var iter = dir.iterate();
    while (try iter.next()) |entry| {
        if (entry.kind == .file) {
            std.debug.print("{s} \n", .{entry.name});
            var file = try dir.openFile(entry.name, .{});
            defer file.close();

            const content = try file.readToEndAlloc(allocator, 100000);

            try WordsInJobDescriptions.countwords(content);
        }
    }

    try WordsInJobDescriptions.printorderedwordlist();
}
