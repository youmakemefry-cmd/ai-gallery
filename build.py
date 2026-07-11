import os
import json

json_file = 'gallery.json'
existing_titles = {}

# Если файл уже существует, достаем сохраненные кастомные названия
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

# Шаг 1: Собираем все подходящие папки в список
valid_folders = []
for folder_name in os.listdir('.'):
    if os.path.isdir(folder_name) and folder_name.isdigit():
        images = [f for f in os.listdir(folder_name) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.webp', '.gif'))]
        if len(images) >= 2:
            # Сохраняем структуру: (числовой номер папки, имя папки строкой, список картинок)
            valid_folders.append((int(folder_name), folder_name, sorted(images)))

# Шаг 2: Сортируем папки строго по возрастанию их номеров (1, 2, 3... 9, 10, 11)
valid_folders.sort(key=lambda x: x[0])

# Шаг 3: Заполняем словари по идеальному порядку
for _, folder_name, sorted_images in valid_folders:
    data[folder_name] = sorted_images
    
    # Сохраняем старое имя, если оно было изменено вручную, иначе пишем дефолтное
    if folder_name in existing_titles:
        titles[folder_name] = existing_titles[folder_name]
    else:
        titles[folder_name] = f"Folder #{folder_name}"

# Собираем итоговый объект. В Python 3.7+ порядок ключей при записи сохраняется!
final_data = {'_titles': titles}
final_data.update(data)

with open(json_file, 'w', encoding='utf-8') as f:
    json.dump(final_data, f, ensure_ascii=False, indent=2)

print("gallery.json успешно пересобран строго по числовому порядку полок!")