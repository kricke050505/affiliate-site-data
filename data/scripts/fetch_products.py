import json
from pathlib import Path

products = [
    {
        "name": "AI Video Builder",
        "description": "Create AI videos automatically",
        "category": "AI Tools",
        "image": "https://placehold.co/600x400",
        "affiliate_link": "https://example.com"
    },
    {
        "name": "AI Course Creator",
        "description": "Build online courses using AI",
        "category": "Courses",
        "image": "https://placehold.co/600x400",
        "affiliate_link": "https://example.com"
    }
]

output_path = Path("data/products.json")
output_path.parent.mkdir(parents=True, exist_ok=True)

output_path.write_text(
    json.dumps(products, indent=2, ensure_ascii=False),
    encoding="utf-8"
)

print("Products updated")
