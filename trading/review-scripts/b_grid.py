import core, statistics as st, math
from collections import Counter
r=core.build()
def gapb(g):
    if g>=0.05: return '5_高开>=5%'
    if g>=0.03: return '4_高开3~5%'
    if g>0: return '3_高开0~3%'
    if g>-0.03: return '2_低开0~3%'
    return '1_低开>=3%'
cells={}
for x in r: cells.setdefault((x['trend'],gapb(x['gap'])),[]).append(x)
print("=== 15 格主表（含 p 值、同日聚集度、独立交易日数）===")
print(" 趋势 跳空档          n   收高率  加权分     p(二项)  最大单日占比  独立日数")
res=[]
for k in sorted(cells,key=lambda k:(k[0],k[1])):
    v=cells[k]; nn=len(v); kk=sum(1 for y in v if y['oc']>0)
    z,p=core.ztest(kk,nn)
    dc=Counter(y['date'] for y in v); top=dc.most_common(1)[0]
    res.append((k,nn,kk/nn,core.wscore(v),p,top,len(dc)))
    print(f" {k[0]} {k[1]:<14} {nn:5d}  {kk/nn*100:5.1f}%  {core.wscore(v):+6.2f}  {p:9.2e}   {top[1]}/{nn}={top[1]/nn*100:.0f}% ({top[0]})  {len(dc)}")
print("\n=== Benjamini-Hochberg FDR 校正（15 个检验）===")
ps=sorted([(x[4],x[0]) for x in res])
m=len(ps)
print(" 排名  p        BH阈值(q=0.05)  格子                 通过")
for i,(p,k) in enumerate(ps,1):
    th=0.05*i/m
    print(f" {i:>3}  {p:9.2e}  {th:.5f}       {k[0]}{k[1]:<14} {'✓' if p<=th else '✗'}")
# Bonferroni
print("\n Bonferroni 阈值 = %.5f"%(0.05/15))
print("\n=== 规则2『下跌×高开≥5%』做同日聚类的稳健检验 ===")
v=cells[('下跌','5_高开>=5%')]
byd={}
for y in v: byd.setdefault(y['date'],[]).append(y)
print("  n=%d 覆盖 %d 个交易日；每日收高率的『按天平均』= %.1f%%"%(len(v),len(byd),
      st.mean(sum(1 for y in g if y['oc']>0)/len(g) for g in byd.values())*100))
zz,pp=core.ztest(sum(1 for y in v if y['oc']>0),len(v)); print("  朴素二项 p=%.2e (z=%.2f)"%(pp,zz))
# 有效样本量 = 独立日数; 用每日均值做单样本 t 检验 对 0.5
xs=[sum(1 for y in g if y['oc']>0)/len(g) for g in byd.values()]
mu=st.mean(xs); sd=st.stdev(xs); t=(mu-0.5)/(sd/math.sqrt(len(xs)))
print("  按天为单位 t 检验：均值%.3f sd%.3f n=%d  t=%.2f"%(mu,sd,len(xs),t))
print("  剔除 2026-07-31 后：n=%d 收高率%.1f%% 加权分%+.2f"%(
  len([y for y in v if y['date']!='2026-07-31']),
  core.hi([y for y in v if y['date']!='2026-07-31'])*100, core.wscore([y for y in v if y['date']!='2026-07-31'])))
d2=sorted(byd.items(), key=lambda kv:-len(kv[1]))[:6]
print("  最集中的日子：", [(k,len(g)) for k,g in d2])
rest=[y for y in v if y['date'] not in ('2026-07-31',d2[1][0])]
print("  再剔除第二集中日 %s 后：n=%d 收高率%.1f%% 加权分%+.2f"%(d2[1][0],len(rest),core.hi(rest)*100,core.wscore(rest)))
