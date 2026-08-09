import json, statistics as st, math, random
BARS=json.load(open('bars.json'))
SER={c:[[x[0]]+[float(v) for v in x[1:6]] for x in b] for c,b in BARS.items()}
START,END='2025-06-24','2026-07-31'
def cap(code): return 0.20 if code[0]=='3' or code[:3]=='688' else 0.10
def is_lu(code,b,i):
    if i==0: return False
    r=b[i][2]/b[i-1][2]-1
    return r>=cap(code)-0.005 and abs(b[i][2]-b[i][3])<1e-6   # 收盘=最高
# 连板计数
def streak(code,b,i):
    k=0
    while i-k>=1 and is_lu(code,b,i-k): k+=1
    return k
print("=== 问题三：38 只科技股里『连续涨停』的样本有多少 ===")
rows=[]
for c,b in SER.items():
    for i in range(61,len(b)-20):
        if not (START<=b[i][0]<=END): continue
        s=streak(c,b,i)
        if s>=1: rows.append((c,b[i][0],s,i))
from collections import Counter
cnt=Counter(r[2] for r in rows)
print(" 连板数:", dict(sorted(cnt.items())))
for s in sorted(cnt):
    days=len(set(r[1] for r in rows if r[2]==s))
    print(f"  {s} 连板: 股票-日 {cnt[s]:4d}  独立交易日 {days:3d}")
print("\n=== 连板后的表现（次日 / 次周=5日 / 20日），按连板数分 ===")
print(" 连板  n   独立日  次日均值  次日中位 次日涨概率  5日均值 5日中位  20日均值 20日中位")
def fw(c,i,h):
    b=SER[c]; return b[i+h][2]/b[i][2]-1
for s in sorted(cnt):
    g=[r for r in rows if r[2]==s]
    if len(g)<5: continue
    d1=[fw(r[0],r[3],1) for r in g]; d5=[fw(r[0],r[3],5) for r in g]; d20=[fw(r[0],r[3],20) for r in g]
    print(f"  {s}  {len(g):4d}  {len(set(r[1] for r in g)):4d}  {st.mean(d1)*100:+7.2f}% {st.median(d1)*100:+7.2f}% {sum(1 for x in d1 if x>0)/len(d1)*100:6.1f}%  {st.mean(d5)*100:+6.2f}% {st.median(d5)*100:+6.2f}%  {st.mean(d20)*100:+6.2f}% {st.median(d20)*100:+6.2f}%")
print("\n 全样本基准（同期所有股票-日）:")
allr=[(c,i) for c,b in SER.items() for i in range(61,len(b)-20) if START<=b[i][0]<=END]
for h in (1,5,20):
    v=[fw(c,i,h) for c,i in allr]
    print(f"   {h:>2}日: 均值{st.mean(v)*100:+6.2f}% 中位{st.median(v)*100:+6.2f}% 上涨概率{sum(1 for x in v if x>0)/len(v)*100:.1f}%")

print("\n=== 连板≥2 的次日：按交易日聚类检验 ===")
g=[r for r in rows if r[2]>=2]
byd={}
for r in g: byd.setdefault(r[1],[]).append(fw(r[0],r[3],1))
# 与同日全样本均值比（剔除行情漂移）
mkt={}
for c,i in allr: mkt.setdefault(SER[c][i][0],[]).append(fw(c,i,1))
mkt={d:st.mean(v) for d,v in mkt.items()}
xs=[st.mean(v)-mkt[d] for d,v in byd.items()]
mu=st.mean(xs); sd=st.stdev(xs); t=mu/(sd/math.sqrt(len(xs)))
print(f"  股票-日 n={len(g)}  独立交易日 n={len(xs)}")
print(f"  次日相对同期全样本: 均值 {mu*100:+.2f}pp  sd {sd*100:.2f}  t={t:+.2f}  p={math.erfc(abs(t)/math.sqrt(2)):.4f}")
