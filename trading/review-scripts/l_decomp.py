import core, statistics as st, random
r=core.build(); n=len(r)
d=0.01
mkt=st.mean(x['oc'] for x in r)
lim=[]
for x in r:
    lim.append(((x['c']-x['o']*(1-d))/(x['o']*(1-d))) if x['lowpct']<=-d else 0.0)
act=st.mean(lim)
print("规则 1 那 0.26pp 的差额，到底是什么造成的？（限价 -1% vs 开盘市价，当日收盘结账）\n")
print(f"  市价策略平均            {mkt*100:+.3f}%   （100% 的日子有仓位）")
print(f"  限价策略平均            {act*100:+.3f}%   （68.5% 的日子有仓位，成交价便宜 1%）")
print(f"  差额                    {(act-mkt)*100:+.3f}pp\n")
# 反事实：把成交与否在同一天内的股票间随机打散 -> 保留成交率与折价，去掉选择性
byd={}
for i,x in enumerate(r): byd.setdefault(x['date'],[]).append(i)
random.seed(5); sims=[]
for _ in range(200):
    tot=0
    for dt,idxs in byd.items():
        k=sum(1 for i in idxs if r[i]['lowpct']<=-d)
        pick=set(random.sample(idxs,k))
        for i in idxs:
            x=r[i]
            tot+= ((x['c']-x['o']*(1-d))/(x['o']*(1-d))) if i in pick else 0.0
    sims.append(tot/n)
cf=st.mean(sims)
print(f"  反事实：同一天内随机挑同样多的票『成交』（保留 68.5% 成交率和 1% 折价，抹掉选择性）")
print(f"    反事实平均            {cf*100:+.3f}%")
print(f"    → 纯仓位效应（少 31.5% 仓位）  {(cf-mkt)*100:+.3f}pp")
print(f"    → 纯选择效应（成交的正好是弱的）{(act-cf)*100:+.3f}pp")
print(f"\n  这一年开盘→收盘的平均漂移是 {mkt*100:+.3f}%/天；漂移若为 0，仓位效应会归零，只剩选择效应。")
