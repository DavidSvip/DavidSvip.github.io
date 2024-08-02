import math
import random as rd
times=1000000


goodwins=0
badwins=0
for j in range(times):
    hunter=5
    werewolf=3
    blackwolf=0
    games=werewolf+blackwolf
    for i in range(games):
        # print('night of',i+1) # 第i+1天夜晚
        hunter-=1 # 狼人刀人
        # print('hunter=',hunter)
        if hunter==0:
            # print('狼人胜利')
            badwins+=1
            break
        while True: # 猎人随机带人
            kill=rd.randint(1,hunter+werewolf+blackwolf)
            if kill<=hunter:
                hunter-=1 # 猎人被带，新猎人再次随机带人
                # print('hunter=',hunter)
                if hunter==0:
                    break
            elif kill>hunter and kill<=hunter+blackwolf:
                blackwolf-=1
                if werewolf==0 and blackwolf==0:
                    break
                hunter-=1 # 黑狼有视角，技能必带猎人
                # print('hunter=',hunter)
                if hunter==0:
                    break
            else:
                werewolf-=1 # 狼人被带
                # print('werewolf=',werewolf)                
                break
        if werewolf==0 and blackwolf==0:
            # print('好人胜利')
            goodwins+=1
            break
        if hunter==0:
            # print('狼人胜利')
            badwins+=1
            break
        # print('day of',i+1) # 第i+1天白天
        if hunter<=werewolf+blackwolf: # 绑票机制
            badwins+=1
            break
        kill=rd.randint(1,hunter+werewolf+blackwolf) # 随机投票流放
        if kill<=hunter:
            hunter-=1
            # print('hunter=',hunter)
            if hunter==0:
                # print('狼人胜利')
                badwins+=1
                break
        elif kill>hunter and kill<=hunter+blackwolf:
            blackwolf-=1
            if werewolf==0 and blackwolf==0:
                # print('好人胜利')
                goodwins+=1
                break
        else:
            werewolf-=1
            # print('werewolf=',werewolf)
            if werewolf==0 and blackwolf==0:
                # print('好人胜利')
                goodwins+=1
                break
print(goodwins/times)
print(badwins/times)
    
    
        
