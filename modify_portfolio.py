import re

with open('src/app/pages/Portfolio.tsx', 'r') as f:
    content = f.read()

# Replace Imports
import_block = """import ledSignage from "../../assets/6e7025d0f5bf2d57099bad163673cfc1e536634e.png";
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

new_imports = """import imgMeghraj from "../../assets/meghraj-1.png";
import imgParagon from "../../assets/paragon-1.png";
import imgSafehouse from "../../assets/safehouse-1.png";
import imgSocialPanga from "../../assets/socialpanga-1.png";
import imgReltio from "../../assets/reltio-1.png";
import imgCleartax from "../../assets/cleartax-1.png";"""

content = content.replace(import_block, new_imports)

# Replace ALL_PROJECTS array
old_proj_start = content.find("const ALL_PROJECTS = [")
old_proj_end = content.find("];\n\nconst FILTERS = [", old_proj_start) + 2

new_proj = """const ALL_PROJECTS = [
  { id: 1,  title: "Meghraj Jewellers",   category: "retail",   image: imgMeghraj,       description: "2000 sqft premium retail space execution completed in 90 days." },
  { id: 2,  title: "Paragon KG Road",     category: "retail",   image: imgParagon,       description: "700 sqft signature retail store delivered in 30 days." },
  { id: 3,  title: "Safe House",          category: "fb",       image: imgSafehouse,     description: "3000 sqft gastro pub with an industrial theme completed in 90 days." },
  { id: 4,  title: "Social Panga",        category: "office",   image: imgSocialPanga,   description: "2580 sqft vibrant office design delivered in 60 days." },
  { id: 5,  title: "Reltio",              category: "office",   image: imgReltio,        description: "1300 sqft modern corporate office interior completed in 30 days." },
  { id: 6,  title: "Cleartax",            category: "office",   image: imgCleartax,      description: "1000 sqft dynamic workspace design delivered in 30 days." },
];"""
content = content[:old_proj_start] + new_proj + content[old_proj_end:]

# Replace FILTERS array
old_filt_start = content.find("const FILTERS = [")
old_filt_end = content.find("];\n\nexport function Portfolio() {", old_filt_start) + 2

new_filt = """const FILTERS = [
  { id: "all",         label: "All Projects" },
  { id: "retail",      label: "Retail Design" },
  { id: "office",      label: "Office Interiors" },
  { id: "fb",          label: "F&B / Hospitality" },
];"""
content = content[:old_filt_start] + new_filt + content[old_filt_end:]

content = content.replace("10,000+", "500+")

with open('src/app/pages/Portfolio.tsx', 'w') as f:
    f.write(content)
