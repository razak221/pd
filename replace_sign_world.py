import os
import re

files_to_update = [
    'index.html',
    'src/lib/db.ts',
    'src/app/components/LiveChat.tsx',
    'src/app/components/Header.tsx',
    'src/lib/storage.ts',
    'src/app/pages/admin/AdminLayout.tsx',
    'src/app/pages/admin/AdminMessages.tsx',
    'src/app/pages/admin/AdminLogin.tsx',
    'supabase-schema.sql'
]

for file_path in files_to_update:
    if os.path.exists(file_path):
        with open(file_path, 'r') as f:
            content = f.read()
        
        # Replace specific strings
        content = content.replace("Sign World Prints", "Pristine Decore")
        content = content.replace("Sign World", "Pristine Decore")
        content = content.replace("printing and signage needs", "interior design needs")
        content = content.replace("Premium Signage & Printing Solutions", "Premium Interior Design & Execution")
        content = content.replace("Premium Signage & Printing", "Premium Interior Design & Execution")
        
        with open(file_path, 'w') as f:
            f.write(content)

print("Done replacing Sign World occurrences.")
