# Supply Chain Application - Complete Documentation

**Version:** 1.0  
**ERPNext Version:** 15  
**Last Updated:** December 2025

---

## Overview

The **Supply Chain Application** is an ERPNext v15 custom app for pharmaceutical inventory management with two core modules:

### Module 1: Agency Management
Manages supplier agencies, tracks their supplied items, and auto-generates ERPNext Suppliers.

### Module 2: Manufacturer-Item Mapping
Maps manufacturers to items with part numbers and GTINs, with manufacturer blocking and unique constraints.

---

## Installation & Setup

### Prerequisites
- ERPNext v15
- Frappe Framework
- MySQL/MariaDB
- Python 3.8+

### Setup Steps

```bash
# 1. Create new bench
bench init frappe-bench --frappe-branch version-15
cd frappe-bench

# 2. Get ERPNext
bench get-app erpnext --branch version-15

# 3. Get Supply Chain App
bench get-app https://github.com/jaffar-sherif/supply-chain.git

# 4. Create site
bench new-site supply_chain.local

# 5. Install ERPNext
bench --site supply_chain.local install-app erpnext

# 6. Install Supply Chain App
bench --site supply_chain.local install-app supply_chain

# 7. Start bench
bench start
```

**Access:** http://supply_chain.local:8000

---

## Module 1: Agency Management

### Features & Requirements

#### ✅ Prevent Deactivating Agency with Items
- Cannot deactivate an Agency if it has linked items in the Agency Item table
- **Error Message:** "Cannot deactivate {agency_name} as this agency has N items"
- User must remove items first or keep agency active

#### ✅ Create Supplier Button
- Auto-generates ERPNext Supplier from Agency details
- Button appears only if:
  - Agency is active (is_active = 1)
  - Agency is saved (not new)
  - No supplier already linked
- Auto-creates Contact with email and phone
- Links supplier back to Agency

#### ✅ Inactive Agencies in Red on List View
- Active agencies: Normal background + Green [Active] badge
- Inactive agencies: Normal background  + Red [Inactive] badge + Highlight Agency name in red

#### ✅ Agency Lead Times Report
- View all agencies with their supplied items
- Columns: Agency ID, Agency Name, Item Code, Item Name, Min Order Qty, Lead Time Days
- Filters: Agency, Item Code, Lead Time (Days) <=

---

## Module 2: Manufacturer-Item Mapping

### Features & Requirements

#### ✅ Block Manufacturer Items When Blocked
- If Manufacturer.is_blocked = 1, cannot add items
- Blocked manufacturers don't appear in Link field dropdown
- If blocked manufacturer ID is manually entered, validation throws error
- **Error Message:** "Cannot add items for blocked manufacturer {name}"

#### ✅ Unique (Manufacturer, Item) Pair
- Cannot add same item from same manufacturer twice
- **Error Message:** "Manufacturer-Item mapping already exists"
- Applies to child table entries

#### ✅ Auto-fill Part Number
- If manufacturer_part_no is left blank, auto-fills with item_code on save
- Example: Leave blank, save → part_number becomes "PARA-500"
- Can be overridden with custom value

#### ✅ REST API: Get Manufacturers by Item
**Endpoint:**
```
POST /api/method/supply_chain.supply_chain.api.get_manufacturers_by_item
```

**Request:**
```json
{
  "item_code": "PARA-500"
}
```

**Response:**
```json
{
  "message": {
    "item_code": "PARA-500",
    "manufacturers": [
      {
        "manufacturer": "Pfizer",
        "manufacturer_part_no": "PFZ-PARA-500-001",
        "custom_gtin": "5901234123457"
      },
      {
        "manufacturer": "Sun Pharma",
        "manufacturer_part_no": "SUN-PARA-500-001",
        "custom_gtin": "8901234567890"
      }
    ],
    "status": "Success"
  }
}
```

#### ✅ Items by Manufacturer Report
- View all items mapped to selected manufacturer
- Columns: Manufacturer Name, Item Name, Manufacturer Part No, GTIN
- Filters: Manufacturer, Item Code

**Last Updated:** December 2025  
**Repository:** https://github.com/jaffar-sherif/supply-chain.git
