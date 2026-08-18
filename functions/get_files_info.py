import os


def get_files_info(working_directory: str, directory: str = ".") -> str:
    try:
        work_dir = os.path.abspath(working_directory)
        target_dir = os.path.normpath(os.path.join(work_dir, directory))
        valid_target_dir = os.path.commonpath([work_dir, target_dir]) == work_dir
        if not valid_target_dir:
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    
        if not os.path.isdir(target_dir):
            return f'Error: "{directory}" is not a directory'
        else:
            file_list = []            
            for name in os.listdir(target_dir):
                full_path = os.path.join(target_dir, name)
                file_list.append(f'{name}: file_size={os.path.getsize(full_path)} bytes, is_dir={os.path.isdir(full_path)}')

            return file_list
                
    except Exception as e:
        return f"Error: {e}"