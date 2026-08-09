import json, statistics as st, math, random
BARS=json.load(open('bars.json'))
SER={c:[[x[0]]+[float(v) for v in x[1:6]] for x in b] for c,b in BARS.items()}
START,END='2025-06-24','2026-07-31'
print("干净版：从『成交那一天』往后算 20 日收益，不跟固定终点比。")
print("对照 = 同一天全池所有票的 20 日平均（剔除行情漂移）。\n")
F=20
mkt={}
for c,b in SER.items():
    for i in range(61,len(b)-F):
        if START<=b[i][0]<=END: mkt.setdefault(b[i][0],[]).append(b[i+F][2]/b[i][2]-1)
mkt={d:st.mean(v) for d,v in mkt.items()}
print(" 触发条件（从某天收盘起 20 日内首次触及）      成交事件 独立日  成交后20日相对大盘  bootstrap 95%区间")
for depth in [0.05,0.075,0.10]:
    ev={}
    for c,b in SER.items():
        for i in range(61,len(b)-F):
            if not (START<=b[i][0]<=END): continue
            lvl=b[i][2]*(1-depth)
            for j in range(i+1,min(i+1+20,len(b)-F)):
                if b[j][4]<=lvl:
                    if b[j][0] in mkt: ev.setdefault(b[j][0],[]).append(b[j+F][2]/lvl-1-mkt[b[j][0]])
                    break
    dates=list(ev); n=sum(len(v) for v in ev.values())
    pt=st.mean(x for v in ev.values() for x in v)
    random.seed(3)
    bs=sorted(st.mean(x for d in s for x in ev[d]) for s in ([random.choice(dates) for _ in dates] for _ in range(500)))
    print(f"  跌到起点下方 {depth*100:4.1f}% 就买                 {n:6d}  {len(dates):4d}     {pt*100:+7.2f}pp        [{bs[12]*100:+.2f}, {bs[-12]*100:+.2f}]")
print("\n注：成交事件会重复计入同一天（不同起点触发同一个价位），独立日才是有效观察数。")
print("\n=== 对照：无条件买入（任意一天收盘）后 20 日相对大盘 = 0.00pp（定义如此）===")
