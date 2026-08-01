import core, statistics as st
r=core.build(); n=len(r)
print("=== 规则1 拆解：跌破开盘的『幅度』 ===")
for th in [0.0,0.001,0.002,0.005,0.01,0.015,0.02,0.03,0.05]:
    k=sum(1 for x in r if x['lowpct']<=-th)
    print(f"  最低价 ≤ 开盘价 −{th*100:.1f}%  的比例: {k/n*100:5.1f}%")
print("  最低相对开盘 中位数 %.2f%%  25分位 %.2f%%"%(st.median(x['lowpct'] for x in r)*100, sorted(x['lowpct'] for x in r)[n//4]*100))
print("  开盘价恰为当日最低的比例: %.2f%%"%(sum(1 for x in r if x['l']>=x['o'])/n*100))

print("\n=== 限价 vs 市价：同一笔资金，未成交=不持仓（当日 0 收益）===")
print(" 挂单折扣  成交率   成交日开→收中位  策略期望(计未成交为0)  市价基准")
mkt=st.mean(x['oc'] for x in r)
for d in [0.005,0.01,0.02,0.03]:
    fill=[x for x in r if x['lowpct']<=-d]
    # 成交价 = 开盘*(1-d), 收盘卖出
    rets=[(x['c']-x['o']*(1-d))/(x['o']*(1-d)) for x in fill]
    exp=sum(rets)/n
    print(f"  −{d*100:>4.1f}%   {len(fill)/n*100:5.1f}%   {st.median(x['oc'] for x in fill)*100:+6.2f}%      {exp*100:+7.3f}%           {mkt*100:+.3f}%")
print("\n=== 按趋势拆：限价 −1% 策略 vs 市价 ===")
for t in ['下跌','震荡','上涨']:
    s=[x for x in r if x['trend']==t]
    fill=[x for x in s if x['lowpct']<=-0.01]
    rets=[(x['c']-x['o']*0.99)/(x['o']*0.99) for x in fill]
    print(f"  {t}: 成交率{len(fill)/len(s)*100:5.1f}%  限价期望{sum(rets)/len(s)*100:+.3f}%  市价{st.mean(x['oc'] for x in s)*100:+.3f}%")
print("\n=== 15格 跌破开盘率 最低值核对 ===")
def gapb(g):
    if g>=0.05: return '高开≥5%'
    if g>=0.03: return '高开3~5%'
    if g>0: return '高开0~3%'
    if g>-0.03: return '低开0~3%'
    return '低开≥3%'
cells={}
for x in r: cells.setdefault((x['trend'],gapb(x['gap'])),[]).append(x)
lo=sorted(((sum(y['brk'] for y in v)/len(v),k,len(v)) for k,v in cells.items()))
for p,k,c in lo[:5]: print(f"  {k} n={c} 跌破率{p*100:.1f}%")
