# Core modules
from ..core import writeFile

# Third party modules
import secrets

def add(description:str, data:list):
    template = {
        'id': secrets.token_hex(4),
        'description': description,
        'status': False,
    }

    data.append(template)
    writeFile(data)
    print('\n' + '\033[97m' + 'Task created successfully ✨' + '\033[0m')