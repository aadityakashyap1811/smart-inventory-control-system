import streamlit as st
import pandas as pd
import plotly.express as px

# ----------------------------------------------------
# Page Configuration
# ----------------------------------------------------
st.set_page_config(
    page_title="Enterprise Smart Inventory Control System",
    page_icon="📦",
    layout="wide"
)

# ----------------------------------------------------
# 1. 50+ COMPANIES REALISTIC INVENTORY DATA GENERATOR
# ----------------------------------------------------
@st.cache_data
def load_initial_data():
    raw_companies = [
        # Automotive & Mobility
        ("Tata Motors - Spares Division", "TM", [
            ("Brake Pads", "Mechanical", 140, 50, 300, 1200),
            ("Engine Oil (5L)", "Fluids", 35, 40, 200, 2400),
            ("Spark Plugs", "Electrical", 12, 60, 500, 350),
            ("Air Filter", "Mechanical", 80, 30, 150, 650),
            ("Lithium Battery Pack", "EV Spares", 5, 10, 50, 45000),
        ]),
        ("Mahindra & Mahindra - Auto Sector", "MM", [
            ("Clutch Plate Assembly", "Transmission", 45, 30, 120, 4800),
            ("Shock Absorbers", "Suspension", 28, 40, 100, 2800),
            ("LED Headlamp Cluster", "Electrical", 15, 20, 60, 6500),
            ("Diesel Fuel Injector", "Fuel System", 60, 50, 180, 5200),
            ("ECU Control Module", "Electronics", 8, 15, 40, 18500),
        ]),
        ("Maruti Suzuki - Components Hub", "MS", [
            ("Brake Rotor Discs", "Brakes", 220, 80, 400, 1800),
            ("Alternator 12V", "Electrical", 30, 40, 100, 4200),
            ("Radiator Coolant (1L)", "Fluids", 450, 200, 800, 280),
            ("Timing Belt Kit", "Engine", 75, 50, 160, 1450),
            ("Cabin AC Filter", "HVAC", 110, 60, 250, 420),
        ]),
        ("Bajaj Auto - Two-Wheeler Spares", "BA", [
            ("Chain Sprocket Kit", "Drivetrain", 180, 60, 350, 1150),
            ("Carburetor Repair Kit", "Fuel System", 40, 50, 120, 680),
            ("Alloy Wheel Rim 17-inch", "Chassis", 18, 25, 60, 3200),
            ("Front Fork Oil (350ml)", "Fluids", 95, 40, 200, 190),
            ("Speedometer Digital Console", "Electronics", 12, 20, 50, 2900),
        ]),
        ("Hero MotoCorp - Parts Warehouse", "HM", [
            ("Piston Ring Set", "Engine", 300, 100, 600, 320),
            ("Brake Shoe Rear", "Brakes", 450, 150, 800, 210),
            ("Halogen Bulb 35W", "Lighting", 600, 200, 1200, 85),
            ("Handlebar Grip Set", "Body", 180, 80, 400, 130),
            ("Ignition Switch Assembly", "Electrical", 65, 50, 150, 480),
        ]),
        ("TVS Motor Company - Fast Moving Spares", "TVS", [
            ("Throttle Cable", "Controls", 210, 80, 400, 160),
            ("Side Mirror Set", "Body", 90, 50, 200, 380),
            ("Disc Brake Caliper", "Brakes", 22, 30, 75, 1850),
            ("Drive Belt (Scooter)", "Transmission", 65, 40, 150, 750),
            ("4T 10W-30 Engine Oil", "Fluids", 320, 100, 500, 390),
        ]),
        ("Ola Electric - Mega Factory Inventory", "OLA", [
            ("Lithium-Ion Cell 21700 (Pack 50)", "Battery", 35, 50, 150, 16500),
            ("BLDC Hub Motor 8.5kW", "Powertrain", 14, 20, 60, 22000),
            ("7-inch TFT Display Cluster", "Infotainment", 9, 25, 70, 8900),
            ("Regenerative Brake Sensor", "Electronics", 70, 40, 160, 850),
            ("Home Fast Charger 750W", "Accessories", 28, 45, 120, 6800),
        ]),

        # Steel, Metals & Heavy Engineering
        ("Tata Steel - Raw & Maintenance", "TS", [
            ("Iron Ore Pellets (Tons)", "Raw Material", 450, 200, 1000, 8500),
            ("Refractory Bricks", "Kiln Spares", 60, 100, 500, 450),
            ("Industrial Lubricant (200L)", "Fluids", 12, 25, 80, 18000),
            ("TMT Rebar 12mm (Tons)", "Finished Goods", 320, 150, 800, 54000),
            ("Conveyor Belt Roll (50m)", "Plant Maintenance", 3, 8, 20, 75000),
        ]),
        ("JSW Steel - Plant Spares", "JSW", [
            ("Coking Coal (Metric Tons)", "Raw Material", 620, 300, 1200, 14200),
            ("Slag Pot Carrier Spares", "Heavy Machinery", 4, 6, 15, 145000),
            ("Hydraulic Valve Block", "Hydraulics", 18, 15, 40, 32000),
            ("Continuous Casting Mold", "Foundry", 2, 5, 12, 280000),
            ("Graphite Electrodes", "Furnace", 25, 20, 60, 45000),
        ]),
        ("Steel Authority of India (SAIL)", "SAIL", [
            ("Dolomite Flux (Tons)", "Raw Material", 800, 400, 1500, 3800),
            ("Blast Furnace Tuyere", "Consumables", 14, 20, 50, 26000),
            ("Hot Strip Mill Rollers", "Rolling Mill", 6, 10, 25, 195000),
            ("Oxygen Lance Nozzle", "Refinery Spares", 45, 30, 100, 8500),
            ("Safety Goggles & Visor (Pack)", "PPE", 350, 150, 600, 450),
        ]),
        ("Jindal Steel & Power (JSPL)", "JSPL", [
            ("Direct Reduced Iron (Sponge Iron)", "Raw Material", 510, 250, 1000, 28500),
            ("Crane Wire Rope (100m)", "Lifting", 8, 12, 30, 38000),
            ("Thermo-Mechanically Treated Billets", "Semi-Finished", 220, 100, 500, 46000),
            ("Furnace Temperature Sensors", "Instrumentation", 38, 25, 80, 4200),
            ("Gearbox Reducer Unit", "Mechanical Drive", 3, 5, 15, 88000),
        ]),
        ("Hindalco Industries - Aluminum Ops", "HAL", [
            ("Calcined Alumina (Tons)", "Raw Material", 380, 200, 800, 34000),
            ("Carbon Anode Blocks", "Smelting", 110, 150, 400, 16500),
            ("Extrusion Die Sets", "Tooling", 15, 20, 50, 42000),
            ("Foil Rolling Coolant (200L)", "Chemicals", 24, 30, 80, 12500),
            ("Aluminum Ingots 99.7% Pure", "Finished Goods", 450, 150, 900, 220000),
        ]),
        ("L&T Heavy Engineering", "LT", [
            ("High Tensile Alloy Bolts (Pack 100)", "Fasteners", 85, 30, 200, 3400),
            ("Hydraulic Cylinder Seal Kit", "Hydraulics", 4, 10, 40, 14500),
            ("MIG Welding Wire Spool (15kg)", "Welding", 40, 50, 150, 2800),
            ("Heavy Duty Industrial Safety Helmets", "Safety PPE", 110, 40, 300, 450),
            ("Pressure Gauge 0-400 Bar", "Instrumentation", 6, 12, 50, 6200),
        ]),
        ("Bharat Heavy Electricals (BHEL)", "BHEL", [
            ("Turbine Rotor Blades", "Turbomachinery", 16, 20, 60, 95000),
            ("Transformer Core Laminations", "Electrical Steel", 90, 50, 200, 14500),
            ("High Voltage Bushing 220kV", "Insulators", 8, 10, 25, 42000),
            ("Stator Winding Copper Bar", "Conductors", 65, 40, 150, 8200),
            ("Boiler Tube Alloy Steel", "Piping", 140, 80, 300, 11500),
        ]),

        # Retail & E-Commerce
        ("Reliance Retail - Electronics", "RR", [
            ("Wireless Mouse", "Accessories", 95, 30, 200, 899),
            ("Mechanical Keyboard", "Accessories", 18, 25, 100, 3200),
            ("27-inch 4K Monitor", "Displays", 8, 15, 50, 22500),
            ("USB-C Fast Charger", "Cables & Power", 150, 50, 400, 1299),
            ("Noise Cancelling Headphones", "Audio", 4, 20, 80, 9999),
        ]),
        ("Flipkart Fulfillment Center", "FK", [
            ("Corrugated Packaging Box (Large)", "Packaging", 2500, 1000, 6000, 35),
            ("Bubble Wrap Roll (100m)", "Packaging", 45, 80, 300, 650),
            ("Handheld Barcode Scanners", "Warehouse Assets", 8, 15, 50, 4500),
            ("Thermal Shipping Labels (Roll)", "Consumables", 350, 120, 800, 280),
            ("Pallet Stretch Film", "Packaging", 18, 40, 150, 520),
        ]),
        ("Amazon India Fulfillment BLR4", "AMZ", [
            ("Self-Adhesive Kraft Tape", "Packing", 800, 300, 1500, 120),
            ("Poly Mailers 12x16 inch", "Packing", 3400, 1500, 8000, 8),
            ("Mobile Barcode RFID Reader", "Equipment", 14, 20, 50, 8500),
            ("Industrial Hand Truck Trolley", "Material Handling", 12, 10, 30, 4200),
            ("Electronic Weighing Scale 50kg", "Inspection", 22, 15, 40, 3100),
        ]),
        ("Tata CLiQ Luxury", "TCL", [
            ("Premium Velvet Storage Pouches", "Packaging", 140, 80, 300, 280),
            ("Branded Rigid Gift Boxes", "Packaging", 85, 100, 400, 350),
            ("RFID Anti-Theft Tags (Box 500)", "Loss Prevention", 12, 20, 50, 4200),
            ("Anti-Static Watch Protectors", "Handling", 210, 100, 500, 150),
            ("Tamper Evident Security Tape", "Dispatch", 45, 30, 100, 420),
        ]),
        ("DMart - Central Distribution Depot", "DM", [
            ("Plastic Shopping Crates (60L)", "Storage", 450, 200, 1000, 480),
            ("Heavy Duty Pallet Racks Beam", "Shelving", 35, 20, 80, 2100),
            ("Price Tag Label Rolls (Packs)", "Store Ops", 600, 250, 1200, 95),
            ("Manual Hydraulic Pallet Truck", "Equipment", 6, 8, 20, 16500),
            ("Shrink Wrap Plastic Roll (3kg)", "Packing", 110, 60, 250, 620),
        ]),
        ("Shoppers Stop - Apparel Logistics", "SS", [
            ("Wooden Suit Hangers (Pack 50)", "Display Spares", 80, 100, 300, 1250),
            ("Garment Steamer Commercial", "Finishing", 5, 8, 20, 6800),
            ("Anti-Theft Hard EAS Tags", "Security", 1200, 500, 3000, 18),
            ("Garment Cover Bags (Clear)", "Protective", 850, 400, 2000, 22),
            ("Barcode Price Tag Gun Needles", "Store Consumables", 40, 30, 100, 350),
        ]),
        ("Nykaa E-Retail - Cosmetic Hub", "NYK", [
            ("Bubble Pouch Small (Box 1000)", "Packaging", 65, 80, 200, 1400),
            ("Pink Customized Corrugated Box", "Branding Packaging", 1800, 800, 4000, 42),
            ("Cosmetic Glass Dropper Flacons", "Packaging Raw", 450, 200, 1000, 35),
            ("Fragile Label Stickers (Roll)", "Dispatch", 180, 90, 400, 180),
            ("Temperature Controlled Gel Packs", "Cold Chain", 340, 200, 800, 65),
        ]),
        ("Titan Company - Watches & Eyewear", "TTN", [
            ("Sapphire Crystal Glass 38mm", "Watch Spare", 120, 60, 300, 1450),
            ("Leather Watch Straps 20mm", "Accessories", 220, 100, 500, 850),
            ("Titanium Eyeglass Frame Hinges", "Eyewear Parts", 95, 50, 250, 320),
            ("Silver Oxide Button Battery 377", "Components", 650, 300, 1500, 45),
            ("Precision Micro Screw Set (1000x)", "Fasteners", 15, 20, 50, 1800),
        ]),

        # Pharmaceuticals & Healthcare
        ("MedLife Pharmaceuticals", "ML", [
            ("Paracetamol 650mg", "Tablets", 1200, 500, 3000, 30),
            ("N95 Surgical Masks", "PPE", 250, 300, 1500, 45),
            ("Hand Sanitizer (500ml)", "Hygiene", 40, 100, 500, 180),
            ("Digital Thermometer", "Devices", 65, 20, 150, 450),
            ("Saline Dextrose IV", "IV Fluids", 15, 50, 250, 110),
        ]),
        ("Sun Pharma Laboratories", "SP", [
            ("Active Pharma Ingredient (API) Atorvastatin", "Raw Material", 45, 30, 100, 24000),
            ("Gelatin Capsule Shells Empty Size 0", "Capsules", 8500, 3000, 20000, 0.45),
            ("Blister Packing Aluminum Foil", "Packaging", 32, 40, 120, 8500),
            ("HPLC Chromatography Column", "QC Lab", 4, 8, 20, 38000),
            ("HEPA Filter Unit for Cleanroom", "Cleanroom HVAC", 6, 10, 25, 28000),
        ]),
        ("Dr. Reddy's Laboratories", "DRL", [
            ("Omeprazole Granules (25kg Drum)", "Raw Material", 18, 20, 50, 65000),
            ("Amber Glass Bottles 100ml", "Primary Packaging", 2400, 1000, 6000, 14),
            ("Microbiological Culture Media", "Micro Lab", 28, 30, 80, 3200),
            ("Nitrogen Gas Cylinders 47L", "Inert Gas", 14, 25, 60, 2200),
            ("Lyophilization Vials 10ml", "Injectables", 1600, 800, 4000, 25),
        ]),
        ("Cipla Respiratory Care", "CIP", [
            ("Salbutamol Metered Dose Inhaler Casing", "Inhalers", 1400, 600, 3500, 85),
            ("HFA Propellant Gas (Cylinder)", "Aerosol Drive", 22, 30, 80, 16500),
            ("Budesonide Micronized Powder (kg)", "API", 8, 12, 30, 125000),
            ("Dry Powder Inhaler Rotahaler Device", "Medical Devices", 450, 200, 1000, 140),
            ("Sterile Cleanroom Coveralls (Tyvek)", "PPE", 85, 100, 300, 650),
        ]),
        ("Apollo Hospitals - Pharmacy Depot", "APO", [
            ("Meropenem Injection 1g", "Antibiotics", 320, 150, 800, 780),
            ("Sterile Disposable Syringes 5ml", "Consumables", 4500, 2000, 10000, 6.5),
            ("IV Cannula 20G Pink (Box 100)", "Consumables", 48, 50, 150, 1200),
            ("ECG Recording Paper Rolls", "Diagnostic Consumables", 85, 40, 200, 180),
            ("Nitrile Examination Gloves (Box 100)", "PPE", 210, 150, 500, 420),
        ]),
        ("Biocon Biologics", "BIO", [
            ("Insulin Glargine Bulk Solution (L)", "Biologics", 14, 20, 50, 185000),
            ("Single-Use Bioreactor Bags 200L", "Fermentation", 8, 12, 30, 48000),
            ("Sterilizing Grade Membrane Filter", "Filtration", 24, 25, 80, 14500),
            ("Cold Chain Cryovials -80C", "Storage Consumables", 1200, 500, 3000, 38),
            ("Monoclonal Antibody Culture Feed", "Media", 35, 40, 100, 29000),
        ]),

        # FMCG, Food & Agriculture
        ("ITC Limited - FMCG & Foods", "ITC", [
            ("Aashirvaad Atta (10kg)", "Staples", 650, 200, 1200, 420),
            ("Sunfeast Dark Fantasy (Packs)", "Biscuits", 90, 150, 800, 40),
            ("Classmate Pulse Spiral Notebook", "Stationery", 400, 100, 1000, 85),
            ("Bingo! Mad Angles (Cartons)", "Snacks", 25, 60, 300, 350),
            ("Fiama Gel Bar (Pack of 3)", "Personal Care", 180, 80, 500, 190),
        ]),
        ("Zomato Hyperpure - B2B Supplies", "ZH", [
            ("Basmati Rice Premium (25kg)", "Grains", 120, 50, 400, 2100),
            ("Refined Sunflower Oil (15L Tin)", "Edible Oils", 22, 40, 200, 1850),
            ("Fresh Paneer (5kg Blocks)", "Dairy", 8, 20, 60, 1400),
            ("Biodegradable Meal Containers (Pack 100)", "Packaging", 550, 200, 1500, 650),
            ("Whole Garam Masala (1kg)", "Spices", 45, 15, 100, 780),
        ]),
        ("Hindustan Unilever Limited (HUL)", "HUL", [
            ("Surf Excel Detergent Powder (5kg)", "Home Care", 420, 150, 900, 680),
            ("Dove Moisturizing Soap (Pack 4)", "Personal Wash", 180, 200, 600, 240),
            ("Red Label Tea Leaf (1kg)", "Beverages", 310, 120, 700, 490),
            ("Linear Alkyl Benzene (LAB)", "Raw Chemical", 45, 30, 100, 135000),
            ("Laminated Pouch Rolls (Printed)", "Packaging Material", 60, 50, 150, 18500),
        ]),
        ("Nestlé India - Moga Factory", "NES", [
            ("Maggi 2-Minute Noodles Carton", "Instant Foods", 850, 300, 2000, 720),
            ("Nescafé Classic Instant Coffee 200g", "Coffee", 140, 150, 500, 640),
            ("Skimmed Milk Powder Bulk (25kg)", "Dairy Raw", 65, 40, 150, 9200),
            ("Palm Olein Oil (Bulk Tanker Share)", "Oils", 28, 30, 80, 84000),
            ("Multi-Layer Barrier Laminates", "Packaging", 42, 50, 120, 22000),
        ]),
        ("Britannia Industries", "BRIT", [
            ("Good Day Butter Cookies Cartons", "Bakery", 410, 180, 900, 580),
            ("Refined Wheat Flour Maida (50kg)", "Raw Staples", 280, 120, 600, 1650),
            ("Speciality Butterfat (Fat Block 15kg)", "Dairy Fat", 48, 50, 140, 6800),
            ("Baking Yeast Commercial (Pack)", "Ingredients", 95, 40, 200, 480),
            ("BOPP Packaging Film (Rolls)", "Wrapping", 38, 45, 100, 14200),
        ]),
        ("Amul - Gujarat Cooperative Depot", "AMUL", [
            ("Amul Salted Butter (500g Packs)", "Dairy Products", 680, 300, 1500, 275),
            ("Amul Pasteurised Toned Milk 1L", "Fresh Dairy", 1200, 800, 3000, 54),
            ("Tetra Pak Aseptic Cartons (Empty)", "Packaging", 5500, 2000, 12000, 4.2),
            ("Ice Cream Wooden Spoons (Box 5000)", "Consumables", 35, 40, 100, 950),
            ("Refrigerated Compressor Spare Filter", "Cold Storage", 8, 12, 30, 7400),
        ]),
        ("Dabur India - Ayurvedic Depot", "DAB", [
            ("Dabur Chyawanprash (1kg)", "Health Supplements", 290, 120, 600, 395),
            ("Organic Raw Forest Honey (Barrel)", "Raw Ingredients", 16, 20, 50, 42000),
            ("Amla Extract (Herb Concentrate)", "Raw Extract", 24, 25, 70, 18500),
            ("PET Bottles 500ml for Vatika Hair Oil", "Bottles", 3200, 1500, 8000, 6.2),
            ("Induction Sealing Wads (Pack 5000)", "Packaging Seal", 45, 30, 100, 1250),
        ]),

        # Technology, IT Hardware & Telecom
        ("Infosys - IT Infrastructure Hub", "INFY", [
            ("Dell OptiPlex Desktop SFF", "Computing Hardware", 45, 30, 120, 58000),
            ("Cisco Catalyst 48-Port Switch", "Networking", 6, 10, 25, 165000),
            ("Cat6 Ethernet Cable Roll 305m", "Cabling", 32, 20, 80, 4800),
            ("SFP+ 10G Fiber Transceiver", "Fiber Optics", 48, 40, 120, 3200),
            ("UPS Battery 12V 100Ah", "Power Backup", 18, 25, 60, 9500),
        ]),
        ("TCS - Campus Assets & Hardware", "TCS", [
            ("ThinkPad Core i7 Laptops", "Laptops", 85, 50, 200, 74000),
            ("Full HD DisplayPort Monitors 24-inch", "Peripherals", 110, 60, 250, 11500),
            ("Polycom IP Conference Phone", "Telecom", 14, 15, 40, 24000),
            ("Server DDR4 64GB ECC RAM", "Server Parts", 28, 30, 80, 16800),
            ("Ergonomic Mesh Office Chair Spares", "Facility", 40, 25, 100, 1450),
        ]),
        ("Wipro Technologies - Data Center", "WIP", [
            ("Blade Server Intel Xeon Scalable", "Servers", 8, 12, 30, 380000),
            ("Enterprise SAS SSD 3.84TB", "Storage", 26, 30, 80, 32000),
            ("Server Rack Cooling Fan Modular", "Cooling", 35, 20, 80, 4200),
            ("PDU Power Distribution Unit 32A", "Electrical", 12, 10, 30, 18500),
            ("KVM Over IP Console Switch", "Infra Management", 4, 6, 15, 68000),
        ]),
        ("Bharti Airtel - Telecom Circle Hub", "AIR", [
            ("4G/5G Remote Radio Unit (RRU)", "Telecom Gear", 14, 20, 50, 145000),
            ("CPRI Optical Fiber Patchcord 50m", "Cables", 120, 80, 300, 1650),
            ("Telecom Tower Aviation Light LED", "Tower Infra", 18, 15, 45, 5800),
            ("Base Station Rectifier Module 48V", "Power", 9, 15, 40, 34000),
            ("RF Coaxial Feeder Cable 7/8 inch", "Cabling", 22, 30, 70, 12500),
        ]),
        ("Reliance Jio - 5G Equipment Store", "JIO", [
            ("5G Massive MIMO Antenna Unit", "Wireless", 12, 25, 60, 290000),
            ("JioFiber Home Gateway Routers", "CPE Devices", 420, 200, 1000, 1950),
            ("Fiber Splice Protection Sleeves", "Consumables", 2800, 1000, 6000, 3.5),
            ("Outdoor Optical Splice Enclosure", "Infra", 75, 40, 180, 2600),
            ("Diesel Generator AVR Controller", "Power Backup", 15, 20, 50, 8900),
        ]),

        # Energy, Oil & Gas, Renewables
        ("Oil and Natural Gas Corporation (ONGC)", "ONGC", [
            ("Tricone Drill Bit 8-1/2 inch", "Drilling Tool", 8, 12, 30, 185000),
            ("Drill Pipe Casing Alloy (Joints)", "Casing", 65, 40, 150, 45000),
            ("High Pressure Mud Pump Valve", "Drilling Rig Spares", 14, 20, 50, 38000),
            ("Wellhead Choke Valve 10,000 PSI", "Pressure Control", 3, 6, 15, 320000),
            ("Oil Spill Absorbent Booms (Pack)", "Safety Environment", 45, 30, 100, 6500),
        ]),
        ("Indian Oil Corporation (IOCL)", "IOCL", [
            ("Crude Distillation Heat Exchanger Tube", "Refinery Spares", 42, 30, 100, 16500),
            ("Hydrotreating Catalyst (Metric Ton)", "Refining Catalysts", 6, 10, 25, 450000),
            ("Digital Petrol Dispenser Nozzle", "Marketing Spares", 55, 40, 120, 7800),
            ("Flammable Gas Detection Sensors", "Safety Instrumentation", 32, 20, 80, 12500),
            ("LPG Cylinder Brass Valves (Box 100)", "LPG Bottling", 95, 60, 250, 18500),
        ]),
        ("Bharat Petroleum (BPCL)", "BPCL", [
            ("Cryogenic Loading Arm Seals", "Terminal Spares", 12, 15, 40, 28000),
            ("High Octane Aviation Fuel Filter", "Aviation Spares", 18, 20, 60, 34000),
            ("Explosion-Proof Motor 15kW", "Electrical", 5, 8, 20, 72000),
            ("Pipeline Ultrasonic Flowmeter", "Metering", 4, 6, 15, 145000),
            ("Cast Steel Gate Valve 6-inch 300#", "Piping", 22, 18, 50, 24000),
        ]),
        ("Adani Green Energy", "AGE", [
            ("Bifacial Solar Photovoltaic Module 540W", "Solar Modules", 350, 200, 800, 8900),
            ("Central String Inverter 250kW", "Inverters", 6, 10, 25, 480000),
            ("Solar Tracker Slew Drive Motor", "Tracker Mechanics", 24, 30, 80, 24500),
            ("MC4 Solar Connectors Male/Female", "Electrical", 1500, 600, 3000, 45),
            ("Solar Pyranometer Radiation Sensor", "Meteo Station", 5, 8, 20, 65000),
        ]),
        ("Tata Power Solar - EPC Warehouse", "TPS", [
            ("Mono PERC Solar Cells (Lot 1000)", "Manufacturing", 45, 50, 150, 55000),
            ("Solar Cable 4 sq mm (Roll 500m)", "DC Cabling", 60, 40, 150, 14500),
            ("Lightning Arrester 33kV", "Substation Protection", 14, 15, 40, 18500),
            ("Aluminum Solar Mounting Rail 4.2m", "Structure", 380, 200, 900, 1250),
            ("Array Junction Box with SPD", "BOS Components", 32, 25, 75, 8200),
        ]),
        ("Suzlon Energy - Wind Spares", "SUZ", [
            ("Wind Turbine Rotor Blade Bearing", "Turbine Mechanical", 2, 4, 10, 420000),
            ("Pitch Control Servo Drive", "Control Systems", 7, 10, 25, 89000),
            ("Hydraulic Yaw Brake Caliper", "Brakes", 15, 18, 45, 26000),
            ("Wind Anemometer Ultrasonic 24V", "Instrumentation", 11, 15, 35, 18500),
            ("Synthetic Gearbox Lubricant 208L", "Specialty Fluids", 16, 20, 50, 68000),
        ]),

        # Aerospace, Defense & Shipping
        ("Hindustan Aeronautics Limited (HAL)", "HALD", [
            ("Avionics Radar Processing Card", "Radar & Avionics", 4, 6, 15, 580000),
            ("Titanium Fasteners Grade 5 (Lot)", "Aerospace Fasteners", 45, 30, 100, 42000),
            ("Aircraft Hydraulic Actuator Seal", "Hydraulics", 18, 25, 60, 22500),
            ("Cockpit Head-Up Display Panel Glass", "Optics", 3, 5, 12, 340000),
            ("Jet Engine Synthetic Lube MIL-PRF", "Fluids", 38, 25, 80, 14500),
        ]),
        ("Bharat Electronics Limited (BEL)", "BEL", [
            ("Tactical Software Defined Radio (SDR)", "Defense Telecom", 12, 15, 40, 290000),
            ("Multilayer Military Grade PCB Substrate", "Electronics", 90, 50, 250, 6500),
            ("Thermal Imaging Night Sensor Module", "Optronics", 6, 10, 25, 420000),
            ("Hermetic Sealed Mil-Spec Connectors", "Interconnect", 140, 80, 300, 2800),
            ("RF Power Amplifier Transistor 50W", "RF Components", 55, 40, 150, 7400),
        ]),
        ("Mazagon Dock Shipbuilders", "MDL", [
            ("Marine Grade Steel Plate AH36", "Hull Material", 65, 40, 150, 88000),
            ("Submarine Valve Titanium Alloy", "Naval Systems", 8, 10, 25, 210000),
            ("Sacrificial Zinc Anodes for Hull", "Cathodic Protection", 180, 90, 400, 3200),
            ("Watertight Bulkhead Door Seals", "Ship Spares", 24, 25, 70, 16500),
            ("Marine Propeller Shaft Bearing", "Propulsion", 3, 5, 12, 450000),
        ]),

        # Logistics, Paints & Construction
        ("Blue Dart Express - Hub Maintenance", "BD", [
            ("Conveyor Sorter Drive Rollers", "Automation", 55, 30, 120, 4200),
            ("Heavy Duty Aviation Cargo Netting", "Air Cargo", 18, 25, 60, 14500),
            ("Handheld Delivery PDA Scanners", "Field Mobility", 28, 40, 100, 12500),
            ("Castor Wheels for Airport Dollies", "Ground Support", 110, 60, 250, 850),
            ("Weigh-in-Motion Sensor Cells", "Sorting", 9, 12, 30, 28000),
        ]),
        ("Asian Paints - Kasna Production Plant", "AP", [
            ("Titanium Dioxide Rutile (Tons)", "Pigment Raw", 45, 30, 100, 260000),
            ("Pure Acrylic Emulsion Polymer (Drums)", "Resins", 68, 40, 150, 34000),
            ("Automated Paint Tinting Valve Nozzle", "Dispensing Spares", 15, 20, 50, 8900),
            ("Metal Paint Cans 20L (Empty Bulk)", "Packaging", 1200, 500, 3000, 145),
            ("Dispersing Additive BYK-190 (25kg)", "Chemicals", 18, 25, 60, 19500),
        ]),
        ("UltraTech Cement - Bulk Terminal", "UTC", [
            ("Portland Pozzolana Clinker (Tons)", "Raw Material", 750, 300, 1500, 4200),
            ("Ball Mill Grinding Media Steel Balls", "Milling Spares", 85, 50, 200, 65000),
            ("HDPE Woven Cement Bags 50kg (Bundle)", "Bags", 4200, 2000, 10000, 14.5),
            ("Rotary Kiln Tyre Lubricating Grease", "Lubrication", 22, 25, 70, 21000),
            ("Baghouse Dust Filter Bags PTFE", "Filtration", 190, 100, 450, 1850),
        ]),
        ("Pidilite Industries - Vapi Plant", "PID", [
            ("Vinyl Acetate Monomer (VAM Bulk L)", "Chemical Raw", 6200, 3000, 15000, 115),
            ("Fevicol Plastic Squeeze Bottles 250g", "Packaging", 3400, 1500, 8000, 9.8),
            ("Epoxy Resin Part A + Hardener B", "Adhesive Bulk", 48, 40, 120, 14200),
            ("Continuous Mixing Impeller Blade", "Plant Spares", 6, 8, 20, 45000),
            ("Hot Melt Glue Gun Industrial 300W", "Application Tools", 32, 20, 80, 2400),
        ]),
        ("Delhivery Mega Gateway - North Hub", "DEL", [
            ("Cross-Belt Sorter Carrier Trays", "Intralogistics", 42, 30, 100, 6800),
            ("Telescopic Truck Unloading Conveyor", "Dock Spares", 2, 4, 10, 380000),
            ("Thermal Printhead Zebra ZT411", "Printing Spares", 14, 20, 50, 11500),
            ("Security Tamper Seals (Box 5000)", "Tracking", 45, 30, 100, 1900),
            ("Motorized Roller Drive Pulley 48V", "Conveyor Parts", 28, 25, 75, 9500),
        ]),
    ]

    db = {}
    for org_name, sku_prefix, items in raw_companies:
        item_list = []
        for idx, (item, category, current_stock, reorder_lvl, max_cap, unit_cost) in enumerate(items, start=1):
            item_list.append({
                "SKU": f"{sku_prefix}-{idx:03d}",
                "Item": item,
                "Category": category,
                "Current_Stock": current_stock,
                "Reorder_Level": reorder_lvl,
                "Max_Capacity": max_cap,
                "Unit_Cost_INR": float(unit_cost)
            })
        db[org_name] = pd.DataFrame(item_list)
    return db

# Session State Initialization
if "inventory_db" not in st.session_state:
    st.session_state.inventory_db = load_initial_data()

# ----------------------------------------------------
# 2. SIDEBAR - COMPANY SELECTOR & CONFIG
# ----------------------------------------------------
st.sidebar.title("🏢 Enterprise Hub")
companies = sorted(list(st.session_state.inventory_db.keys()))

st.sidebar.markdown(f"**Indexed Companies:** `{len(companies)} Active Organizations`")
selected_company = st.sidebar.selectbox("Select Target Enterprise:", companies)

st.sidebar.markdown("---")
st.sidebar.subheader("➕ Add SKU to Current Inventory")

with st.sidebar.form("add_stock_form", clear_on_submit=True):
    sku = st.text_input("SKU Code (e.g., SK-999)")
    item_name = st.text_input("Item Name")
    category = st.text_input("Category", value="General")
    stock = st.number_input("Current Stock", min_value=0, value=50, step=1)
    reorder_level = st.number_input("Reorder Level", min_value=1, value=20, step=1)
    max_cap = st.number_input("Max Capacity", min_value=10, value=100, step=1)
    unit_cost = st.number_input("Unit Cost (₹)", min_value=1.0, value=500.0, step=10.0)
    
    submitted = st.form_submit_button("Add to Inventory")
    if submitted:
        if sku and item_name:
            new_item = {
                "SKU": sku.strip().upper(),
                "Item": item_name.strip(),
                "Category": category.strip(),
                "Current_Stock": int(stock),
                "Reorder_Level": int(reorder_level),
                "Max_Capacity": int(max_cap),
                "Unit_Cost_INR": float(unit_cost)
            }
            st.session_state.inventory_db[selected_company] = pd.concat(
                [st.session_state.inventory_db[selected_company], pd.DataFrame([new_item])],
                ignore_index=True
            )
            st.sidebar.success(f"Added {item_name} to {selected_company}!")
            st.rerun()
        else:
            st.sidebar.error("SKU aur Item Name daalna zaroori hai.")

# ----------------------------------------------------
# 3. SMART DATA PROCESSING
# ----------------------------------------------------
df = st.session_state.inventory_db[selected_company].copy()

def evaluate_stock_status(row):
    if row["Current_Stock"] == 0:
        return "Critical: Out of Stock"
    elif row["Current_Stock"] <= row["Reorder_Level"]:
        return "Warning: Low Stock"
    elif row["Current_Stock"] > (row["Max_Capacity"] * 0.9):
        return "Notice: Near Overstock"
    else:
        return "Optimal"

def calculate_recommended_order(row):
    if row["Current_Stock"] <= row["Reorder_Level"]:
        return max(0, row["Max_Capacity"] - row["Current_Stock"])
    return 0

df["Stock_Status"] = df.apply(evaluate_stock_status, axis=1)
df["Suggested_Reorder_Qty"] = df.apply(calculate_recommended_order, axis=1)
df["Total_Inventory_Value_INR"] = df["Current_Stock"] * df["Unit_Cost_INR"]

# ----------------------------------------------------
# 4. MAIN DASHBOARD VIEW
# ----------------------------------------------------
st.title(f"📦 Smart Inventory Dashboard: {selected_company}")
st.caption("Enterprise multi-tenant supply telemetry, replenishment forecasts, and asset valuation metrics.")

# Top KPI Cards
total_items = len(df)
low_stock_count = len(df[df["Current_Stock"] <= df["Reorder_Level"]])
total_valuation = df["Total_Inventory_Value_INR"].sum()
critical_count = len(df[df["Current_Stock"] == 0])

col1, col2, col3, col4 = st.columns(4)
col1.metric("Total SKU Count", f"{total_items} Items")
col2.metric("Total Inventory Value", f"₹ {total_valuation:,.2f}")
col3.metric(
    "Low Stock Alerts",
    f"{low_stock_count}",
    delta=f"-{low_stock_count}" if low_stock_count > 0 else "0",
    delta_color="inverse"
)
col4.metric(
    "Out of Stock",
    f"{critical_count}",
    delta="Action Req" if critical_count > 0 else "All Good",
    delta_color="inverse"
)

st.markdown("---")

# ----------------------------------------------------
# 5. INVENTORY TABLE WITH ALERT STYLING
# ----------------------------------------------------
st.subheader("📋 Live Inventory Status & Restock Engine")

def highlight_alerts(val):
    if "Critical" in str(val):
        return "background-color: #ff4d4d; color: white; font-weight: bold;"
    elif "Warning" in str(val):
        return "background-color: #ffa64d; color: black; font-weight: bold;"
    elif "Optimal" in str(val):
        return "background-color: #d4edda; color: #155724;"
    elif "Notice" in str(val):
        return "background-color: #d1ecf1; color: #0c5460;"
    return ""

styled_df = df.style.map(highlight_alerts, subset=["Stock_Status"]).format({
    "Unit_Cost_INR": "₹ {:,.2f}",
    "Total_Inventory_Value_INR": "₹ {:,.2f}"
})

st.dataframe(styled_df, use_container_width=True, height=270)

# ----------------------------------------------------
# 6. CHARTS & ANALYTICS
# ----------------------------------------------------
st.markdown("---")
st.subheader("📊 Inventory Analytics & Distribution")

chart_col1, chart_col2 = st.columns(2)

with chart_col1:
    fig_stock = px.bar(
        df,
        x="Item",
        y=["Current_Stock", "Reorder_Level"],
        barmode="group",
        title="Current Stock vs Reorder Level",
        labels={"value": "Quantity (Units)", "variable": "Stock Metric"},
        color_discrete_map={"Current_Stock": "#1f77b4", "Reorder_Level": "#ff7f0e"}
    )
    fig_stock.update_layout(xaxis_tickangle=-30)
    st.plotly_chart(fig_stock, use_container_width=True)

with chart_col2:
    fig_cat = px.pie(
        df,
        names="Category",
        values="Total_Inventory_Value_INR",
        title="Capital Allocation by Category (₹ Value)",
        hole=0.42
    )
    st.plotly_chart(fig_cat, use_container_width=True)