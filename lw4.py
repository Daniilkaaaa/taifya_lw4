import csv
import sys

def a(b, c, d):
    e = set()
    f = c.readlines()

    g = f[0].strip().split(';')
    h = f[1].strip().split(';')

    for i in range(1, len(g)):
        j = {
            "k": h[i],
            "l": g[i],
            "m": []
        }
        b.append(j)

    for k in f[2:]:
        l = k.strip().split(';')
        m = l[0]

        if m != "Оµ":
            e.add(m)

        for n in range(1, len(l)):
            o = {
                "p": m,
                "q": l[n].split(',') if l[n] else []
            }
            b[n - 1]["m"].append(o)

    d = list(e)

    return b, d

def b(c, d):
    e = set()
    for f in c:
        for g in f['m']:
            e.add(g['p'])

    e = sorted(e)

    with open(d, mode='w', newline='', encoding='utf-8') as h:
        i = csv.writer(h, delimiter=';')

        j = ['']
        for k in c:
            j.append(k['l'])
        i.writerow(j)

        l = [''] + [m['k'] for m in c]
        i.writerow(l)

        for n in e:
            o = [n]

            for p in c:
                q = []
                for r in p['m']:
                    if r['p'] == n:
                        q.append(r['q'])

                if not q:
                    o.append('')
                else:
                    s = ','.join(q)
                    o.append(s)

            i.writerow(o)

def c(d, e, f=None):
    if f is None:
        f = set()

    g = set()
    for h in d:
        if h not in f:
            f.add(h)
            for i in e[h]['m']:
                if i['p'] == "ε":
                    g.update(i['q'])

    if not g:
        return f
    else:
        return c(g, e, f)

def d(e, f):
    g = []
    h = {}
    i = {}
    j = []

    f = [k for k in f if k != "ε"]
    for l in e:
        i[l] = frozenset(c({l}, e))

    m = [list(e.keys())[0]]
    n = frozenset(m)
    h[n] = "S0"
    j.append(m)
    o = 0

    while j:
        p = j.pop(0)
        q = frozenset(p)
        r = {
            "k": h[q],
            "l": "",
            "m": []
        }

        s = frozenset().union(*(i[t] for t in p))

        for t in s:
            if e[t]['l'] == "F":
                r['l'] = "F"

            for u in f:
                for v in e[t]['m']:
                    if v['p'] == u:
                        if v['q']:
                            w = list(v['q'])
                            x = next(
                                (y for y in r['m'] if y['p'] == u), None
                            )

                            if x:
                                x['q'].extend(
                                    z for z in w if z not in x['q']
                                )
                            else:
                                r['m'].append({
                                    'p': u,
                                    'q': w
                                })

        for y in r['m']:
            z = frozenset(y['q'])

            if z:
                if z not in h.keys():
                    o += 1
                    h[z] = f"S{o}"
                    j.append(y['q'])
                y['q'] = h[z]

        g.append(r)
    return g

def main():
    if len(sys.argv) != 3:
        print("Usage: lab3 grammar.txt output.csv")
        sys.exit(1)

    n = sys.argv[1]
    o = sys.argv[2]

    p = []
    q = []

    with open(n, 'r', encoding='utf-8') as r:
        p, q = a(p, r, q)

    s = {}

    for t in p:
        s[t["k"]] = {
            "l": t["l"],
            "m": t["m"]
        }

    u = d(s, q)

    b(u, o)

if __name__ == "__main__":
    main()