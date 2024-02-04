# Это программа на Python
# Обрезка видео

# Импортируем модуль
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip

# Укажите путь к исходному видеофайлу
source_video = "source.mp4"

# Укажите путь к выходному видеофайлу
output_video = "output.mp4"

# Укажите начальное и конечное время в секундах
start_time = 0
end_time = 10 * 60  # 10 минут

# Обрезка видео
ffmpeg_extract_subclip(source_video, start_time, end_time, targetname=output_video)
