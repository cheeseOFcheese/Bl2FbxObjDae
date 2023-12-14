import bpy
import os

# Выбор всех объектов в сцене и их выделение
for obj in bpy.context.scene.objects:
    obj.select_set(True)

# Преобразование выбранных объектов в сетки
bpy.ops.object.convert(target='MESH')

# Создание папки для экспорта
export_folder = "C:/tmp/exported_files"
os.makedirs(export_folder, exist_ok=True)

# Экспорт в форматах .obj, .fbx, .dae
file_formats = ['OBJ', 'FBX', 'DAE']

for file_format in file_formats:
    file_path = os.path.join(export_folder, f"exported_file.{file_format.lower()}")
    
    if file_format == 'OBJ':
        bpy.ops.wm.obj_export(filepath=file_path)
    elif file_format == 'FBX':
        bpy.ops.export_scene.fbx(filepath=file_path)
    elif file_format == 'DAE':
        bpy.ops.wm.collada_export(filepath=file_path)
