import core, statistics as st, random
r=core.build(); n=len(r)
def sc(x): return core.score(x)
print("=== 用文档自己的指标（加权分/收高率）比较 限价 vs 市价，未成交记 0 分 ===")
print(" 策略        平均分   收高(赚钱)率   中位收益")
mkt=[x['oc'] for x in r]
print(f" 市价买入   {st.mean(sc(v) for v in mkt):+.3f}   {sum(1 for v in mkt if v>0)/n*100:5.1f}%    {st.median(mkt)*100:+.2f}%")
for d in [0.005,0.01,0.02]:
    vals=[]
    for x in r:
        if x['lowpct']<=-d: vals.append((x['c']-x['o']*(1-d))/(x['o']*(1-d)))
        else: vals.append(None)
    ss=[sc(v) if v is not None else 0.0 for v in vals]
    got=[v for v in vals if v is not None]
    print(f" 限价−{d*100:.1f}%  {st.mean(ss):+.3f}   {sum(1 for v in got if v>0)/n*100:5.1f}%    {st.median([v if v is not None else 0 for v in vals])*100:+.2f}%")

print("\n=== 按交易日整块 bootstrap（保留同日相关性），限价−1% 减 市价 的平均收益差 ===")
bydate={}
for x in r: bydate.setdefault(x['date'],[]).append(x)
dates=list(bydate)
def diff(sample_dates):
    tot=0;cnt=0
    for d in sample_dates:
        for x in bydate[d]:
            m=x['oc']
            l=((x['c']-x['o']*0.99)/(x['o']*0.99)) if x['lowpct']<=-0.01 else 0.0
            tot+= l-m; cnt+=1
    return tot/cnt
random.seed(7)
b=[diff([random.choice(dates) for _ in dates]) for _ in range(1000)]
b.sort()
print("  点估计 %+.3f%%   95%%CI [%+.3f%%, %+.3f%%]"%(diff(dates)*100,b[25]*100,b[975]*100))
