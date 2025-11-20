with open('ZENO LocalFlow — Business Plan.md', 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace('ZENO LocalFlow', 'ZENO CY')

with open('ZENO LocalFlow — Business Plan.md', 'w', encoding='utf-8') as f:
    f.write(content)

print("Done! Replaced all occurrences of 'ZENO LocalFlow' with 'ZENO CY'")
