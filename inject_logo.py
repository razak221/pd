import os

# Files to modify
header_file = "src/app/components/Header.tsx"
footer_file = "src/app/components/Footer.tsx"

# Add import statements
def inject_import(content, import_stmt):
    if import_stmt not in content:
        # insert after first import
        lines = content.split('\n')
        for i, line in enumerate(lines):
            if line.startswith('import '):
                lines.insert(i + 1, import_stmt)
                return '\n'.join(lines)
    return content

# 1. Update Header.tsx
with open(header_file, "r") as f:
    h_content = f.read()

h_content = inject_import(h_content, 'import logoImg from "../../assets/logo.png";')

logo_html = """            <div className="w-10 h-10 bg-gradient-to-br from-primary to-amber-500 rounded-xl flex items-center justify-center shadow-[0_0_15px_rgba(212,175,55,0.3)] group-hover:shadow-[0_0_25px_rgba(212,175,55,0.5)] transition-shadow">
              <span className="text-black font-black text-lg leading-none">S</span>
            </div>
            <div>
              <div className="font-bold text-xl text-white tracking-tight leading-none group-hover:text-primary transition-colors">Pristine Decore</div>
              <div className="text-[10px] text-primary uppercase tracking-[0.2em] mt-1 font-medium">Prints & Signage</div>
            </div>"""

new_logo_html = """            <img src={logoImg} alt="Pristine Decore Logo" className="h-12 w-auto object-contain transition-transform group-hover:scale-105" />"""

h_content = h_content.replace(logo_html, new_logo_html)
h_content = h_content.replace("// Logo image not available — using text branding fallback", "")

# Fix typo from the previous replacement if any
h_content = h_content.replace("info@signworldprints.com", "pristinedecorblr@gmail.com")
h_content = h_content.replace("+91-78996 34299", "+91-98453 02888")
h_content = h_content.replace("+917899634299", "+919845302888")

with open(header_file, "w") as f:
    f.write(h_content)


# 2. Update Footer.tsx
with open(footer_file, "r") as f:
    f_content = f.read()

f_content = inject_import(f_content, 'import logoImg from "../../assets/logo.png";')

v_logo_html = """              <div className="w-10 h-10 bg-gradient-to-br from-primary to-amber-500 rounded-xl flex items-center justify-center shadow-[0_0_15px_rgba(212,175,55,0.3)] group-hover:shadow-[0_0_25px_rgba(212,175,55,0.5)] transition-shadow duration-300">
                <span className="text-black font-black text-lg leading-none">S</span>
              </div>
              <div>
                <div className="font-bold text-xl text-white tracking-tight group-hover:text-primary transition-colors">Pristine Decore</div>
                <div className="text-[10px] text-primary uppercase tracking-[0.2em] mt-1 font-medium">Interior Design & Execution</div>
              </div>"""

new_v_logo_html = """              <img src={logoImg} alt="Pristine Decore Logo" className="h-14 w-auto object-contain transition-transform group-hover:scale-105" />"""

f_content = f_content.replace(v_logo_html, new_v_logo_html)
f_content = f_content.replace("// Logo image not available — using text branding fallback", "")

with open(footer_file, "w") as f:
    f.write(f_content)

print("Headers and Footers updated with the new logo!")
