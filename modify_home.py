import re

with open('src/app/pages/Home.tsx', 'r') as f:
    content = f.read()

# Replace Imports
old_imports = """import ledSignage from "../../assets/6e7025d0f5bf2d57099bad163673cfc1e536634e.png";
import backLight from "../../assets/403c1199464256ac90b1ecca1d59649dc2d0dbef.png";
import frontLight from "../../assets/d0ce665437f8f0456bf97f05fc20f321ed58c8dd.png";
import vinylBranding from "../../assets/d1f28106930ee5834bea7b4bfb0fb7becbc0f871.png";
import metalLetters from "../../assets/d7bc7a37ce186421a801bc4f8bb301881fd1ec2f.png";
import flexPrinting from "../../assets/2eaac58e7610a969b8193473d957111135848359.png";
import ecoSolvent from "../../assets/92d28b1ce92d3ab83d434c6baee10e34bd6f23e0.png";
import pamphlets from "../../assets/efb1e0ab435aabe3ceb6354313b0dde45ea3fb1d.png";

// Missing Figma assets replaced with curated photo URLs
const hoardings        = "https://images.unsplash.com/photo-1556742049-0cfed4f6a45d?w=800&q=80";
const acp              = "https://images.unsplash.com/photo-1497366216548-37526070297c?w=800&q=80";
const neonBoards       = "https://images.unsplash.com/photo-1520034475321-cbe63696469a?w=800&q=80";
const acrylic          = "https://images.unsplash.com/photo-1558618666-fcd25c85cd64?w=800&q=80";
const digitalSignages  = "https://images.unsplash.com/photo-1611532736597-de2d4265fba3?w=800&q=80";
const electionBanners  = "https://images.unsplash.com/photo-1540910419892-4a36d2c3266c?w=800&q=80";
const menuBoards       = "https://images.unsplash.com/photo-1414235077428-338989a2e8c0?w=800&q=80";
const vehicleSignages  = "https://images.unsplash.com/photo-1558618047-f4e80e930b6f?w=800&q=80";
const exhibitionStalls = "https://images.unsplash.com/photo-1540575467063-178a50c2df87?w=800&q=80";
const businessCards    = "https://images.unsplash.com/photo-1572021335469-31706a17aaef?w=800&q=80";"""

new_imports = """import retailSpace from "../../assets/meghraj-1.png";
import officeDesign from "../../assets/socialpanga-1.png";
import fbDesign from "../../assets/safehouse-1.png";
import clientele from "../../assets/clientele.png";"""

content = content.replace(old_imports, new_imports)

# Stats
content = content.replace(
    'label: "Projects Completed"',
    'label: "Projects Delivered"'
).replace(
    'number: 10000',
    'number: 500'
).replace(
    'number: 35',
    'number: 20' # adjust experience
)

# Services
old_services_start = content.find("const services = [")
old_services_end = content.find("];\n\nconst features = [", old_services_start) + 2

new_services = """const services = [
  {
    title: "Retail Design",
    description: "Creating immersive retail spaces that captivate customers and drive engagement.",
    image: retailSpace,
    icon: Building2,
    gradient: "from-yellow-500 via-orange-500 to-red-500"
  },
  {
    title: "Office Interiors",
    description: "Designing modern, productive workspaces tailored to your company's culture.",
    image: officeDesign,
    icon: Users,
    gradient: "from-blue-500 via-purple-500 to-pink-500"
  },
  {
    title: "F&B Settings",
    description: "Crafting memorable dining and hospitality experiences through conceptual design.",
    image: fbDesign,
    icon: Star,
    gradient: "from-cyan-500 via-blue-500 to-indigo-500"
  },
  {
    title: "3D Rendering",
    description: "High-quality 3D visualizations to preview your dream space before execution.",
    image: "https://images.unsplash.com/photo-1618221195710-dd6b41faaea6?w=800&q=80",
    icon: Eye,
    gradient: "from-green-500 via-teal-500 to-cyan-500"
  },
  {
    title: "Residential Interiors",
    description: "Transforming homes to perfectly reflect your lifestyle and aesthetic.",
    image: "https://images.unsplash.com/photo-1600210492486-724fe5c67fb0?w=800&q=80",
    icon: Lightbulb,
    gradient: "from-pink-500 via-rose-500 to-red-500"
  },
  {
    title: "Commercial Execution",
    description: "End-to-end execution of commercial spaces with uncompromising quality.",
    image: "https://images.unsplash.com/photo-1541888086225-ece6249fa6b3?w=800&q=80",
    icon: Target,
    gradient: "from-indigo-500 via-purple-500 to-pink-500"
  }
];"""

content = content[:old_services_start] + new_services + content[old_services_end:]

# Hero text
content = content.replace("India's Premier Signage Experts", "Premium Interior Designers & Builders")
content = content.replace("Elevate Your", "Unlock Your")
content = content.replace("Brand Presence", "Lifestyle")
content = content.replace("Exquisite printing and avant-garde signage solutions crafted for brands that demand nothing but absolute excellence.", "Pristine Decore enables customers to design their dream space. We offer smart and holistic interior solutions and execution that are perfect to style modern homes and commercial spaces.")

# Marquee Strip
content = content.replace(
    '"LED Signages", "Outdoor Hoardings", "ACP Signage", "Neon Boards",\n            "Vehicle Wraps", "Acrylic Signs", "Metal Letters", "Flex Printing",\n            "Digital Displays", "Exhibition Stalls", "Business Cards", "Vinyl Branding",\n            "LED Signages", "Outdoor Hoardings", "ACP Signage", "Neon Boards",\n            "Vehicle Wraps", "Acrylic Signs", "Metal Letters", "Flex Printing",\n            "Digital Displays", "Exhibition Stalls", "Business Cards", "Vinyl Branding",',
    '"Retail Design", "Office Interiors", "F&B Design", "Residential Spaces",\n            "3D Concept Rendering", "Commercial Execution", "Turnkey Projects", "Space Planning",\n            "Retail Design", "Office Interiors", "F&B Design", "Residential Spaces",\n            "3D Concept Rendering", "Commercial Execution", "Turnkey Projects", "Space Planning",'
)

content = content.replace("Curated precision printing and artisanal signage", "Curated interior design and flawless execution")

content = content.replace("Sign World Prints", "Pristine Decore")
content = content.replace("printing and signage solutions", "interior design and construction")

# Replace FAQ locations and services
content = content.replace("printing needs", "interior needs")
content = content.replace("5-7 days", "4-12 weeks")
content = content.replace("vehicle wraps maybe 1-2 weeks", "complex commercial projects may take 3-6 months")

with open('src/app/pages/Home.tsx', 'w') as f:
    f.write(content)
