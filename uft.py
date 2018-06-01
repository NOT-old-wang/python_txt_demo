# encoding=utf-8
'''
正常结果一般在2以上, 乱码非常接近1, 可以认为1.2以下就一定是乱码了.
也可转成概率公式.
设为1时概率为0.9, 2时概率为0.1,可得下面的公式
P=11+exp(4.395∗x−6.594)

式中:
x--为字符串长度与分词数组长度的比值
P--为概率.

这个方法引入了结巴分词模块
需要提前安装

pip3 install jieba
'''
import jieba

def new_len(iterable):
    try:
      return iterable.__len__()
    except AttributeError:
      return sum(1 for _ in iterable)


normal_str="我来到北京清华大学"
normal_len=len(normal_str)
seg_list = jieba.cut(normal_str)

res = "正常文本:"+str(normal_len / new_len(seg_list))

print(res)

luanma_str = "楀钩镞惰鐪熷涔狅纴鍒昏嫤阍荤爷鎶?湳锛屾墡瀹炲伐浣滐纴瑙勮寖绠＄悊銆备汉镐寲镄勭鐞嗗哜镵氢简涓?镓规妧链骞诧纴寰楀埌浜嗗叏鍏徃锻桦伐镄勪俊璧栥?锻桦伐100%鍙傚姞鍖讳缭锛?5钖嶅憳宸弬锷犲煄淇濓纴澶栨潵锻桦伐鎻愪緵椋熷锛屾椂镞跺埢鍒讳互鍏变骇鍏氩憳镄勬爣鍑呜 閲忚嚜宸憋纴鍦濂戒紒涓氱殑钖屾椂锛屼负绀句细浜嬩笟鎹愯祫锷10涓囧厓锛屾崘璧犺传锲板憳宸灞炴不鐥?涓囧厓锛屽府锷传锲板鐢?.6涓囧厓锛屾崘璧犳枃鏋椾腑瀛绅链鸿澶?涓囧厓锛屾厛锽勬崘鐚?涓囧厓銆?/p> 锻拰鍏村悓蹇楀浜嬩笟镓宪杩芥眰锛屽湪杩椤崄鍑犲勾浼佷笟鍙戝睍杩囩涓纴鍏呭垎鍙戞尌浜嗕竴涓叡浜厷锻樼殑鍏堥攱妯寖甯浣灭敤锛屽弹鍒颁简闀囨敛搴溿?甯傜骇涓荤閮桊镄勮褰帮纴绀句细钖勭晫镄勪竴镊村璇勶纴浠栧潥淇彧链変笉鏂彂灞曪"
luanma_len = len(luanma_str)
luanma = jieba.cut(luanma_str)


res = "乱码:"+str(luanma_len / new_len(luanma))
print(res)
