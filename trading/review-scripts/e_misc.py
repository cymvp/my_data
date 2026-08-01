import core, statistics as st
r=core.build()
def gapb(g):
    return '高开>=5%' if g>=0.05 else ('高开3~5%' if g>=0.03 else ('高开0~3%' if g>0 else ('低开0~3%' if g>-0.03 else '低开>=3%')))
cells={}
for x in r:
    if x['nd_chg'] is not None: cells.setdefault((x['trend'],gapb(x['gap'])),[]).append(x)
print("=== 次日：核对『42%~54%』 ===")
ups=[]; meds=[]
for k,v in sorted(cells.items()):
    u=sum(1 for y in v if y['nd_chg']>0)/len(v); m=st.median(y['nd_chg'] for y in v)
    ups.append(u); meds.append(m)
    print(f" {k[0]}{k[1]:<10} n={len(v):5d} 次日上涨率{u*100:5.1f}% 次日涨跌中位{m*100:+.2f}%")
print(" 区间: 上涨率 %.0f%%~%.0f%%  中位 %+.2f%%~%+.2f%%"%(min(ups)*100,max(ups)*100,min(meds)*100,max(meds)*100))
print(" 次日盘中跌破次日开盘率 %.1f%%"%(sum(1 for x in r if x['nd_brk'])/sum(1 for x in r if x['nd_brk'] is not None)*100))

print("\n=== 量能核对 ===")
for lo,hi_,nm in [(None,0.85,'缩量<0.85'),(1.6,None,'巨量>=1.6')]:
    v=[x for x in r if x['volx'] and (hi_ is None or x['volx']<hi_) and (lo is None or x['volx']>=lo)]
    print(f" {nm}: n={len(v)} 收高率{core.hi(v)*100:.0f}% 加权分{core.wscore(v):+.2f}")
print("\n=== 分批建仓（开盘跳空>=3% 建仓，扣0.10%成本，限价按当日最低判成交）===")
print(" 趋势   一次性(开盘全买)  分3批-已投入口径  分3批-计划资金口径  投入占比")
for t in ['下跌','震荡','上涨']:
    s=[x for x in r if x['trend']==t and x['gap']>=0.03]
    if not s: continue
    once=[core.score(x['oc']-0.001) for x in s]
    inv=[];plan=[];ratio=[]
    for x in s:
        legs=[]  # 1/3 开盘, 1/3 开盘-1%, 1/3 开盘-2%
        legs.append(x['oc']-0.001)
        for d in (0.01,0.02):
            if x['lowpct']<=-d: legs.append((x['c']-x['o']*(1-d))/(x['o']*(1-d))-0.001)
        filled=len(legs)
        inv.append(core.score(sum(legs)/filled)); ratio.append(filled/3)
        plan.append(core.score(sum(legs)/3))   # 未投出的部分收益 0
    print(f" {t}  n={len(s):4d}  {st.mean(once):+.2f}          {st.mean(inv):+.2f}            {st.mean(plan):+.2f}          {st.mean(ratio)*100:.0f}%")
