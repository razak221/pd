import re

with open('src/app/components/Footer.tsx', 'r') as f:
    footer = f.read()

# Footer fixes
footer = footer.replace("Sign World", "Pristine Decore")
footer = footer.replace("Prints & Signage", "Interior Design & Execution")
footer = footer.replace("Professional printing and signage solutions tailored for brands that demand excellence. Precision in every detail.", "Premium interior design and execution for residential, retail, and commercial spaces. Elevating lifestyles through design.")
footer = footer.replace("+917899634299", "+919845302888")
footer = footer.replace("78996 34299", "98453 02888")
# Remove the other two phone numbers
footer = re.sub(r'<a href="tel:\+919844496579"[^>]*>\+91-98444 96579</a>', '', footer)
footer = re.sub(r'<a href="tel:\+919986888937"[^>]*>\+91-99868 88937</a>', '', footer)
footer = footer.replace("info@signworldprints.com", "pristinedecorblr@gmail.com")
footer = footer.replace("# 26 Ground Floor, Harmony Dale,<br />New Bamboo Bazaar Road<br />Bangalore 560 051", "#54/3, 2nd Cross, 1st Main,<br />Near R.T.Nagar Police Station,<br />R.T.Nagar Post, Bengaluru - 560032")
footer = footer.replace("LED & Digital Signages", "Retail Store Design")
footer = footer.replace("ACP & Acrylic Signs", "Office Interiors")
footer = footer.replace("Vehicle Wraps & Branding", "F&B / Hospitality Design")
footer = footer.replace("Flex & Eco-Solvent Printing", "Residential Interiors")
footer = footer.replace("Exhibition Stalls", "Commercial Execution")

with open('src/app/components/Footer.tsx', 'w') as f:
    f.write(footer)


with open('src/app/pages/Contact.tsx', 'r') as f:
    contact = f.read()

# Contact fixes
contact = contact.replace("Sign World Prints", "Pristine Decore")
contact = contact.replace("Sign World", "Pristine Decore")
contact = contact.replace("+91-78996 34299, +91-98444 96579, +91 99868 88937", "+91-9845302888")
contact = contact.replace("+917899634299", "+919845302888")
contact = contact.replace("+91-78996 34299", "+91-98453 02888")
contact = contact.replace("info@signworldprints.com", "pristinedecorblr@gmail.com")
contact = contact.replace("# 26 Ground Floor, Harmony Dale, New Bamboo Bazaar Road, Bangalore 560 051", "#54/3, 2nd Cross, 1st Main, Near R.T.Nagar Police Station, R.T.Nagar Post, Bengaluru - 560032")
contact = contact.replace("# 26 Ground Floor, Harmony Dale<br />\n                  New Bamboo Bazaar Road<br />\n                  Bangalore 560 051", "#54/3, 2nd Cross, 1st Main<br />\n                  Near R.T.Nagar Police Station<br />\n                  R.T.Nagar Post, Bengaluru - 560032")

# Services array
old_services = """const services = [
    "Business Signage",
    "Vehicle Wraps",
    "Banners & Flags",
    "Custom Stickers",
    "Print Materials",
    "Specialty Printing",
    "Other"
  ];"""

new_services = """const services = [
    "Retail Store Design",
    "Office Interiors",
    "F&B / Hospitality Design",
    "Residential Interiors",
    "Commercial Execution",
    "3D Rendering",
    "Other"
  ];"""
contact = contact.replace(old_services, new_services)

with open('src/app/pages/Contact.tsx', 'w') as f:
    f.write(contact)
