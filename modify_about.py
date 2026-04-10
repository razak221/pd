import re

with open('src/app/pages/About.tsx', 'r') as f:
    content = f.read()

# Replace texts
old_vision_mission = """The Sign World Story"""
new_vision_mission = """The Pristine Decore Story"""

content = content.replace(old_vision_mission, new_vision_mission)
content = content.replace("Sign World Prints", "Pristine Decore")
content = content.replace("Sign World", "Pristine Decore")
content = content.replace("printing & installation of a wide variety of signages for companies across various portfolios.", "interior design and commercial execution for luxury homes, retail spaces, and corporate offices.")
content = content.replace("signage company", "interior design firm")
content = content.replace("signage solutions", "interior solutions")
content = content.replace("International Sign Forums", "Global Design Consortiums")
content = content.replace("latest sign standards", "latest design trends")
content = content.replace("sign technologies", "design technologies")
content = content.replace("35+", "15+")

# Inject specific mission/vision
vision_text = """<p>
                  <strong className="text-white">Vision:</strong> <strong className="text-primary font-medium">Create beautiful living spaces</strong> that inspire and enable a better lifestyle.
                </p>
                <p>
                  <strong className="text-white">Mission:</strong> Make use of <strong className="text-primary font-medium">quality materials</strong> and our technical expertise to provide smart and holistic interior solutions.
                </p>"""

content = content.replace("""<p>
                  With our office in <strong className="text-white">Bangalore</strong>""", vision_text + """\n                <p>
                  With our office in <strong className="text-white">Bangalore</strong>""")

with open('src/app/pages/About.tsx', 'w') as f:
    f.write(content)
