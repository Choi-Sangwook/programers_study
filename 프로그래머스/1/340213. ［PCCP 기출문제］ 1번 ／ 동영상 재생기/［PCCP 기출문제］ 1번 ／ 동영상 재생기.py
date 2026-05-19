def solution(video_len, pos, op_start, op_end, commands):
    video_min = int(video_len.split(':')[0])
    video_sec = int(video_len.split(':')[1])
    total_video_sec = video_min * 60 + video_sec
    
    op_start_min = int(op_start.split(':')[0])
    op_start_sec = int(op_start.split(':')[1])
    total_op_st_sec = op_start_min * 60 + op_start_sec
    
    op_end_min = int(op_end.split(':')[0])
    op_end_sec = int(op_end.split(':')[1])
    total_op_ed_sec = op_end_min * 60 + op_end_sec
    
    pos_min = int(pos.split(':')[0])
    pos_sec = int(pos.split(':')[1])
    total_pos_sec = pos_min * 60 + pos_sec

    if total_op_st_sec <= total_pos_sec <= total_op_ed_sec:
        total_pos_sec = total_op_ed_sec

    for i in commands:
        if i == 'next':
            total_pos_sec += 10
            if total_pos_sec > total_video_sec:
                total_pos_sec = total_video_sec

        elif i == 'prev':
            total_pos_sec -= 10
            if total_pos_sec < 0:
                total_pos_sec = 0

        if total_op_st_sec <= total_pos_sec <= total_op_ed_sec:
            total_pos_sec = total_op_ed_sec

    total_min = total_pos_sec // 60
    total_sec = total_pos_sec % 60

    answer = f"{total_min:02d}:{total_sec:02d}"
    return answer