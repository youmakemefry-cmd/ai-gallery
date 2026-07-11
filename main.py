import os
import json

data = {}
# Ищем все папки-числа в текущей директории
for folder_name in os.listdir('.'):
    if os.path.isdir(folder_name) and folder_name.isdigit():
        images = [f for f in os.listdir(folder_name) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.webp', '.gif'))]
        # Берем только те папки, где есть хотя бы оригинал и 1 обработка
        if len(images) >= 2:
            data[folder_name] = sorted(images)

with open('gallery.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("gallery.json успешно создан!")