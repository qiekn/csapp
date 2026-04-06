import gdb

# print truth table
class Ptt(gdb.Command):
    def __init__(self):
        super(Ptt, self).__init__("ptt", gdb.COMMAND_USER)

    def invoke(self, arg, from_tty):
        expr = arg.strip()
        if not expr:
            print("usage: ptt <expr>")
            print("example: ptt ~(~x & ~y)")
            return

        print("x y | expr")
        print("----+-----")

        for xv in (0, 1):
            for yv in (0, 1):
                e = expr.replace("x", str(xv)).replace("y", str(yv))
                try:
                    val = int(gdb.parse_and_eval(e))
                    print(f"{xv} {yv} | {1 if val != 0 else 0}")
                except gdb.error as ex:
                    print(f"{xv} {yv} | error: {ex}")

Ptt()
