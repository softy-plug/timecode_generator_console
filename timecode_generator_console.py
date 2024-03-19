import time

# Функция для вычисления таймкода на основе частоты кадров
def get_timecode(frame_rate, total_frames):
    hours = int(total_frames / (frame_rate * 60 * 60))
    minutes = int((total_frames / (frame_rate * 60)) % 60)
    seconds = int((total_frames / frame_rate) % 60)
    frames = int(total_frames % frame_rate)
    return f"{hours:02d}:{minutes:02d}:{seconds:02d}:{frames:02d}"

# Задаем частоту кадров и общее количество кадров
frame_rates = [24, 30, 25, 50, 60, 120]
total_frames = 0

while True:
    # Цикл для отображения таймера и таймкода по каждой частоте кадров
    for frame_rate in frame_rates:
        # Очищаем консоль перед каждым обновлением таймера
        print('\033c', end='')
        
        # Вычисляем и отображаем текущий таймкод
        timecode = get_timecode(frame_rate, total_frames)
        print(f"Таймкод (кадры/сек): {timecode}")
        
        # Увеличиваем общее количество кадров
        total_frames += 1
        
        # Задержка между кадрами для создания эффекта таймера
        time.sleep(1 / frame_rate)

# softy_plug