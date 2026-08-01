import core, statistics as st, math
r=core.build()
def gapb(g):
    if g>=0.05: return '高开>=5%'
    if g>=0.03: return '高开3~5%'
    if g>0: return '高开0~3%'
    if g>-0.03: return '低开0~3%'
    return '低开>=3%'
cells={}
for x in r: cells.setdefault((x['trend'],gapb(x['gap'])),[]).append(x)
def daytest(v):
    byd={}
    for y in v: byd.setdefault(y['date'],[]).append(y)
    xs=[sum(1 for y in g if y['oc']>0)/len(g) for g in byd.values()]
    if len(xs)<3: return None
    mu=st.mean(xs); sd=st.stdev(xs); t=(mu-0.5)/(sd/math.sqrt(len(xs)))
    p=math.erfc(abs(t)/math.sqrt(2))  # 正态近似，n>=25 够用
    return len(xs),mu,t,p
print("=== 以『交易日』为观察单位（每日先聚合成一个收高率），检验是否偏离 50% ===")
print(" 格子                  股票日n  独立日  按天收高率  t      p(近似)")
out=[]
for k,v in sorted(cells.items()):
    d=daytest(v)
    if not d: continue
    nd,mu,t,p=d
    out.append((p,k,len(v),nd,mu,t))
for p,k,n,nd,mu,t in sorted(out):
    print(f" {k[0]}{k[1]:<12} {n:5d}   {nd:4d}    {mu*100:5.1f}%   {t:+5.2f}  {p:8.4f}")
print("\n BH 校正(q=0.05, m=15):")
for i,(p,k,n,nd,mu,t) in enumerate(sorted(out),1):
    print(f"  {i:>2} {k[0]}{k[1]:<12} p={p:.4f} 阈值{0.05*i/15:.4f} {'✓' if p<=0.05*i/15 else '✗'}")

print("\n=== 三个候选逐条细看 ===")
for key in [('下跌','高开>=5%'),('下跌','低开>=3%'),('震荡','低开>=3%')]:
    v=cells[key]; byd={}
    for y in v: byd.setdefault(y['date'],[]).append(y)
    ds=sorted(byd)
    half=len(ds)//2
    a=[y for d in ds[:half] for y in byd[d]]; b=[y for d in ds[half:] for y in byd[d]]
    ka=sum(1 for y in a if y['oc']>0); kb=sum(1 for y in b if y['oc']>0)
    z,p=core.z2(ka,len(a),kb,len(b))
    # 赛道
    sect={}
    for y in v: sect.setdefault(y['sect'],[]).append(y)
    ok=[(s,len(g),core.hi(g)) for s,g in sect.items() if len(g)>=8]
    sign=1 if core.hi(v)>0.5 else -1
    rev=[s for s,n2,h in ok if (h>0.5)!=(core.hi(v)>0.5)]
    print(f"\n {key}: n={len(v)} 独立日{len(ds)} 收高率{core.hi(v)*100:.1f}% 加权分{core.wscore(v):+.2f}")
    print(f"   时间对半(按独立日切): 前{ka}/{len(a)}={ka/len(a)*100:.0f}% 后{kb}/{len(b)}={kb/len(b)*100:.0f}% p={p:.4f}")
    print(f"   赛道 n>=8 的有{len(ok)}个，反例{len(rev)}个: {rev}")
    # 留一日
    worst=max(byd,key=lambda d:len(byd[d]))
    rest=[y for y in v if y['date']!=worst]
    print(f"   剔最集中日{worst}({len(byd[worst])}条): 加权分{core.wscore(rest):+.2f} (变动{core.wscore(rest)-core.wscore(v):+.2f})")
