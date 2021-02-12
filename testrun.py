import os
from pathlib import Path
import sys
ROOT_DIR = Path(__file__).resolve(strict=True).parent.parent
sys.path.append(str(ROOT_DIR / "ss411"))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.local")

from ss411.users.models import User
ssolist = User.objects.all()
