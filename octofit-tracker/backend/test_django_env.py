# Test Django environment setup
try:
    import django
    print("Django imported successfully")
    print(f"Django version: {django.get_version()}")
except ImportError as e:
    print(f"Error importing Django: {e}")

try:
    from django.conf import settings
    print("Django settings imported successfully")
except ImportError as e:
    print(f"Error importing Django settings: {e}")
