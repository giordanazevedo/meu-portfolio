import re

with open('style.css', 'r', encoding='utf-8') as f:
    content = f.read()

# Locate the end of the .hero-image img block inside the media query
# We search for: .hero-btns { flex-direction: column; width: 100%; }\n\n}
# followed by blank lines and then /* Configurações específicas da Galeria */
pattern = r'(\.hero-btns \{\s*flex-direction:\s*column;\s*width:\s*100\s*%;\s*\}\s*\}\s*\n\s*)(/\*\s*Configurações específicas da Galeria\s*\*/)'

match = re.search(pattern, content)
if match:
    print("Found match! Inserting closing brace.")
    # Add a closing brace to close the media query
    content_fixed = content[:match.end(1)] + "}\n\n" + content[match.start(2):]
    with open('style.css', 'w', encoding='utf-8') as f:
        f.write(content_fixed)
else:
    print("Match not found.")
