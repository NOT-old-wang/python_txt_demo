# --coding=utf8--
#分析倍加福摄像头扫描二维码数据的python脚本
import os
filename = raw_input('请输入需要处理的文件名称：')
os.system('rm -f '+filename+'.*' )

right_file = filename + '.right'
time_file = filename + '.time'
time_val = filename + '.time_val'
result_file = filename + '.result'
waring_file = filename + '.waring'

waring_value = 0    #异常阈值
waring_count = 0    #异常计数
sum_time = 0        
max_time = 0
sum_count = 0       #总帧数
right_flag = 0      #正确帧标志

def write(file, string):
    with open(file, 'a') as target:
        target.write(string)

'''
提取正确帧
'''
with open(filename) as file:                
    for line in file:
        if "00 46" in line and right_flag == 0 :
            right_flag = 1
            write(right_file,line)
            time_s = line.split(':')[2].split('(')[0]
            time_ms = line.split('(')[1].split(')')[0]
            Time = time_s + time_ms
            write(time_file,Time +'\n') #总时间
        elif "02 06" in line: 
            right_flag = 0
            
'''
提取时间戳
'''
with open(time_file) as file_object:
    for line in file_object:
        line_new = line
        time_new = (int)(line_new)
        if sum_count >= 1 and time_new > time_old:
            line_val = time_new - time_old
            write(time_val,(str)(line_val) + '\n')
            sum_time += line_val
            if line_val > max_time:
                max_time = line_val 
        sum_count += 1
        line_old = line
        time_old = (int)(line_old)


    print 'sum_count: '+str(sum_count) 
    print 'sum_time: '+str(sum_time)+' ms'
    print 'avg_time: '+str(sum_time / sum_count)+' ms'
    print 'max_time: '+str(max_time)+' ms'     

sum_count = 0 

'''
提取异常帧
'''
waring_value = int(raw_input('请输入异常阈值：'))
with open(time_file) as file_object:
    for line in file_object:
        line_new = line
        time_new = (int)(line_new)
        if sum_count >= 1 and time_new > time_old:
            line_val = time_new - time_old   
        if line_val > waring_value:
            write(waring_file,'-----!!!!!!-----'+(str)(line_val) + '-----!!!!!!-----'+'\n')
            waring_count += 1
        else :
            write(waring_file,(str)(line_val) + '\n') 
        sum_count += 1
        line_old = line
        time_old = (int)(line_old)
    print 'waring_count: '+str(waring_count) 

    write(result_file, 'sum_count: '+str(sum_count)+'\n')
    write(result_file, 'sum_time: '+str(sum_time)+' ms'+'\n')
    write(result_file, 'avg_time: '+str(sum_time / sum_count)+' ms'+'\n')
    write(result_file, 'max_time: '+str(max_time)+' ms'+'\n')
    write(result_file, 'waring_count: '+str(waring_count)+'\n')