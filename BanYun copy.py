import yt_dlp
import requests
import os

import yt_dlp
import requests
import os

def download_youtube_video(url, output_folder):
    try:
        ydl_opts = {
            'outtmpl': f'{output_folder}/%(title)s.%(ext)s',
            'format': 'bv*+ba/best',
            'merge_output_format': 'mp4',
            'ffmpeg_location': 'E:/ffmpeg-7.0.2-essentials_build/bin/ffmpeg.exe',

            # 🔥关键：伪装浏览器 + 使用cookies
            'http_headers': {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
                'Accept-Language': 'en-US,en;q=0.9'
            },
            'cookiefile': r'E:\Desktop\Youtube_video_LEGO\Youtube_Video_Download\www.youtube.com_cookies.txt',

            'retries': 10,
            'fragment_retries': 10,
            'skip_unavailable_fragments': True,

            # 避免断点续传导致403
            'continuedl': False,
            'nocheckcertificate': True,
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

        print(f"视频已成功下载到 {output_folder}")

    except Exception as e:
        print(f"发生错误: {e}")


def remove_time_param(youtube_url):
    # 找到 '?t=' 或 '&t=' 的起始位置
    time_param_pos = youtube_url.find('&t=')
    
    # 如果找不到 &t=，就找 ?t=
    if time_param_pos == -1:
        time_param_pos = youtube_url.find('?t=')
    
    # 如果找到 't' 参数
    if time_param_pos != -1:
        # 从找到的位置开始，直到找到下一个 '&' 或字符串结束
        end_pos = youtube_url.find('&', time_param_pos + 1)
        
        # 如果找到下一个 '&'，则去除 't=xxs' 这段参数
        if end_pos != -1:
            youtube_url = youtube_url[:time_param_pos] + youtube_url[end_pos:]
        else:
            youtube_url = youtube_url[:time_param_pos]
    
    # 如果只有一个 '?'，去掉它
    if youtube_url[-1] == '?':
        youtube_url = youtube_url[:-1]
    
    return youtube_url

def get_video_info(url):
    try:
        # 使用 yt_dlp 的 YoutubeDL 类获取视频信息
        with yt_dlp.YoutubeDL() as ydl:
            info_dict = ydl.extract_info(url, download=False)
            title = info_dict.get('title', '未知标题')
            uploader = info_dict.get('uploader', '未知作者')
            print()
            print(f"来源: {remove_time_param(url)}")
            print(f"原标题: {title}")
            print(f"发布者: {uploader}")
            print()
    except Exception as e:
        print(f"发生错误: {e}")

def download_video_thumbnail(url, output_folder):
    try:
        # 使用 yt_dlp 获取视频信息
        with yt_dlp.YoutubeDL() as ydl:
            info_dict = ydl.extract_info(url, download=False)
            thumbnail_url = info_dict.get('thumbnail')
            
            if not thumbnail_url:
                print("无法获取视频的封面")
                return
            
            # 获取封面文件名
            thumbnail_filename = os.path.join(output_folder, os.path.basename(thumbnail_url))
            
            # 下载封面
            response = requests.get(thumbnail_url)
            if response.status_code == 200:
                with open(thumbnail_filename, 'wb') as f:
                    f.write(response.content)
                print(f"封面已成功下载到 {thumbnail_filename}")
            else:
                print("无法下载封面")
                
    except Exception as e:
        print(f"发生错误: {e}")

def BanYun(url,output_folder):
    download_youtube_video(url, output_folder)
    #download_video_thumbnail(url, output_folder)
    get_video_info(url)





url = 'https://www.youtube.com/@IronBrick96/videos'
output_folder = "Video"
BanYun(url,output_folder)

