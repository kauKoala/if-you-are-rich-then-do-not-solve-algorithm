input = __import__("sys").stdin.readline
from collections import defaultdict as dfd
dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]

# 입력값
n, m = map(int, input().split())
sx, sy = -1, -1
world_map = [[*input().strip()] for _ in range(n)]
move = [*input().strip()]

k = 0; l = 0
for i in range(n):
    for j in range(m):
        if world_map[i][j] in ['&', 'M']: k += 1
        elif world_map[i][j] == 'B': l += 1
        elif world_map[i][j] == '@': sx = i; sy = j

monster_map = [[-1] * m for _ in range(n)]
monster_info = []
chest_map = [[-1] * m for _ in range(n)]
chest_info = []

for i in range(k):
    r, c, s, w, a, h, e = input().strip().split()
    r = int(r) - 1; c = int(c) - 1; w = int(w); a = int(a); h = int(h); e = int(e)
    monster_map[r][c] = len(monster_info)
    monster_info.append([s, w, a, h, e])

for i in range(l):
    r, c, t, s = input().strip().split()
    r = int(r) - 1; c = int(c) - 1
    if t in ['W', 'A']: s = int(s)
    chest_map[r][c] = len(chest_info)
    chest_info.append([t, s])

# 플레이어 정보
x, y = sx, sy                # 시작 위치
LV = 1                       # 레벨
NOW_HP = 20                  # 체력
FULL_HP = 20                 # 최대 체력
ATT = 2                      # 기본 공격력
DEF = 2                      # 기본 방어력
NOW_EXP = 0                  # 현재 경험치
FULL_EXP = 5                 # 레벨업에 필요한 경험치
TURN = 0                     # 턴 수
WEAPON = 0                   # 무기 공격력
ARMOR = 0                    # 방어구 방어력
RING = dfd(lambda: False)    # 장신구
RING_COUNT = 0               # 장신구 개수
KILL_BOSS = 0                # 보스 킬 여부
'''
########### 게임 진행 관련 함수 ###########
'''

def movable(direction, now_x, now_y):
    nx, ny = now_x, now_y
    if direction == 'R': nx, ny = x + dx[2], y + dy[2]
    elif direction == 'L': nx, ny = x + dx[3], y + dy[3]
    elif direction == 'U': nx, ny = x + dx[1], y + dy[1]
    else: nx, ny = x + dx[0], y + dy[0]

    if 0 <= nx < n and 0 <= ny < m and world_map[nx][ny] != '#': return [nx, ny]
    return [now_x, now_y]

def trap():
    global NOW_HP, RING_COUNT, x, y
    if RING['DX']: NOW_HP -= 1
    else: NOW_HP -= 5
    if NOW_HP <= 0 and RING['RE']:  # 부활
        RING['RE'] = False
        RING_COUNT -= 1
        x, y = sx, sy
        NOW_HP = FULL_HP


def chest():
    global WEAPON, ARMOR, RING_COUNT
    chest_idx = chest_map[x][y]
    name, effect = chest_info[chest_idx]
    if name in ['W', 'A']: # 무기, 방어구 장착
        if name == 'W': WEAPON = effect
        else: ARMOR = effect
    elif name == 'O' and not RING[effect] and RING_COUNT != 4: # 장신구 장착
        RING[effect] = True
        RING_COUNT += 1

    world_map[x][y] = '.'

def monster():
    global LV, FULL_HP, NOW_HP, ATT, DEF, FULL_EXP, NOW_EXP, RING_COUNT, x, y

    monster_idx = monster_map[x][y]
    m_name, m_weapon, m_armor, m_hp, m_exp = monster_info[monster_idx]
    ATK = ATT + WEAPON
    SHIELD = DEF + ARMOR

    if RING['CO']:
        FIRST_ATK = ATK
        if RING['DX']: FIRST_ATK = ATK * 3
        else: FIRST_ATK = ATK * 2
        m_hp -= max(1, FIRST_ATK - m_armor)
    else: m_hp -= max(1, ATK - m_armor)

    # 이제 맞아야함
    if m_hp > 0:
        m_ATK = max(1, m_weapon - SHIELD)
        ATK = max(1, ATK - m_armor)

        player_dead_turn = NOW_HP // m_ATK + (1 if NOW_HP % m_ATK else 0)
        monster_dead_turn = m_hp // ATK + (1 if m_hp % ATK else 0)

        if player_dead_turn <= monster_dead_turn: # 내가 먼저 때렸으므로 내가 죽는 턴이면 내가 죽어야함
            if RING['RE']: # 부활
                RING['RE'] = False
                RING_COUNT -= 1
                x, y = sx, sy
                NOW_HP = FULL_HP
                return
            NOW_HP = 0
            return

        # 몬스터가 먼저 죽을 때
        NOW_HP -= m_ATK * monster_dead_turn
        m_hp -= ATK * monster_dead_turn

    if m_hp <= 0: world_map[x][y] = '.'

    # 전투 종료 -> 경험치 계산 후, 레벨 업
    if RING['EX']: NOW_EXP += int(m_exp * 1.2)
    else: NOW_EXP += m_exp

    if NOW_EXP >= FULL_EXP:
        LV += 1
        FULL_HP += 5
        NOW_HP = FULL_HP
        ATT += 2
        DEF += 2
        FULL_EXP += 5
        NOW_EXP = 0
    if RING['HR']:
        NOW_HP = min(NOW_HP + 3, FULL_HP)

def boss():
    global LV, FULL_HP, NOW_HP, ATT, DEF, FULL_EXP, NOW_EXP, RING_COUNT, x, y, KILL_BOSS

    monster_idx = monster_map[x][y]
    m_name, m_weapon, m_armor, m_hp, m_exp = monster_info[monster_idx]
    ATK = ATT + WEAPON
    SHIELD = DEF + ARMOR

    # 첫 공격에 CO 적용 유무
    if RING['CO']:
        FIRST_ATK = ATK
        if RING['DX']: FIRST_ATK = ATK * 3
        else: FIRST_ATK = ATK * 2
        m_hp -= max(1, FIRST_ATK - m_armor)
    else: m_hp -= max(1, ATK - m_armor)

    # HU가 있으면 풀피 회복 및 보스 첫 공격 무시라 다시 플레이어 공격함
    if RING['HU'] and m_hp > 0:
        m_ATK = max(1, m_weapon - SHIELD)
        ATK = max(1, ATK - m_armor)
        NOW_HP = FULL_HP

        player_dead_turn = NOW_HP // m_ATK + (1 if NOW_HP % m_ATK else 0)
        monster_dead_turn = m_hp // ATK + (1 if m_hp % ATK else 0)

        if player_dead_turn < monster_dead_turn:
            if RING['RE']: # 부활
                RING['RE'] = False
                RING_COUNT -= 1
                x, y = sx, sy
                NOW_HP = FULL_HP
                return
            NOW_HP = 0
            return
        # 몬스터가 먼저 죽을 때
        NOW_HP -= m_ATK * (monster_dead_turn - 1)
        m_hp -= ATK * monster_dead_turn
    elif m_hp > 0: # HU가 없으면 보스 공격부터 하면 댐
        m_ATK = max(1, m_weapon - SHIELD)
        ATK = max(1, ATK - m_armor)

        player_dead_turn = NOW_HP // m_ATK + (1 if NOW_HP % m_ATK else 0)
        monster_dead_turn = m_hp // ATK + (1 if m_hp % ATK else 0)

        if player_dead_turn <= monster_dead_turn:
            if RING['RE']: # 부활
                RING['RE'] = False
                RING_COUNT -= 1
                x, y = sx, sy
                NOW_HP = FULL_HP
                return
            NOW_HP = 0
            return

        NOW_HP -= m_ATK * monster_dead_turn
        m_hp -= ATK * monster_dead_turn

    if m_hp <= 0:
        world_map[x][y] = '.'
        KILL_BOSS = 1

    if RING['EX']: NOW_EXP += int(m_exp * 1.2)
    else: NOW_EXP += m_exp

    if NOW_EXP >= FULL_EXP:
        LV += 1
        FULL_HP += 5
        NOW_HP = FULL_HP
        ATT += 2
        DEF += 2
        FULL_EXP += 5
        NOW_EXP = 0
    if RING['HR']:
        NOW_HP = min(NOW_HP + 3, FULL_HP)

def game_end(reason):
    global NOW_HP
    NOW_HP = max(0, NOW_HP)
    if NOW_HP > 0: world_map[x][y] = '@'
    for i in range(n):
        for j in range(m):
            print(world_map[i][j], end='')
        print()
    print(f'Passed Turns : {TURN}')
    print(f'LV : {LV}')
    print(f'HP : {NOW_HP}/{FULL_HP}')
    print(f'ATT : {ATT}+{WEAPON}')
    print(f'DEF : {DEF}+{ARMOR}')
    print(f'EXP : {NOW_EXP}/{FULL_EXP}')
    if NOW_HP == 0:
        if reason == '^': print('YOU HAVE BEEN KILLED BY SPIKE TRAP..')
        else:
            monster_idx = monster_map[x][y]
            monster_name = monster_info[monster_idx][0]
            print(f'YOU HAVE BEEN KILLED BY {monster_name}..')
    elif KILL_BOSS == 1:
        print('YOU WIN!')
    else:
        print('Press any key to continue.')


'''
########### 게임 진행 로직 ###########
'''
world_map[x][y] = '.'
for _ in range(len(move)):
    x, y = movable(move[_], x, y)
    TURN += 1
    if world_map[x][y] in ['^', '&', 'M', 'B']:
        if world_map[x][y] == '^': trap()
        elif world_map[x][y] == '&': monster()
        elif world_map[x][y] == 'M':
            boss()
            if KILL_BOSS: break
        else: chest()

    if NOW_HP <= 0:
        game_end(world_map[x][y])
        exit()
game_end('.')

'''
- R (행)
- C (열)
- S (몬스터 이름)
- W (몬스터 공격력)
- A (몬스터 방어력)
- H (몬스터 체력)
- E (몬스터 경험치)

########### 게임 정보 ###########
1) 빈 칸(.) : 자유롭게 입장 가능 (@: 주인공 시작 위치)
2) 벽(#) : 이동 불가
3) 아이템 상자(B) - 얻으면 빈 칸으로 변하고 이동 가능
    - 무기(W) : 얻은 장비로 무조건 교체
    - 갑옷(A) : 얻은 장비로 무조건 교체
    - 장신구(O) : 착용 칸이 남았고, 동일한 효과의 장신구가 아니면 장신구를 착용함
4) 가시 함정 (^) : 5의 데미지를 얻음 (함정은 사라지지 않음 - 제자리로 이동해도 데미지를 받음)
5) 몬스터 (&, M)
    - 정보 : 이름, 공격력, 방어력, 체력, 경험치
    - 전투: 서로 데미지를 max(1, 내 공격력 - 상대의 방어력)으로 입힐 수 있음
    - 한 명이 죽을 때까지 과정을 한 턴 내에 이루어짐
    - 보스 몬스터 : M (게임의 목표) 

########### 주인공 정보 ###########
1) 초기 스탯: 체력 20, 공격력 2, 방어력 2
2) 경험치 : 레벨 1로 시작함. 레벨 N → 레벨 N+1이 되기 위해 필요한건 5xN의 경험치
3) 레벨업
    - 최대 체력 5 상승, 공격력 2 상승, 방어력 2 상승, HP 모두 회복
    - 경험치는 0으로 되돌아감
4) 장비
    - 무기 : 한 개만 착용 가능 (주인공의 공격력 + 무기 공격력) → 장신구의 공격력은 최종 공격력에 얻을 수 있음
    - 방어구 : 한 개만 착용 가능 (주인공의 방어력 + 방어구 방어력)
    - 장신구 : 최대 4개
        - HP : 전투에서 승리할 때마다 체력을 3 회복한다
        - RE : 사망 했을 때 사라지는 대신 주인공을 최대 체력으로 부활시킴 (부활 장소 : 첫 시작 위치) + 전투 중인 몬스터가 있으면 최대 체력으로 올라감
        - CO : 모든 전투에서 첫 번째 공격이 주인공의 공격력의 두 배로 적용 = max(1, 공격력x2 - 몬스터의 방어력)
        - EX : 경험치 획득량 1.2배. 소수점 아래는 버림
        - DX : 가시 함정에 입는 데미지가 1로 고정. 이때 CO를 착용하고 있으면 공격력 효과가 두 배에서 세 배로 적용됨
        - HU : 보스 몬스터와 전투에 돌입하는 순간, 체력을 최대치로 회복함 + 보스 몬스터의 첫 공격에 0 데미지를 입음
        - CU : 아무 능력 없음

########### 게임 진행 방법 ###########
1) 주인공은 상하좌우로 한 칸 이동하고, 이벤트 발생
2) 입력이 끝나지 않았는데, 게임이 종료됐을 경우엔 남은 입력은 모두 무시함
'''
