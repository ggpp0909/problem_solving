def solution(m, musicinfos):
    arr = []
    m = change_sharp(m)
    # print(m)
    for i in range(len(musicinfos)):
        temp = musicinfos[i].split(',')
        s_minute = int(temp[0][0:2]) * 60 + int(temp[0][3:5])  # 분으로 환산
        e_minute = int(temp[1][0:2]) * 60 + int(temp[1][3:5])
        play_time = e_minute - s_minute
        note = temp[3]
        note_arr = change_sharp(note)

        # 악보 만들기 (feat. 지슬)
        note_arr *= (play_time // len(note_arr) + 1)
        note_arr = note_arr[:play_time]
        # music = ''.join(note_arr)
        # if len(note_arr) > len(m):
        #     for j in range(len(note_arr) - len(m)):
        #         if note_arr[j] == m[0]:
        #             flag = 1
        #             for k in range(len(m)):
        #                 if m[k] != note_arr[j + k]:
        #                     flag = 0
        #                     break
        #
        #             if flag:
        #                 arr.append([play_time, temp[2]])
        #                 break
        # elif len(note_arr) < len(m):
        #     break
        # else: #길이가 같을 경우
        #     flag = 1
        #     for j in range(len(note_arr)):
        #         if m[j] != note_arr[j]:
        #             flag = 0
        #             break
        #     if flag:
        #         arr.append([play_time, temp[2]])
        #         break

        if m in note_arr:
            arr.append([play_time, temp[2]])
    if arr:
        arr.sort(key=lambda x: x[0], reverse=True)
        return arr[0][1]
    return "(None)"

# def convert(string):
#     note_arr = []
#     for j in range(len(string)):
#         if string[j] != '#':
#             note_arr.append(string[j])
#         else:
#             note_arr[-1] += '#'
#
#     return note_arr

def change_sharp(melody):
    melody = melody.replace('C#', 'c')
    melody = melody.replace('D#', 'd')
    melody = melody.replace('F#', 'f')
    melody = melody.replace('G#', 'g')
    melody = melody.replace('A#', 'a')
    melody = melody.replace('B#', 'b')
    return melody

# solution("CC#BCC#BCC#BCC#B", ["03:00,03:30,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B"])
solution("A#", ["13:00,13:02,HAPPY,B#A#"])
# print(solution("ABC", ["12:00,12:14,HELLO,CDEFGAB", "13:00,13:14,WORLD,ABCDEF"]))