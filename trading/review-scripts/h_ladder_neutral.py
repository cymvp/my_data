import json, statistics as st, random
BARS=json.load(open('bars.json'))
SER={c:[[x[0]]+[float(v) for v in x[1:6]] for x in b] for c,b in BARS.items()}
START,END='2025-06-24','2026-07-31'
# 先算每只票每天的 20/10/5 日前瞻收益，再按日期做横截面去均值 = 剔除行情漂移
def build(H):
    idx={}
    for c,b in SER.items():
        for i in range(61,len(b)-H):
            if START<=b[i][0]<=END:
                idx.setdefault(b[i][0],[]).append((c,i,b[i+H][2]/b[i][2]-1))
    mkt={d:st.mean(x[2] for x in v) for d,v in idx.items()}
    return idx,mkt
print("剔除行情漂移后：同一天所有 38 只票的 H 日收益取横截面均值当作『大盘』，只看相对表现\n")
for H in [10,20]:
    idx,mkt=build(H)
    print(f"=== H={H} 天（该期横截面平均 {st.mean(mkt.values())*100:+.2f}%）===")
    print("  深度   成交率   [相对大盘] 立即买  阶梯    差额     其中: 成交日相对  未成交日相对")
    for depth in [0.05,0.075,0.10]:
        imm=[];lad=[];hits=[];hi_r=[];mi_r=[]
        for d,v in idx.items():
            m=mkt[d]
            for c,i,r in v:
                b=SER[c]; p0=b[i][2]; lvl=p0*(1-depth)
                hit=any(b[j][4]<=lvl for j in range(i+1,i+1+H))
                rl=(b[i+H][2]/lvl-1) if hit else 0.0
                imm.append(r-m); lad.append(rl-m); hits.append(hit)
                (hi_r if hit else mi_r).append(r-m)
        fr=sum(hits)/len(hits)
        print(f"  -{depth*100:4.1f}%  {fr*100:5.1f}%   {st.mean(imm)*100:+7.2f}%  {st.mean(lad)*100:+7.2f}%  {(st.mean(lad)-st.mean(imm))*100:+6.2f}pp   {st.mean(hi_r)*100:+7.2f}%     {st.mean(mi_r)*100:+7.2f}%")
    print()
print("『成交日相对』= 触发了限价的那些起点，若当初立即买、相对大盘的表现")
print("『未成交日相对』= 没触发的那些起点，若当初立即买、相对大盘的表现")
print("两者之差就是纯选择效应：跌下来的票是不是本来就更弱。\n")
# 纯选择效应的显著性：按日期整块 bootstrap
H=20; depth=0.075
idx,mkt=build(H)
per_date={}
for d,v in idx.items():
    m=mkt[d]; a=[];b_=[]
    for c,i,r in v:
        bb=SER[c]; lvl=bb[i][2]*(1-depth)
        (a if any(bb[j][4]<=lvl for j in range(i+1,i+1+H)) else b_).append(r-m)
    per_date[d]=(a,b_)
def stat(ds):
    A=[x for d in ds for x in per_date[d][0]]; B=[x for d in ds for x in per_date[d][1]]
    return (st.mean(A)-st.mean(B)) if A and B else None
dates=list(per_date); random.seed(11)
pt=stat(dates)
bs=sorted(x for x in (stat([random.choice(dates) for _ in dates]) for _ in range(600)) if x is not None)
print(f"纯选择效应（-7.5%/20天）：成交组 减 未成交组 的相对收益 = {pt*100:+.2f}pp")
print(f"  按交易日整块 bootstrap 600 次，95%% 区间 [{bs[15]*100:+.2f}, {bs[-15]*100:+.2f}] pp")
