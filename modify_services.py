import re

with open('src/app/pages/Services.tsx', 'r') as f:
    content = f.read()

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

new_imports = """import retailSpace from "../../assets/meghraj-1.png";
import officeDesign from "../../assets/socialpanga-1.png";
import fbDesign from "../../assets/safehouse-1.png";
import residentialDesign from "../../assets/paragon-2.png"; // Using Paragon interior as placeholder for now
import commercialExec from "../../assets/cleartax-1.png";"""

content = content.replace(import_block, new_imports)

old_serv_start = content.find("const services = [")
old_serv_end = content.find("];\n\n  const process = [", old_serv_start) + 2

new_serv = """const services = [
    {
      icon: Store,
      title: "Retail Design",
      description: "We orchestrate engaging retail experiences that reflect your brand identity while maximizing product display and customer flow.",
      features: [
        "Brand Identity Integration",
        "Spatial Experience Mapping",
        "Custom Fixture Design",
        "Lighting & Display Optimization",
        "Turnkey Execution"
      ],
      image: retailSpace
    },
    {
      icon: Building2,
      title: "Office Interiors",
      description: "Elevate your corporate workspace with modern, ergonomic designs tailored to foster productivity and collaboration.",
      features: [
        "Space & Layout Planning",
        "Acoustic & Lighting Solutions",
        "Ergonomic Furniture Design",
        "Brand Integration",
        "End-to-End Build Out"
      ],
      image: officeDesign
    },
    {
      icon: Lightbulb,
      title: "F&B / Hospitality Design",
      description: "From concept to execution, we craft ambient, immersive dining and hospitality spaces that leave lasting impressions.",
      features: [
        "Thematic Conceptualization",
        "Seating & Capacity Planning",
        "Custom Bar & Counter Design",
        "Venting & Lighting Integration",
        "Material Sourcing & Build"
      ],
      image: fbDesign
    },
    {
      icon: Palette,
      title: "Residential Interiors",
      description: "Unlock your lifestyle with bespoke luxury interiors designed for comfort, function, and aesthetic perfection.",
      features: [
        "Personalized Concept Design",
        "3D Rendering & Visualization",
        "Premium Material Selection",
        "Custom Furniture Fabrication",
        "Flawless Execution"
      ],
      image: residentialDesign
    },
    {
      icon: Zap,
      title: "Commercial Execution",
      description: "Our dedicated construction and project management team handles large-scale commercial implementations with surgical precision.",
      features: [
        "General Contracting",
        "MEP (Mechanical, Electrical, Plum.)",
        "Civil & Structural Works",
        "Quality & Safety Control",
        "On-Time Project Delivery"
      ],
      image: commercialExec
    }
  ];"""
  
content = content[:old_serv_start] + new_serv + content[old_serv_end:]

content = content.replace("Comprehensive Printing <span className=\"text-primary italic font-light\">&</span> Signage Solutions", "Comprehensive Interior Design <span className=\"text-primary italic font-light\">&</span> Execution Focus")
content = content.replace("From visionary concept to flawless installation, we provide end-to-end printing services tailored to elevate your business presence.", "From visionary concept to flawless installation, we provide end-to-end interior design and commercial construction services tailored to elevate your space.")

with open('src/app/pages/Services.tsx', 'w') as f:
    f.write(content)
