const std = @import("std");
const scramble = @import("scramble");

pub fn main() !void {
    _ = scramble.WordCounter();
    std.debug.print("test", .{});
}
