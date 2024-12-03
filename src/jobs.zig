const std = @import("std");

const eql = std.mem.eql;
const testing = std.testing;
const outw = std.io.getStdOut().writer();
const stdin = std.io.getStdIn().reader();

const ArrayList = std.ArrayList;
const allocator = std.testing.allocator;

const job = struct {
    title: []u8,
    company: []u8,
    salary: ?i32,
    description: []u8,
    responsibilities: []u8,
    requirements: []u8,
    hiring_process: []u8,
    company_description: []u8,
};

// test "arrayList" {
//     // Initialisation of the job list
//     var list = ArrayList(u8).init(allocator);
//     defer list.deinit();

//     try list.append('A');
//     try list.append('B');

//     for (list.items, 0..) |item, i| {
//         try outw.print("{}: {}\n", .{ i, item });
//     }

//     list.items[0] = 'C';
//     for (list.items, 0..) |item, i| {
//         try outw.print("{}: {}\n", .{ i, item });
//     }

//     try testing.expect(list.items[0] == 'C');
//     try testing.expect(list.items[1] == 'B');

//     try outw.print("{c}\n", .{list.items[0]});
// }

// test "test sdtin" {
//     const input = try stdin.readUntilDelimiterAlloc(std.heap.page_allocator, '\n', 8192);
//     defer std.heap.page_allocator.free(input);
//     try outw.print("Your input was: {s}\n", .{input});
// }

// test "test sdtin" {
//     var input: [10]u8 = undefined;
//     _ = try stdin.readUntilDelimiter(&input, '\n');
//     try outw.print("Your input was: {s}\n", .{input});
// }
