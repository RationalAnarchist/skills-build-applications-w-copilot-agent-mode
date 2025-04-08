# Test imports for bson and django
try:
    from bson import ObjectId
    print("bson imported successfully")
except ImportError as e:
    print(f"Error importing bson: {e}")

try:
    from django.core.management.base import BaseCommand
    print("django imported successfully")
except ImportError as e:
    print(f"Error importing django: {e}")
