const std = @import("std");

pub fn main() !void {
    var stdout_buffer: [2048]u8 = undefined;
    const stdout = std.fs.File.stdout().writer(&stdout_buffer);
    const w = stdout.interface;
    try w.print("Hello world", .{});
    try w.flush();
}
