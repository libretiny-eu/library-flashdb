#  Copyright (c) Kuba Szczodrzyński 2023-5-9.

from os.path import realpath

Import("env")

for item in env.get("CPPDEFINES", []):
    if "FDB_USING_FAL_MODE" in str(item):
        env.Append(
            SRC_FILTER=[
                "+<port/fal/src>",
            ],
            CPPPATH=[
                realpath("port/fal/inc"),
            ],
        )
