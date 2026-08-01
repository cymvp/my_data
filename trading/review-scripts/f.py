import core, statistics as st, math
r=core.build()
v=[x for x in r if x['trend']=='上涨' and x['gap']<=-0.03 and x['nd_chg'] is not None]
byd={}
for y in v: byd.setdefault(y['date'],[]).append(y)
xs=[sum(1 for y in g if y['nd_chg']>0)/len(g) for g in byd.values()]
mu=st.mean(xs); sd=st.stdev(xs); t=(mu-0.5)/(sd/math.sqrt(len(xs)))
print("上涨x低开>=3% 次日上涨率 按天 {:.1f}% n_day={} t={:.2f} p={:.4f}".format(mu*100,len(xs),t,math.erfc(abs(t)/math.sqrt(2))))
ds=sorted(set(x['date'] for x in r)); mid=ds[len(ds)//2]
a=[x for x in r if x['date']<mid]; b=[x for x in r if x['date']>=mid]
print("跌破开盘率 前半 {:.1f}% 后半 {:.1f}%".format(sum(y['brk'] for y in a)/len(a)*100, sum(y['brk'] for y in b)/len(b)*100))
byd2={}
for y in r: byd2.setdefault(y['date'],[]).append(y)
print("每日跌破率最低5天:", sorted((round(sum(z['brk'] for z in g)/len(g),2),d) for d,g in byd2.items())[:5])
