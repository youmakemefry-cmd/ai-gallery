import os
import json
import re

json_file = 'gallery.json'
existing_titles = {}

# Сохраняем старые кастомные названия, если они есть
if os.path.exists(json_file):
    try:
        with open(json_file, 'r', encoding='utf-8') as f:
            old_data = json.load(f)
            if '_titles' in old_data:
                existing_titles = old_data['_titles']
    except Exception as e:
        print(f"Не удалось прочитать старый JSON: {e}")

data = {}
titles = {}

# Функция для натуральной сортировки (как в Windows: 1, 2, 10, а не 1, 10, 2)
def natural_sort_key(text):
    return [int(c) if c.isdigit() else c.lower() for c in re.split(r'(\d+)', text)]

valid_folders = []

# Шаг 1: Собираем папки
for folder_name in os.listdir('.'):
    # Берем только папки и игнорируем скрытые/системные (например, .git)
    if os.path.isdir(folder_name) and not folder_name.startswith('.'):
        images = [f for f in os.listdir(folder_name) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.webp', '.gif'))]
        
        if len(images) >= 2:
            # Сортируем файлы внутри папки как в проводнике
            sorted_images = sorted(images, key=natural_sort_key)
            
            # Получаем время создания папки для выстраивания хронологии
            creation_time = os.path.getctime(folder_name)
            
            # Сохраняем структуру: (время создания, имя папки, отсортированный список картинок)
            valid_folders.append((creation_time, folder_name, sorted_images))

# Шаг 2: Сортируем сами папки по времени создания (хронологически: от старых к новым)
valid_folders.sort(key=lambda x: x[0])

# Шаг 3: Заполняем словари
for _, folder_name, sorted_images in valid_folders:
    data[folder_name] = sorted_images
    
    # Если имя папки уже меняли руками, оставляем его
    if folder_name in existing_titles:
        titles[folder_name] = existing_titles[folder_name]
    else:
        # Берем имя ВТОРОЙ фотки в подборке (индекс 1)
        second_img_full_name = sorted_images[1]
        
        # Отрезаем расширение (.png, .jpg), чтобы название выглядело чисто
        second_img_name = os.path.splitext(second_img_full_name)[0]
        
        titles[folder_name] = second_img_name

# Собираем итоговый объект
final_data = {'_titles': titles}
final_data.update(data)

with open(json_file, 'w', encoding='utf-8') as f:
    json.dump(final_data, f, ensure_ascii=False, indent=2)

print("gallery.json успешно пересобран по хронологии с авто-названиями из вторых фото!")