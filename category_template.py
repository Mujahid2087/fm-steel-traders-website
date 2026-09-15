from pathlib import Path
import json, re
base=Path('/mnt/data/fmsteel_v3_base')
email='mujahiddongarkar@gmail.com'
phone='+91 99231 23467'
wa='919923123467'

pages={
'ms-plain-washers.html':{
 'title':'MS Plain Washer Supplier in Pune | FM STEEL TRADERS',
 'desc':'FM STEEL TRADERS supplies Mild Steel (MS) plain washers from Chakan, Pune for bulk industrial requirements. Standard and custom OD × ID × thickness sizes.',
 'h1':'MS Plain Washers Supplier in Pune',
 'intro':'FM STEEL TRADERS supplies Mild Steel plain washers for bulk industrial and B2B requirements from Chakan, Pune. The current range includes multiple OD × ID × thickness combinations, with custom-size requirements considered on request.',
 'sections':[
 ('What is an MS Plain Washer?','An MS plain washer is a flat washer made from Mild Steel and used with fasteners where a washer is required as part of an assembly. For purchasing, the key dimensions are outer diameter (OD), inner diameter (ID) and thickness.'),
 ('Current MS Plain Washer Range','Our current listed range covers 12 MS plain/flat washer sizes. Each listed size has a dedicated product page with its dimensions and enquiry option.'),
 ('Manufacturing & Finishing','FM STEEL TRADERS uses power-press stamping followed by tumbling/deburring. Raw MS is the standard finish. Zinc plating can be arranged on request at additional cost.'),
 ('Inspection Information','Current stated checks include OD, ID, thickness and visual checks for defects such as rust and cracks. Customer-specific material grades, tolerances and inspection requirements should be confirmed before production or supply.'),
 ],
 'links':[('View all MS washer sizes','products.html'),('MS Flat Washers','ms-flat-washers.html'),('Industrial MS Washers','industrial-ms-washers.html'),('Custom Size Washers','custom-ms-washers.html')]
},
'ms-flat-washers.html':{
 'title':'MS Flat Washer Supplier in Pune | FM STEEL TRADERS',
 'desc':'Bulk MS flat washer supply from FM STEEL TRADERS, Chakan Pune. Plain flat washers in listed OD × ID × thickness sizes; custom requirements can be discussed.',
 'h1':'MS Flat Washers for Bulk Industrial Supply',
 'intro':'FM STEEL TRADERS supplies Mild Steel flat washers for industrial hardware, fastener distribution, engineering, fabrication and other bulk requirements. Dimensions are specified as OD × ID × thickness.',
 'sections':[
 ('MS Flat Washer Dimensions','Washer selection should be based on the required outer diameter, inner diameter and thickness. FM STEEL TRADERS currently lists 12 standard size combinations and can discuss additional custom dimensions.'),
 ('Flat Washer Supply from Chakan','Supply is coordinated from Chakan, Pune. Typical minimum order preference is 1 MT per size, subject to the requirement and commercial discussion.'),
 ('Finish Options','Raw MS is the standard finish. Zinc plating can be arranged on request at additional cost.'),
 ('Before Ordering','Please confirm size, quantity, material/grade if specified, finish, delivery location and any drawing or inspection requirement before production or supply.'),
 ],
 'links':[('MS Plain Washers','ms-plain-washers.html'),('View all sizes','products.html'),('Industrial MS Washers','industrial-ms-washers.html'),('Custom Size Washers','custom-ms-washers.html')]
},
'industrial-ms-washers.html':{
 'title':'Industrial MS Washer Supplier in Pune | FM STEEL TRADERS',
 'desc':'Industrial Mild Steel washer supply from Chakan, Pune for fastener, engineering, fabrication, machinery and industrial hardware requirements. Bulk orders welcome.',
 'h1':'Industrial MS Washers for Bulk Requirements',
 'intro':'FM STEEL TRADERS supports bulk industrial requirements for Mild Steel plain and flat washers from Chakan, Pune. The target applications include fastener distribution, industrial hardware, general engineering, fabrication, machinery and agricultural equipment requirements.',
 'sections':[
 ('Industries & Buying Requirements','Our washer range can be considered by fastener businesses, industrial hardware suppliers, engineering and fabrication companies, machinery-related businesses and other buyers requiring bulk plain washers.'),
 ('Bulk Supply Capability','The current stated supply capability is approximately 25–30 MT/month across washer production/supply. A typical minimum order preference is 1 MT per size.'),
 ('Production Process','The stated process uses power-press stamping followed by tumbling/deburring. Residual burr may remain, so customer application requirements should be reviewed before supply.'),
 ('Quality Information','Current checks include OD, ID, thickness and visual inspection for rust, cracks and other visible defects. Formal customer-specific tolerances or inspection plans should be agreed before production when required.'),
 ],
 'links':[('MS Plain Washers','ms-plain-washers.html'),('MS Flat Washers','ms-flat-washers.html'),('View product sizes','products.html'),('Custom Size Washers','custom-ms-washers.html')]
},
'custom-ms-washers.html':{
 'title':'Custom MS Washer Supplier in Pune | OD ID Thickness',
 'desc':'Custom Mild Steel washer requirements from FM STEEL TRADERS, Chakan Pune. Share OD × ID × thickness, quantity, finish and drawing/specification for review.',
 'h1':'Custom Size MS Washers',
 'intro':'FM STEEL TRADERS can discuss custom Mild Steel plain/flat washer requirements where the required OD × ID × thickness is different from the currently listed standard sizes.',
 'sections':[
 ('What to Send for a Custom Washer Enquiry','Please send the required outer diameter (OD), inner diameter (ID), thickness, quantity, finish and delivery location. If available, include a drawing, sample details or customer specification.'),
 ('Material & Finish','Mild Steel is the current material offering. Raw MS is the standard finish and zinc plating can be arranged on request at additional cost. If a particular material grade or plating specification is required, it should be stated before quotation.'),
 ('Production Review','Custom requirements should be reviewed for tooling, material availability, dimensions, quantity and commercial feasibility before confirmation. Do not assume a custom size is available until FM STEEL TRADERS confirms it.'),
 ('Quality & Inspection','Current stated checks include OD, ID, thickness and visual checks. Any required dimensional tolerances, inspection criteria or documentation should be communicated before production or supply.'),
 ],
 'links':[('MS Plain Washers','ms-plain-washers.html'),('MS Flat Washers','ms-flat-washers.html'),('Industrial MS Washers','industrial-ms-washers.html'),('View listed sizes','products.html')]
}}

# common navigation/footer
nav='''<div class="topbar"><div class="wrap"><span>MS Plain & Flat Washers • Bulk Industrial Supply</span><span>Chakan, Pune, Maharashtra • India</span></div></div><header class="header"><div class="wrap nav"><a class="brand" href="index.html" aria-label="FM STEEL TRADERS Home"><div class="logo">FM</div><div><strong>FM STEEL TRADERS</strong><span>MS WASHERS • INDUSTRIAL SUPPLY</span></div></a><nav class="menu"><a href="index.html">Home</a><a href="company.html">Company</a><a class="active" href="products.html">Products</a><a href="contact.html">Contact</a><a href="return-policy.html">Return Policy</a><a class="btn" href="contact.html">Send Enquiry</a></nav></div></header>'''
footer=f'''<footer class="footer"><div class="wrap footergrid"><div><h3>FM STEEL TRADERS</h3><p>Bulk supplier/manufacturer of Mild Steel plain and flat washers from Chakan, Pune.</p></div><div><h3>Product Pages</h3><p><a href="ms-plain-washers.html">MS Plain Washers</a><br><a href="ms-flat-washers.html">MS Flat Washers</a><br><a href="industrial-ms-washers.html">Industrial MS Washers</a><br><a href="custom-ms-washers.html">Custom MS Washers</a></p></div><div><h3>Contact</h3><p>📞 <a href="tel:+919923123467">{phone}</a><br>✉ <a href="mailto:{email}">{email}</a><br>📍 Chakan, Pune, Maharashtra, India</p></div></div><div class="wrap copyright">© 2026 FM STEEL TRADERS. All rights reserved.</div></footer><div class="mobilebar"><a href="tel:+919923123467">CALL</a><a href="https://wa.me/{wa}">WHATSAPP</a><a href="contact.html">ENQUIRE</a></div>'''

for fn,p in pages.items():
 url='https://fmsteeltraders.in/'+fn
 breadcrumb=json.dumps({"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":1,"name":"Home","item":"https://fmsteeltraders.in/"},{"@type":"ListItem","position":2,"name":"Products","item":"https://fmsteeltraders.in/products.html"},{"@type":"ListItem","position":3,"name":p['h1'],"item":url}]},ensure_ascii=False,separators=(',',':'))
 local=json.dumps({"@context":"https://schema.org","@type":"WebPage","name":p['h1'],"url":url,"description":p['desc'],"about":{"@type":"Thing","name":"Mild Steel Washers"},"isPartOf":{"@type":"WebSite","name":"FM STEEL TRADERS","url":"https://fmsteeltraders.in/"}},ensure_ascii=False,separators=(',',':'))
 cards=''.join(f'<div class="card"><div class="pad"><h3>{h}</h3><p>{t}</p></div></div>' for h,t in p['sections'])
 links=''.join(f'<a class="btn alt" href="{u}">{label}</a>' for label,u in p['links'])
 html=f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{p['title']}</title><meta name="description" content="{p['desc']}"><meta name="robots" content="index,follow"><link rel="canonical" href="{url}"><meta property="og:title" content="{p['title']}"><meta property="og:description" content="{p['desc']}"><meta property="og:url" content="{url}"><meta property="og:type" content="website"><link rel="stylesheet" href="styles.css"><script type="application/ld+json">{breadcrumb}</script><script type="application/ld+json">{local}</script></head><body>{nav}<section class="pagehero"><div class="wrap"><div class="crumb"><a href="index.html">Home</a> / <a href="products.html">Products</a> / {p['h1']}</div><h1>{p['h1']}</h1><p>{p['intro']}</p></div></section><section class="section"><div class="wrap"><div class="grid products">{cards}</div></div></section><section class="section gray"><div class="wrap"><h2>Explore FM STEEL TRADERS Washer Categories</h2><p class="lead">Choose a category below or view the complete listed size range.</p><div class="actions">{links}</div></div></section><section class="cta"><div class="wrap"><div><h2>Have a washer requirement?</h2><p>Send OD × ID × thickness, quantity, finish and delivery location for review.</p></div><div class="actions"><a class="btn" href="mailto:{email}?subject=MS%20Washer%20Requirement">Email Us</a><a class="btn whatsapp" href="https://wa.me/{wa}?text=Hello%20FM%20STEEL%20TRADERS%2C%20I%20have%20an%20MS%20washer%20requirement.">WhatsApp</a></div></div></section>{footer}</body></html>'''
 (base/fn).write_text(html,encoding='utf-8')

# update products page with category section before CTA
f=base/'products.html'; s=f.read_text(encoding='utf-8')
marker='<section class="cta">'
section='''<section class="section"><div class="wrap"><h2>MS Washer Product Categories</h2><p class="lead">Explore broader washer categories before selecting an exact size.</p><div class="grid products"><div class="card"><div class="pad"><h3><a href="ms-plain-washers.html">MS Plain Washers</a></h3><p>Mild Steel plain washer supply for bulk industrial requirements.</p></div></div><div class="card"><div class="pad"><h3><a href="ms-flat-washers.html">MS Flat Washers</a></h3><p>Flat washer dimensions listed by OD × ID × thickness.</p></div></div><div class="card"><div class="pad"><h3><a href="industrial-ms-washers.html">Industrial MS Washers</a></h3><p>Bulk washer supply for engineering, hardware, fabrication and machinery requirements.</p></div></div><div class="card"><div class="pad"><h3><a href="custom-ms-washers.html">Custom Size MS Washers</a></h3><p>Discuss custom OD × ID × thickness requirements.</p></div></div></div></div></section>'''
if marker in s and 'MS Washer Product Categories' not in s:
 s=s.replace(marker,section+marker)
f.write_text(s,encoding='utf-8')

# add links from homepage keyword-links
f=base/'index.html'; s=f.read_text(encoding='utf-8')
old='<div class="keyword-links"><a href="products.html">MS plain washer sizes</a><a href="products.html">MS flat washer supplier</a><a href="contact.html">Bulk washer quotation</a><a href="company.html">Washer supplier Chakan</a></div>'
new='<div class="keyword-links"><a href="ms-plain-washers.html">MS plain washer supplier</a><a href="ms-flat-washers.html">MS flat washer supplier</a><a href="industrial-ms-washers.html">Industrial MS washers</a><a href="custom-ms-washers.html">Custom MS washers</a><a href="products.html">All washer sizes</a><a href="contact.html">Bulk washer quotation</a></div>'
if old in s: s=s.replace(old,new)
f.write_text(s,encoding='utf-8')

# update sitemap
urls=['https://fmsteeltraders.in/','https://fmsteeltraders.in/company.html','https://fmsteeltraders.in/products.html','https://fmsteeltraders.in/contact.html','https://fmsteeltraders.in/return-policy.html','https://fmsteeltraders.in/ms-plain-washers.html','https://fmsteeltraders.in/ms-flat-washers.html','https://fmsteeltraders.in/industrial-ms-washers.html','https://fmsteeltraders.in/custom-ms-washers.html']
# add exact product urls
for x in sorted(base.glob('product-ms-washer-*.html')): urls.append('https://fmsteeltraders.in/'+x.name)
xml='<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'+''.join(f'<url><loc>{u}</loc></url>' for u in urls)+'</urlset>'
(base/'sitemap.xml').write_text(xml,encoding='utf-8')

print('created', [x for x in pages])
