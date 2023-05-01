import argparse
import os
import subprocess
import urllib.parse
import traceback


player_path = "D:\ProgramFiles\PotPlayer\PotPlayerMini64.exe" 
try:
    # argument parse and get protocol string
    parser1 = argparse.ArgumentParser(description='player协议')
    parser1.description = 'player协议'
    parser1.add_argument("parg1", type=str, help='对第一个位置参数的说明')
    args = parser1.parse_args()
    protocol_str = args.parg1
    protocol_str = urllib.parse.unquote(protocol_str)  # url字符转义

    # check protocol title
    protocol_name = "player"
    if protocol_str[:len(protocol_name)+3] != r"player://":
        raise RuntimeError("protocol title is not 'palyer://' !")
    else:
        protocol_str = protocol_str[len(protocol_name)+3:]

    # check timestamp 
    "协议格式为：player://视频路径#起始时间戳-结束时间戳，其中结束时间戳先不管"
    if "#" not in protocol_str:  # no timestamp
        file_path = protocol_str
        start_hour_str = "0"
        start_minute_str = "0"
        start_second_str = "0"
        end_hour_str = "0"  # 其实结束时间戳就没实现，这代码没用
        end_minute_str = "0"  # 其实结束时间戳就没实现，这代码没用
        end_second_str = "0"  # 其实结束时间戳就没实现，这代码没用
    else:  # have timestamp
        hash_index = protocol_str.index("#")
        file_path = protocol_str[:hash_index]
        time_str = protocol_str[hash_index+1:]
        time_split = time_str.split("-")
        start_time_str = time_split[0]
        end_time_str = ""  # 其实结束时间戳就没实现，这代码没用
        # 处理开始时间
        if 1:
            start_time_split = start_time_str.split(":")
            start_second = int(start_time_split[-1]) if len(start_time_split) >= 1 else 0
            start_minute = int(start_time_split[-2]) if len(start_time_split) >= 2 else 0
            start_hour = int(start_time_split[-3]) if len(start_time_split) >= 3 else 0
            if len(start_time_split) > 3:
                print("error 2")
                input()
            #
            start_sum = start_second + start_minute*60 + start_hour*3600
            #
            start_hour_str = str(start_sum // 3600)
            start_minute_str = str(start_sum % 3600 // 60)
            start_second_str = str(start_sum % 60)
        # 处理结束时间
        pass  # 其实结束时间戳就没实现，这代码没用
    # 
    print(f"fp:{file_path}")
    file_path = file_path.replace("%5C", "/")
    if file_path[-1] == "/":
        file_path = file_path[:-1]
    command = fr'{player_path} "{file_path}" /seek={start_hour_str}:{start_minute_str}:{start_second_str}.0'
    print(f"command:{command}")
    subprocess.Popen(command)  # run(command) os.popen(command) os.system(command)
    os.system("exit")  # 如果要调试，就注释掉这一句
except Exception:
    traceback.print_exc()
    input()
