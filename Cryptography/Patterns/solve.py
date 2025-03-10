s1 = "{FsTwizCphdVhjha"
s2 = "3yo30vi_y0xq7rsd_kigdemwh0rqjbogqucvwqd_ilqalbjabbwg"
s3 = "}g1te_x5j8u5bon4"


def get_pattern(n, context):
    # if len(context) > 100: return
    if n in context: return

    context.append(n)
    if n % 2 == 0:
        get_pattern(n // 2, context)
    else:
        get_pattern(3*n + 1, context)

def get_chars(st, pat):
    s = ''
    for i in pat:
        if i > len(st): return ''
        s += st[i-1]
    return s


pat = []
get_pattern(12, pat)
print(pat)

for i in range(1, len(s1)):
    pat = []
    get_pattern(i, pat)
    print(i, len(pat), get_chars(s1, pat))

print("========================================")

for i in range(1, len(s2)):
    pat = []
    get_pattern(i, pat)
    print(i, len(pat), get_chars(s2, pat))

print("========================================")

for i in range(1, len(s3)):
    pat = []
    get_pattern(i, pat)
    print(i, len(pat), get_chars(s3, pat))
