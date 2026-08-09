import json, statistics as st
BARS=json.load(open('bars.json'))
SER={c:[[x[0]]+[float(v) for v in x[1:6]] for x in b] for c,b in BARS.items()}
START,END='2025-06-24','2026-07-31'
def run(depth,H):
    rows=[]
    for code,b in SER.items():
        for i in range(61,len(b)-H):
            if not (START<=b[i][0]<=END): continue
            p0=b[i][2]; lvl=p0*(1-depth); pend=b[i+H][2]
            peak=max(x[2] for x in b[i+1-60:i+1]); tr=(b[i][2]-peak)/peak
            t='下跌' if tr<=-0.15 else ('震荡' if tr<=-0.05 else '上涨')
            hit=any(b[j][4]<=lvl for j in range(i+1,i+1+H))
            rows.append((pend/p0-1, (pend/lvl-1) if hit else 0.0, hit, t))
    return rows
print("『跌 x% 才买』阶梯限价 vs 立即买入 —— 同一笔钱，H 个交易日后一起结账")
print("（挂不到就一直空仓、收益记 0；样本=38 只票每个交易日各起一次，2025-06-24~2026-07-31）\n")
print(" 挂单深度 等待H  成交率   立即买均值  阶梯均值   差额     立即买中位  阶梯中位")
cache={}
for depth in [0.02,0.05,0.075,0.10]:
    for H in [5,10,20]:
        r=run(depth,H); cache[(depth,H)]=r
        imm=[x[0] for x in r]; lad=[x[1] for x in r]; fr=sum(x[2] for x in r)/len(r)
        print(f"  -{depth*100:4.1f}%  {H:>3}天  {fr*100:5.1f}%   {st.mean(imm)*100:+7.2f}%  {st.mean(lad)*100:+7.2f}%  {(st.mean(lad)-st.mean(imm))*100:+6.2f}pp  {st.median(imm)*100:+7.2f}%  {st.median(lad)*100:+7.2f}%")
print("\n=== -7.5% / 20 天 按趋势拆 ===")
r=cache[(0.075,20)]
print(" 趋势     n    成交率  立即买均值  阶梯均值   差额")
for t in ['下跌','震荡','上涨']:
    g=[x for x in r if x[3]==t]
    print(f" {t} {len(g):6d}  {sum(x[2] for x in g)/len(g)*100:5.1f}%  {st.mean(x[0] for x in g)*100:+7.2f}%  {st.mean(x[1] for x in g)*100:+7.2f}%  {(st.mean(x[1] for x in g)-st.mean(x[0] for x in g))*100:+6.2f}pp")
print("\n=== 拆开看选择效应（H=20）===")
for depth in [0.05,0.075,0.10]:
    r=cache[(depth,20)]
    hit=[x for x in r if x[2]]; miss=[x for x in r if not x[2]]
    print(f" -{depth*100:.1f}%:")
    print(f"   成交了 n={len(hit)}  成交价买入到期收益 均值{st.mean(x[1] for x in hit)*100:+.2f}% 中位{st.median(x[1] for x in hit)*100:+.2f}% 为正{sum(1 for x in hit if x[1]>0)/len(hit)*100:.0f}%")
    print(f"                 同一批日子若立即买   均值{st.mean(x[0] for x in hit)*100:+.2f}% 中位{st.median(x[0] for x in hit)*100:+.2f}%")
    print(f"   没成交 n={len(miss)}  若立即买 均值{st.mean(x[0] for x in miss)*100:+.2f}% 中位{st.median(x[0] for x in miss)*100:+.2f}%  <- 踏空掉的是这部分")
