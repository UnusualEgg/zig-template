import subprocess
import sys,os

proc = subprocess.run(["zig", "build", "--color", "off"], stderr=subprocess.PIPE, text=True)
stderr = str(proc.stderr)
find_str = "suggested value: "
find_str_index = stderr.find(find_str)
fingerprint = stderr[find_str_index+len(find_str):stderr.find("\n")]

with open("build.zig.zon","r") as f:
    build_zig_zon = f.read()

#remove the last line and add fingerprint, then read the last line
lines=build_zig_zon.splitlines()
out="\n".join(lines[:-1])
out+=f"\n    .fingerprint = {fingerprint},\n}}\n"

with open("build.zig.zon","w") as f:
    f.write(out)

