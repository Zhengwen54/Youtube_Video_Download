import yt_dlp
import requests
import os

def download_youtube_video(url, output_folder):
    try:
        ydl_opts = {
            'outtmpl': f'{output_folder}/%(title)s.%(ext)s',  # 输出格式
            'format': 'bestvideo+bestaudio/best',  # 下载最清晰的视频和音频并合并
            'merge_output_format': 'mp4',  # 合并后的输出格式
            'ffmpeg_location': 'E:/ffmpeg-7.0.2-essentials_build/bin/ffmpeg.exe',  #  ffmpeg.exe 路径
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





url = "https://www.youtube.com/watch?v=wF440R5p7-8&t=2s"
output_folder = "E:\Desktop\搬运\视频"
BanYun(url,output_folder)


DaiBanYun = [
    "https://rebrickable.com/mocs/MOC-106136/TheOctan/42009-c-model-9397-logging-track/#details",
    'https://www.youtube.com/@MrTekneex/videos',
    "https://www.youtube.com/shorts/s0abjXdFezE"#短视频塔吊
    "https://www.youtube.com/@512TechProj/videos"
    'https://www.youtube.com/watch?v=MtxnVHvTrMk'
    'https://www.youtube.com/@IronBrick96/videos'
    'https://www.youtube.com/playlist?list=PLZnsbSOjLbu2DD17eZVFy9zAN--joQbjR'



    'https://www.flickr.com/photos/rynning/'
    'https://www.youtube.com/@dirtzonebrick/videos'#
    

    'https://rebrickable.com/mocs/MOC-134368/Don_Santos/renault-magnum-solo-with-lift/#details'
    
    'https://www.youtube.com/@tatrovak563/videos'

]
